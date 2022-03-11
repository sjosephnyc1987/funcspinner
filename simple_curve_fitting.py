#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:57:38 2022

@author: stephenjoseph

this bit of code, tests the funcspinner class to generate simple models of the 



"""





#create an array for the params to be passed to the univariate model
fit_params_all1=[]

#addig all 1s depending on how may variables the model needs
for u in range(len(fit_paramsL)):
    fit_params_all1.append(1.2)

#creating the plot for the univariate model    
z_fit = objective_function(x_monotonic,*fit_params_all1) 




plt.figure(1)

plt.plot(x_monotonic,z_fit,'--',color='green',label='univariate fit')
plt.legend(loc='lower right')
title = "univariate " + functionname + " model"
plt.title(title)

-------end univariate model
