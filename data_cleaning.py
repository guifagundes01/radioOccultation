# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:17:46 2023

@author: gfagu
"""

import glob
import xarray as xr 
import datetime

def local_time(data):
    attrs = data.attrs
    utc_time = datetime.datetime(year=attrs['year'], month=attrs['month'], day=int(attrs['day']), hour=int(attrs['hour']), minute=int(attrs['minute']), second=int(attrs['second']))
    local_time = utc_time + datetime.timedelta(hours=attrs['edmaxlon']/15)
    return local_time

# def clean_data(root_path):
#     days = {}
#     for day_path in glob.glob(r'./data/*'):
#         datas = []
#         for profile_path in glob.glob(day_path + '/*'):
#             data = xr.open_dataset(profile_path)
#             data.attrs['local_time'] = local_time(data)
#             datas.append(data)
#             # manipulate and clean data
#         datas.sort(key = lambda data: data.attrs['local_time'])
#         days[day_path.split(r'data')[-1][1:]] = datas 
#     return days


def clean_data(root_path):
    datas = []
    for day_path in glob.glob(r'./data/*'):
        for profile_path in glob.glob(day_path + '/*'):
            data = xr.open_dataset(profile_path)
            data.attrs['local_time'] = local_time(data)
            datas.append(data)
            # manipulate and clean data
    datas.sort(key = lambda data: data.attrs['local_time'])
    return datas


