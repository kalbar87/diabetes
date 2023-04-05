# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:30:25 2023

@author: michalk
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats



def distribution_plot(feature):
    sk = feature.skew()
    kurt = feature.kurtosis()
    fig, axd = plt.subplot_mosaic([['upper left', 'right'],
                                   ['lower left', 'right']], figsize=(14,12))

    #Histogram
    sns.histplot(feature, ax=axd['upper left'], stat='density', kde='False', color='skyblue')
    sns.kdeplot(feature, color='blue', ax=axd['upper left'], label='KDE')
    axd['upper left'].axvline(x = feature.mean(), c='red', linewidth=1.5, label = 'mean')
    axd['upper left'].axvline(x = feature.median(), c='green', linewidth=1.5, label = 'median')
    axd['upper left'].legend()
    
    #Pobability plot
    stats.probplot(feature, plot=axd['lower left'])
    value = [sk, kurt]
    lbl = ['Skew', 'Kurtosis']
    
    [axd['lower left'].text(0.03,0.9-0.1*x,'%s = %.2f' %(lbl[x],y) ,
                           fontsize=18, transform=axd['lower left'].transAxes, 
                           bbox=dict(facecolor='skyblue', alpha=.3)) for x,y in enumerate(value)]

    #Box plot
    medianprops = dict(linewidth=3, linestyle='-', color='crimson')
    boxprops = dict(linestyle='-', linewidth=1.5, color='darkblue')
    capprops = dict(color='darkblue')
    whiskerprops = dict(color='darkblue')

    xs = np.random.normal(1,0.04, feature.shape[0])
    axd['right'].scatter(xs, feature, c='skyblue', alpha=.5)
    axd['right'].boxplot(feature, medianprops=medianprops, boxprops=boxprops, capprops=capprops, whiskerprops=whiskerprops)
    axd['right'].set_xlabel(feature.name)

