#!/usr/bin/python
# -*- coding: utf-8 -*-
# File Name: load_data.py
# Author: Changsheng Zhang
# mail: zhangcsxx@gmail.com
# Created Time: Sun Feb 28 13:20:29 2016

#########################################################################
import pandas as pd

def get_open_price():
    file_path = "raw_data/open.csv"
    open_price = pd.read_csv(file_path, index_col = 0)
    return open_price

def get_high_price():
    file_path = "raw_data/high.csv"
    high_price = pd.read_csv(file_path, index_col = 0)
    return high_price

def get_low_price():
    file_path = "raw_data/low.csv"
    low_price = pd.read_csv(file_path, index_col = 0)
    return low_price
def get_close_price():
    file_path = "raw_data/close.csv"
    close_price = pd.read_csv(file_path, index_col = 0)
    return close_price

def get_volume():
    file_path = "raw_data/volume.csv"
    volume = pd.read_csv(file_path, index_col = 0)
    return volume
