import numpy as np
import matplotlib.pyplot as plt

def plot_pca_space(points,labels,centers,HeatMap=False,plot_title='temp'):
    '''
    '''
    from matplotlib import cm
    from matplotlib.colors import Normalize
    from scipy.interpolate import interpn
    
    fig,ax=plt.subplots()
    color_list=
    
    labels_unique = list(set(labels))
    
    if HeatMap==False:
        for i in np.arange(len(labels_unique)):
            ax.scatter(points[l==i,0],points[l==i,1],marker='.',c=color_list[i],label=color_list[i])
            
        ax.scatter(c[:,0],c[:,1],c='red',label='Cluster Centers')
        
        ax1.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))
        
    if HeatMap == True:
        import pandas as pd
        df=pd.DataFrame(points,columns=['component1','component2'])
        df['labels']=labels
        
        data,x_e,y_e=np.histogram2d(df.component1,df.component2,bins=20,density=True)
        z=interpn((.5*(x_e[1:]+x_e[:-1]),.5*(y_e[1:]+y_e[:-1])),data,np.vstack(df.component1,df.component2).T,method           = spline2fd',bounds_error=False)
        
        idx=z.argsort()
        x,y,z=df.component1[idx],df.component2[:,1][idx],z[idx]
        
        ax.scatter(x,y,c=z)
        norm=Normalize(vmin=np.min(z),vmax=np.max(z))
        cbar=fig.colorbar(cm.ScalarMappable(norm=nom),ax=ax)
        cbar=ax.set_ylabel('Point Density')
        
        for i in labels_unique:
            pts=df[df.labels==i][['component1','component2']].values
            #get convex hull
            hull=ConvexHull(pts)
            #get x and y coordinates
            #repeat last point to close the polygon
            x_hull=np.append(pts[hull.vertices,0],pts[hull.vertices,0][0])
            y_hull=np.append(pts[hull.vertices,1],pts[hull.vertices,1][0])
            
            #plot shape
            ax.plot(x_hull,y_hull,c='red')
    
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    fig.savefig(plot_title)
    
    return None
        
        
def plot_time_range_space(labels,label_data,plot_title):
    '''
    '''
    import xarray as xr
    
    from matplotlib import cm
    from matplotlib.colors import ListedColormap
    from matplotlib.colors
    
    cmap0=ListedColormap(['blue','orange','green','darkqurquoise','magenta'])
    
    label_dataset=xr.open_dataset(label_array)
    label_dataarray=label_dataset.labels
    label_array=label_dataarray.to_numpy()
    
    fig,ax=plt.subplots()
    ax.pcolormesh(np.arange(len(label_array[0])),np.arange(len(label_array[1])),label_array,cmap=cmap0)
    
    fig.savefit(plot_title)
    
    return None
        
def plot_power_spectra(power_data,label_data,plot_name = 'none.png'):
    '''
    '''
    import xarray as xr
    
    labels=xr.open_dataset(label_data)
    power=xr.open_dataset(power_data)
    
    
    labels_unique = list(set(labels))
    color_list=['blue','orange','green','darkqurquoise','magenta']
    cmap0=ListedColormap(color_list)
    
    power_list = []
    for i in np.arange(len(labels_unique)):
        power_temp_list = []
        for j in np.arange(len(power.vel_bins)):
            power_temp=power[:,:,j].where(labels.labels==i).mean()
            power_temp_list.append(power_temp)
        
        power_list.append(power_temp_list)
    
    x_axis=np.asarray([-19.35,-18.141,-16.931,-15.722,-14.513,-13.303,-12.094,-10.884,-9.675,-8.466,-7.256,-6.047,-4.838,-3.628,-2.149,-1.209,0,1.209,2.419,3.628,4.838,6.047,7.256,8.466,9.675,10.884,12.094,13.303,14.513,15.722,16.961,18.141])
    for k in np.arange(len(power_list)):
        plt.plot(x_axis,power_list[k],color=color_list[k],label=color_list[k])
        
    plt.xlabel(r'Doppler Velocity $m^{-1}$')
    plt.ylabel(r'p.d.f. of power spectra (%)')
    plt.savefig(plot_name)
    
    return None
        