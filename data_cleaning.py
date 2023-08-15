# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:17:46 2023

@author: gfagu
"""

import glob
import xarray as xr 
import pandas as pd

def clean_data(root_path):
    days = {}
    for day_path in glob.glob(r'./data/*'):
        datas = {}
        for profile_path in glob.glob(day_path + '/*'):
            data = xr.open_dataset(profile_path)
            datas[profile_path.split('ionPrf_')[-1]] = data
            # manipulate and clean data
            
        days[day_path.split(r'data')[-1][1:]] = datas 
    return days


