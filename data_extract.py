# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:29:53 2023

@author: gfagu
"""

import urllib
import requests
import gzip
import shutil
import os
import tarfile

root_path = r'C:/Users/gfagu/Guilherme/IC/spyder/radioOccultation/'

# Function to extract netCDF files from "https://data.cosmic.ucar.edu/gnss-ro/cosmic1/" from year 2016 to 2019
def get_data(root_path, year, doymin, doymax):
    for doy in range(doymin, doymax+1):  # doy
        if doy in range(1, 10):
            url = str('https://data.cosmic.ucar.edu/gnss-ro/cosmic1/repro2021/level2/' + str(year) + '/00' + str(doy) + '/ionPrf_repro2021_' + str(year) + '_00'
                       + str(doy) + '.tar.gz')  # link do arquivo desejado para baixar doy 1 - 9
            print(url)  # exibir o link no console
            # nome do aquivo doy 1 - 9
            name = 'ionPrf_repro2021_' + str(year) + '_00'
            # requisição de download
            urllib.request.urlretrieve(url, name + str(doy) + '.gz')
            # obtendo infomações sobre o tipo do arquivo
            # r = requests.get(url, allow_redirects=True)
            # print(r.headers.get('content-type'))  # exibindo tipo do arquivo no console
            with gzip.open('ionPrf_repro2021_' + str(year) + '_00' + str(doy) + '.gz', 'rb') as f_in:  # doy 1 - 9
                with open('ionPrf_repro2021_' + str(year) + '_00' + str(doy) + '.tar', 'wb') as f_out:  # doy 1 - 9
                    shutil.copyfileobj(f_in, f_out)
    
            file_path = root_path + 'ionPrf_repro2021_' + \
                str(year) + '_00' + str(doy) + '.gz'  # doy 1 - 9
            os.remove(file_path)
            file = tarfile.open('ionPrf_repro2021_' + str(year) +
                                '_00' + str(doy) + '.tar')  # doy 1 - 9
            file.extractall('./data/' + str(year) + '_' + f'{doy:03}')
            file.close()
    
        if doy in range(10, 100):
    
            url = str('https://data.cosmic.ucar.edu/gnss-ro/cosmic1/repro2021/level2/' + str(year) + '/0' + str(doy) +
                       '/ionPrf_repro2021_' + str(year) + '_0' + str(doy) + '.tar.gz')  # link do arquivo desejado para baixar doy 10 - 99
            print(url)  # exibir o link no console
            # nome do aquivo doy 10 - 99
            name = 'ionPrf_repro2021_' + str(year) + '_0'
            # requisição de download
            urllib.request.urlretrieve(url, name + str(doy) + '.gz')
            # obtendo infomações sobre o tipo do arquivo
            # r = requests.get(url, allow_redirects=True)
            # print(r.headers.get('content-type'))  # exibindo tipo do arquivo no console
    
            with gzip.open('ionPrf_repro2021_' + str(year) + '_0' + str(doy) + '.gz', 'rb') as f_in:  # doy 10 - 99
                with open('ionPrf_repro2021_' + str(year) + '_0' + str(doy) + '.tar', 'wb') as f_out:  # doy 10 - 99
                    shutil.copyfileobj(f_in, f_out)
    
            file_path = root_path + 'ionPrf_repro2021_' + \
                str(year) + '_0' + str(doy) + '.gz'  # doy 10 - 99
            os.remove(file_path)
            file = tarfile.open('ionPrf_repro2021_' + str(year) +
                                '_0' + str(doy) + '.tar')  # doy 10 - 99
            file.extractall('./data/' + str(year) + '_' + f'{doy:03}')
            file.close()
    
        if doy in range(100, 367):
    
            url = str('https://data.cosmic.ucar.edu/gnss-ro/cosmic1/repro2021/level2/' + str(year) + '/' + str(doy) +
                       '/ionPrf_repro2021_' + str(year) + '_' + str(doy) + '.tar.gz')  # link do arquivo desejado para baixar doy 100 - 366
            print(url)  # exibir o link no console
            # nome do aquivo doy 100 - 366
            name = 'ionPrf_repro2021_' + str(year) + '_'
            # requisição de download
            urllib.request.urlretrieve(url, name + str(doy) + '.gz')
            # obtendo infomações sobre o tipo do arquivo
            # r = requests.get(url, allow_redirects=True)
            # print(r.headers.get('content-type'))  # exibindo tipo do arquivo no console
    
            with gzip.open('ionPrf_repro2021_' + str(year) + '_' + str(doy) + '.gz', 'rb') as f_in:  # doy 100 - 366
                with open('ionPrf_repro2021_' + str(year) + '_' + str(doy) + '.tar', 'wb') as f_out:  # doy 100 - 366
                    shutil.copyfileobj(f_in, f_out)
    
            file_path = root_path + 'ionPrf_repro2021_' + \
                str(year) + '_' + str(doy) + '.gz'  # doy 100 - 366
            os.remove(file_path)
            file = tarfile.open('ionPrf_repro2021_' + str(year) +
                                '_' + str(doy) + '.tar')  # doy 100 - 366
            file.extractall('./data/' + str(year) + '_' + f'{doy:03}')
            file.close()

get_data(root_path, 2015, 1, 5)