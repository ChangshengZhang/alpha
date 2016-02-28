#!/usr/bin/python
# -*- coding: utf-8 -*-
# File Name: performamce.py
# Author: Changsheng Zhang
# mail: zhangcsxx@gmail.com
# Created Time: Sun Feb 28 13:55:31 2016

#########################################################################
import numpy as np

def calc_alpha_beta_sharpe(pnl_list,bench_list, rf_rate = 0.03):
    monthly_pnl = []
    for ii in range((len(pnl_list)- 1)/20):
        monthly_pnl.append(pnl_list[20*(ii+1)]/pnl_list[20*(ii)]- 1)
    mean = (np.mean(monthly_pnl)+1)**12 - 1
    std = np.std(monthly_pnl)*np.sqrt(12)
    
    sharpe = (mean- rf_rate)/std
    
    # annualized returns
    daily_return = []
    daily_bench_return = []
    for ii in range(len(pnl_list)-1):
        daily_return.append( (1+ pnl_list[ii+1]/pnl_list[ii])**250 - 1)
        daily_bench_return.append( (1+bench_list[ii+1]/bench_list[ii])**250 - 1)
    
    cov = 0
    for ii in range(len(daily_return)):
        cov = (daily_return - np.mean(daily_return))*(daily_bench_return - np.mean(daily_bench_return))
    cov = cov/(len(daily_return)-1)

    beta = cov/np.var(daily_bench_return)

    alpha = np.mean(daily_return)- rf_rate- beta*(np.mean(daily_bench_return)-rf_rate)

    return alpha, beta, sharpe


def calc_max_dropdown(pnl_list):
    max_dd = []
    for ii in range(len(pnl_list)):
        max_dd.append(1 - pnl_list[ii]/max(pnl_list[0:ii+1]))

    return max(max_dd)

def calc_annualized_return(pnl):
    return (1+pnl[-1]/pnl[0])**(250.0/(len(pnl)-1))- 1



