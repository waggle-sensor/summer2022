
#importing packages
import os
import numpy as np
import xarray as xr
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

#getting the list of files
all_files = os.listdir('/lcrc/group/earthscience/rjackson/sgp_lidar/processed_moments/')
files = []
txt='/lcrc/group/earthscience/rjackson/sgp_lidar/processed_moments/'
for i in all_files:
    if i[-1]=='c' and i[0] != '1':
        files.append(txt + i)
files.sort()
    
#creating a large dataset
for i in np.arange(len(files)):
    if i==0:
        ds=xr.open_dataset(files[i])
        #filtering out low snr data poitns
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
ds=ds.stack(z=('range','time'))

#converting to numpy array, it is faster and easier to work with
ds=ds.to_array()

#transposing into format that PCA wants
ds=ds.transpose()

#dropping nan values
ds=ds.dropna('z')

#creating pca variable
pca=PCA(n_components=2)

#standardizing data
ds=StandardScaler().fit_transform(ds)

#doing PCA
principalComponents=pca.fit_transform(ds)

#using yellowbrick to create elbow plot        
model=KMeans()
visualizer=KElbowVisualizer(model,k=(2,10))
visualizer.fit(principalComponents)
 
#saving elbow plot 
visualizer.show(outpath="kmeans_elbow_plot_all_data.png")
        
        
    
