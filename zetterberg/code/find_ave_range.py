def find_ave_range(directory_files,output_file,variable,maximum = False):
        '''
        A function written to find which files in a group of lidar data show cloud formation.
        Inputs: directory_files = files to analyze
                output_file = name of file which output is written to
                variable = which variable to run over (snr or mean_velocity)
                maximum = if True, will find the max of the file instead of the average, does not work for snr
        '''
        import numpy as np
        import xarray as xr
        
        file_list = np.loadtxt(directory_files,delimiter = '\n',dtype = 'str')
        output_list = []
        
        #just setting it up for average of mean_velocity for now
        for i in np.arange(len(file_list)):
                ds = xr.open_dataset(file_list[i])
                print(file_list[i] + ':   read')
                mean_vel = ds.mean_velocity
                average_vel_list = []
                for k in range(0,len(vel.time),50):
                        total_vel = 0
                        counter = 0
                        for j in range(0,len(vel.range),10):
                                if np.isnan(vel[k,j]) == False:
                                        counter += 1 
                                        total_vel += vel[k,j]
                        average_vel_list.append(total_vel/counter)
                average_vel = sum(average_vel_list)/len(average_vel_list)
                output_list.append(average_vel)        
        
        #writing to the output file
        f = open(output_file, 'w')
        for i in range(len(output_list)):
                f.write(str(file_list[i]) + ':    ' + str(output_list[i]) + '\n')
        f.close()
        
        

