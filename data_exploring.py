# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:32:50 2023

@author: gfagu
"""

# import data_extract
import xarray as xr
import matplotlib.pyplot as plt

# root_path = r'C:/Users/gfagu/Guilherme/IC/spyder/radioOccultation/'


# Format: 
# days = {
#     '2015_001': {
#         'C006.2015.003.21.43.G30_2021.0390_nc': Xarray dataset
#     }        
# }
# data = data_cleaning.clean_data(root_path)
# data1 = data['2015_001']['C001.2015.001.00.11.G06_2021.0390_nc']

    
def plot_profile(data):
    xr.plot.scatter(data, x="ELEC_dens", y="MSL_alt", ylim=150)


def plot_profiles(datas):
    for data in datas:
        plt.figure()
        xr.plot.scatter(data, x="ELEC_dens", y="MSL_alt", ylim=150)
        plt.title(data.attrs['local_time'])
        plt.show()
        
        
def profiles_by_hour(datas):
    profiles_by_hour = {}
    index = 0
    while (index < len(datas)):
        day = datas[index].attrs['local_time'].day
        hour = datas[index].attrs['local_time'].hour
        key = str(day) + '_' + str(hour)
        hour_list = []
        while (datas[index].attrs['local_time'].day == day and datas[index].attrs['local_time'].hour == hour):
            hour_list.append(datas[index])
            index += 1
            if (index == len(datas)):
                break
        profiles_by_hour[key] = hour_list
    return profiles_by_hour
        
def mean_by_hour(profiles_by_hour):
    mean_by_hour = {}
    for key, datas in profiles_by_hour.items():
        interpol_arrays = [da.interp(MSL_alt=datas[0]['MSL_alt']) for da in datas]
        avg_data = xr.concat(interpol_arrays, dim='datas').mean(dim='datas')
        mean_by_hour[key] = avg_data
    return mean_by_hour        
        

def plot_profiles_by_hour(dic_datas):
    for key, data in dic_datas.items():
        plt.figure()
        xr.plot.scatter(data, x="ELEC_dens", y="MSL_alt", ylim=150)
        plt.title(key)
        plt.show()
      
        
# def plot_mean_by_hour_compare_days(dic_datas):
#     dic_by_hour = {}
#     for key, data in dic_datas.items():
#         hour = key.split('_')[-1]
#         dic_by_hour[hour] = 

"""

- perfil médio por dia

- perfil médio por hora

- heatmap

- perfis ao longo do tempo => sazonalidade

"""