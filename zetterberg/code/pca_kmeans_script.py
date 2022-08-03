#importing packages
import os
import numpy as np
import xarray as xr
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#getting the list of files
file_path='/lcrc/group/earthscience/rjackson/sgp_lidar/processed_moments/'
all_files = os.listdir('/lcrc/group/earthscience/rjackson/sgp_lidar/processed_moments/')
files = []
for i in all_files:
    if i[-1]=='c' and i[0] != '1':
        files.append(file_path + i)
files.sort()

#creating a large dataset
for i in np.arange(len(files)):
    if i==0:
        ds=xr.open_dataset(files[i])
        #filtering out datapoints with low snr
        snr_array=ds.snr.where(ds.snr>.5)
        #creating a dataset with only the needed data variables
        ds=xr.Dataset(data_vars={'doppler_velocity':ds.doppler_velocity,
                                 'snr':snr_array,
                                 'spectral_width':ds.spectral_width,
                                 'skewness':ds.skewness,
                                 'kurtosis':ds.kurtosis})
    
    #appending files to the first file opened    
    else:
        ds_temp = xr.open_dataset(files[i])
        snr_array = ds_temp.snr.where(ds_temp.snr>.5)
        ds_temp=xr.Dataset(data_vars={'doppler_velocity':ds_temp.doppler_velocity,
                                      'snr':snr_array,
                                      'spectral_width':ds_temp.spectral_width,
                                      'skewness':ds_temp.skewness,
                                      'kurtosis':ds_temp.kurtosis})
            
        ds=xr.concat([ds,ds_temp],dim='time')

#stacking data into 1 dimensions
ds2=ds.stack(z=('range','time'))
#converting to numpy array, it is faster and easier to work with
ds2=ds2.to_array()
#transposing into format that PCA wants
ds2=ds2.transpose()
#dropping nan values
ds2=ds2.dropna('z')
#creating pca variable
pca=PCA(n_components=2)
#standardizing data
ds_standard=StandardScaler().fit_transform(ds2)

#doing PCA
principalComponents=pca.fit_transform(ds_standard)
#saving eigenvectors and eigenvalues
f = open('pca_variance_all_data.txt','w')
f.write('Eigenvectors:\n')
for i in pca.components_:
    for j in i:
        f.write(str(j)+'   ')
    f.write('\n')
    
f.write('Eigenvalues:  \n')
f.write(str(pca.explained_variance_[0]) + '   ' + str(pca.explained_variance_[1]))
f.close()

#kmeans with k = 5
kmeans=KMeans(n_clusters=5,random_state=42).fit(principalComponents)
centers=kmeans.cluster_centers_
labels=kmeans.labels_

#unstacking data and adding cluster labels to correct data points that were clustered
ds2['label']=('z',labels)
unstacked=ds2.unstack()
ds_labels=unstacked.label.to_dataset(name='labels')
merged=xr.merge([ds,ds_labels])
merged=merged.drop(labels=['doppler_velocity','snr','spectral_width','kurtosis','skewness'])
#saving labels to a file with each cluster label at correct time and range position
merged.to_netcdf(path='label_file_all_data.nc')

#saving principalCompoennts,labels,centers
pc_temp=xr.DataArray(principalComponents)
pc_temp.to_netcdf(path='pc_all_data.nc')
l_temp=xr.DataArray(labels)
l_temp.to_netcdf(path='labels_all_data.nc')
c_temp=xr.DataArray(centers)
c_temp.to_netcdf(path='centers_all_data.nc')


