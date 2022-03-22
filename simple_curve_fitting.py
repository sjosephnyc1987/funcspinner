#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:57:38 2022

@author: stephenjoseph

this bit of code, tests the funcspinner class to generate simple models of the function
being examined for curve fitting.





"""

from pandas import read_csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import Git_PythonCodeSamples.funcspinner.funcspinner as funcspinner


x_start = -10
x_end =10

x=np.linspace(x_start, x_end,100)


functionname = "polyRatio44"
print("\n---------BEGIN---------")

#get the function from the funcspinner class.
objective_function = funcspinner.function_return(functionname)

#to see what's in the function returned
import inspect
print(inspect.getsource(objective_function))





#do linear fit just to figure out how many params your function needs
#there are waaaay better ways to do this, but let's stick with this for 
#for lack of time.
fit_paramsL, covariances = curve_fit(objective_function, x, x, maxfev=500000)


print("params ", fit_paramsL)
print("covariances: \n ", covariances)

#print("-----debug-------")
#create an array for the params to be passed to the univariate model
fit_params_all1=[]

#addig all 1s depending on how may variables the model needs
for u in range(len(fit_paramsL)):
    fit_params_all1.append(1.2)

#creating the plot for the univariate model    
y = objective_function(x,*fit_params_all1) 

#
plt.axhline(0, color='pink')
plt.axvline(0, color='pink')
plt.plot(x,y,'--',color='green',label='univariate fit')
plt.legend(loc='lower right')


title = "univariate " + functionname + " model"
plt.title(title)



print("\n---------END---------\n\n\n")

#spinning thru numbers one by one

looped_y= []

for tt in x:
    y_temp_loop = objective_function(tt,*fit_paramsL)
    looped_y.append(y_temp_loop)

#print(looped_y)

