# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:32:50 2023

@author: gfagu
"""

import data_cleaning
# import data_extract

root_path = r'C:/Users/gfagu/Guilherme/IC/spyder/radioOccultation/'


# Format: 
# days = {
#     '2015_001': {
#         'C006.2015.003.21.43.G30_2021.0390_nc': Xarray dataset
#     }        
# }
data = data_cleaning.clean_data(root_path)

"""
what to do:
    
- compare tecs => identify pattern in wrong tecs

- plots by hour

- detect anomalys

- 

"""
