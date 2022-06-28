def process_lidar_data(filenames,label_array = False,output_file='test.nc'):
    '''
    Input: filenames: list of files (nc files of lidar data)
           label_array: xarray with labels in correct time range positions
    Output: principalComponents, labels, centers, netcdf file with label array
    
    A function that does principal component analysis and kmeans clustering of lidar data
    '''
    
    #importing packages
    import xarray as xr
    import numpy as np
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.cluster import KMeans
    
    file_number = len(filenames)
    
    #reading in data
    for i in np.arange(file_number):
        print(filenames[i])
        if i == 0:
            ds = xr.open_dataset(filenames[i])
            #filtering out snr
            snr_array=ds.snr.where(ds.snr>.5)
            ds=xr.Dataset(data_vars={'doppler_velocity':ds.doppler_velocity,
                                     'snr':snr_array,
                                     'spectral_width':ds.spectral_width,
                                     'kurtosis':ds.kurtosis})
        
        else: 
            ds_temp = xr.open_dataset(filenames[i])
            #filtering out snr
            snr_array=ds_temp.snr.where(ds_temp.snr>.5)
            ds_temp=xr.Dataset(data_vars={'doppler_velocity':ds_temp.doppler_velocity,
                                          'snr':snr_array,
                                          'spectral_width':ds_temp.spectral_width,
                                          'skewness':ds_temp.skewness,
                                          'kurtosis':ds_temp.kurtosis})
            ds=xr.concat([ds,ds_temp],dim='time')
    
    #flattening dataset
    ds2 = ds.stack(z=('range','time'))
    
    #converting to dataArray
    ds2=ds2.to_array()
    
    #transposing array
    ds2=ds2.transpose()
    
    #dropping the nan values
    ds2=ds2.dropna('z')
    
    #Principal Component Analysis
    pca = PCA(n_components=2)
    ds_standard=StandardScaler().fit_transform(ds2)
    principalComponents=pca.fit_transform(ds_standard)
    
    #kmeans with k = 5
    kmeans = KMeans(n_clusters=5,random_state=42).fit(principalComponents)
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    if label_array == True:
        #adding label variable to ds2
        ds2['label']=('z',labels)
        
        #unstacking ds2
        unstacked=ds2.unstack()
        
        #creating a dataset of just the labels
        ds_labels=unstacked.label.to_dataset(name='labels')
        
        #merging unstacked to original dataset
        merged=xr.merge([ds,ds_labels])
        merged = merged.drop(labels=['doppler_velocity','snr','spectral_width','kurtosis','label'])
        #saving values
        merged.to_netcdf(path=output_file)
        
    return principalComponents, labels, centers     
        