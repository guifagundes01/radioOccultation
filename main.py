# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 11:38:40 2023

@author: gfagu
"""

import data_cleaning
import data_exploring
import xarray as xr
import matplotlib.pyplot as plt

root_path = r'C:/Users/gfagu/Guilherme/IC/spyder/radioOccultation/'

datas = data_cleaning.clean_data(root_path)

data_exploring.plot_profile(datas[10])

print(datas[10].attrs['local_time'])

data_exploring.plot_profiles(datas[40:45])

profiles_by_hour = data_exploring.profiles_by_hour(datas)

mean_by_hour = data_exploring.mean_by_hour(profiles_by_hour)

data_exploring.plot_profiles_by_hour(mean_by_hour)

# -- 

data1 = datas[1]

data_exploring.plot_profile(data1)

data2 = datas[5]

data_exploring.plot_profile(data2)


# --
comb_datar = xr.concat([data1, data2], dim='MSL_alt')

data_exploring.plot_profile(comb_datar)

# -- 

data_interp = data1.interp(MSL_alt=data2['MSL_alt'])

mean = (data_interp + data2)/2

data_exploring.plot_profile(mean)



# data_exploring.plot_profile(comb_datar)

# mean_alt = comb_datar.mean(dim='MSL_alt')

# elec = mean_alt.ELEC_dens

# data_interp = data1.interp(MSL_alt=data2['MSL_alt'])

# mean = (data_interp + data2)/2

# data_exploring.plot_profile(mean)

# data_exploring.plot_profile(mean_alt)

# data1.plot()

# data_exploring.plot_profile(data1)
# data_exploring.plot_profile(data2)

# combined_data = xr.concat([data1, data2], dim='MSL_alt')


# xr.plot.scatter(combined_data)


# for profile in datas[:10]:
#     print(profile.attrs['local_time'].day, "  ", profile.attrs['local_time'].hour)

# profiles_by_hour = data_exploring.profiles_by_hour(datas)


# data_exploring.plot_profiles(profiles_by_hour['1_2'])



# mean_by_hour = data_exploring.mean_by_hour(profiles_by_hour)


# data_exploring.plot_profiles_by_hour(mean_by_hour)

# data_exploring.plo




# firsts = list(data1)[:10]

# for key in firsts:
#     data = data1[key]
#     plt.figure()
#     data_exploring.plot_profile(data)
#     plt.title(data.attrs['local_time'])
#     plt.show()




