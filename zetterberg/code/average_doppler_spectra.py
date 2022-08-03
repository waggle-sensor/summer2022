import xarray as xr
import numpy as np
import os

#getting the list of files
file_path='/lcrc/group/earthscience/rjackson/sgp_lidar/processed_moments/'
all_files = os.listdir('/lcrc/group/earthscience/rjackson/sgp_lidar/processed_moments/')
files = []
for i in all_files:
    if i[-1]=='c' and i[0] != '1':
        files.append(file_path + i)
files.sort()

#label file was created with pca_kmeans_script
labels=xr.open_dataset('label_file_all_data.nc')
label_array = labels.label

#the average doppler spectra for the points in each cluster in each file will be
#averaged and added to power_list_list
power_list_list=[]
for i in np.arange(len(files)):
    #using load() function to ensure script runs reasonably fast
    ds=xr.open_dataset(files[i])
    ds.load()
    #filterint out data points with low snr to make code run faster
    power=ds.power_spectra_normed.where(ds.snr>.5)
    
    #the average doppler spectra for the points in each cluster will be added to power_list
    power_list=[]
    for j in np.arange(5):
        #the average doppler spectra for the points in 1 cluster will be added to power_temp_list
        power_temp_list = []
        for k in np.arange(len(power.vel_bins)):
            power_temp=power[:,:,k].where(label_array[:,2000*i:2000*(i+1)]==j).mean()
            power_temp_list.append(power_temp)
        
        #all lists are converted to numpy arrays and lists are appended
        power_temp_array=np.asarray(power_temp_list)
        power_list.append(power_temp_array)
    power_array=np.asarray(power_list)
    power_list_list.append(power_array)
    
power_array_array=np.asarray(power_list_list)

#average spectra for each cluster is added to power_l_l
power_l_l=[]
for i in np.arange(len(power_array_array[0])):
    power_l=[]
    for j in np.arange(len(power_array_array[0][0])):
        #the clusters are averaged along the first index of power_array_array
        power=power_array_array[:,i,j][~np.isnan(power_array_array[:,i,j])].mean()
        power_l.append(power)
    power_arr=np.asarray(power_l)
    power_l_l.append(power_arr)
power_arr_arr=np.asarray(power_l_l)

#power_arr_arr is the numpy array with the average doppler spectra of each spectra
temp_da = xr.DataArray(power_arr_arr)
temp_da.to_netcdf('power_spectra_all_test.nc')

