#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:36:41 2022

@author: stephenjoseph

tester function for the function_return_all function of funspinner
that runs data thru ALL the models in funcspinner and calculates the standard error, 
R-squared etc

"""


from pandas import read_csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import Git_PythonCodeSamples.funcspinner.funcspinner as funcspinner

# read in data and convert to 2D numpy array
#url = 'https://raw.githubusercontent.com/shenge86/pythonhelpers/master/longley.csv'
url = 'https://raw.githubusercontent.com/sjosephnyc1987/datasets/main/TradingEconimicsWorldDataMarch2022.csv'
df = read_csv(url)


data = df.values

pdf = df[['Inflation rate','Jobless rate']]
xx = np.array(pdf['Inflation rate'])
yy = np.array(pdf['Jobless rate'])


plt.figure(0)

# plot input vs output
plt.scatter(xx, yy, label='Raw Data')
plt.xlabel("Inflation Rate")
plt.ylabel('Jobless Rate')
plt.legend(loc='lower right')




##----------- all curve fit ---------
print("\n-----------------")
print("<------ CURVE FITTING ALL MATRIX ------>\n")

listoffuncs = funcspinner.function_return_all("all")

results_matrix = pd.DataFrame(columns=['function_name', 'model_error', 'sj_error'])


for key, value in listoffuncs.items():
    
    print("\n----- ", key, " ------")
    
    try:
        fit_params_all, covariances_all = curve_fit(value, xx, yy ,maxfev=500000)
    except TypeError as tpe:
        print(tpe)
        continue
    
    
    model_error = np.linalg.norm(value(np.array(xx),*fit_params_all))
    sj_model_error = np.linalg.norm(covariances_all)                             
    
    # print(' model error:', key, " - " ,np.linalg.norm(value(np.array(x),*fit_params_all)) )
    # print(' SJ model error: ', np.linalg.norm(covariances_all))

    print("--- ", key, " -model error = ", model_error, " -sj_model_error = ", sj_model_error) 
    print("               ********************             \n")

    results_matrix = results_matrix.append({'function_name':key , 'model_error': model_error, 'sj_error': sj_model_error}, ignore_index=True)


# #get the function from the funcspinner class.
# objective_function = funcspinner.function_return(functionname)



# #to see what's in the function returned
# import inspect
# print(inspect.getsource(objective_function))



# #for printing out the results.
# coeffs = ["a","b","c","d","e","f","g","h","i","j","k"]

# # do linear fit
# fit_paramsL, covariances = curve_fit(objective_function, xx, yy, maxfev=500000)



# print ("Fitting curve using the", functionname, "function")
# print ("-----------------")
# print('Parameter values: ')

# i=0
# for coeff in fit_paramsL:
#     print(coeffs[i], "=" , coeff)
#     i = i+1


# x_monotonic = np.arange(min(xx),max(xx),1)
# y_fit = objective_function(x_monotonic,*fit_paramsL)



#to calulate the standard error
#---------------------------------
#x_expected = np.linspace(min(x),max(x),len(x))

#you can get standard error of individual variables using np.sqrt(np.diag(covariances)) 

# y_expected = objective_function(np.array(xx),*fit_paramsL)

# residuals = yy - y_expected
# squaresumofresiduals = np.sum(residuals**2)
# std_error = np.sqrt(squaresumofresiduals/len(y_expected))
# print("standard error = ", str(std_error))


# #to calculate R-square
# #standarddevparams2 = np.sqrt(np.diag(covariances))
# squaresum = np.sum((yy-np.mean(yy))**2)
# R2 = 1 - (squaresumofresiduals/squaresum)
# print("R-square = ",  R2)

# plt.plot(x_monotonic,y_fit,'--',color='red',label='model fit')
# plt.legend(loc='lower right')
# title = "plotting raw data using the " + functionname + " model"
# plt.title(title)


#testing =====================
#==============

# print("\n\n******** enter testing mode ************")
# pdf2 = pdf[pdf['Inflation rate'] > 2]

# print("length of new dataset = " , len(pdf2))
# x_test = np.array(pdf2['Inflation rate'])
# y_test = np.array(pdf2['Jobless rate'])

# fit_params_test, covariance_test = curve_fit(objective_function, x_test, y_test, maxfev=500000)


# i=0
# for coeff in fit_params_test:
#     print(coeffs[i], "=" , coeff)
#     i = i+1


# x_monotonic_test = np.arange(min(x_test),max(x_test),1)
# y_fit_test = objective_function(x_monotonic_test,*fit_params_test)


# #to calulate the standard error in testing mode
# #----------------------------------------------------

# #you can get standard error of individual variables using np.sqrt(np.diag(covariances)) 

# y_expected_test = objective_function(np.array(x_test),*fit_params_test)

# residuals_test = y_test - y_expected_test
# squaresumofresiduals_test = np.sum(residuals_test**2)
# std_error_test = np.sqrt(squaresumofresiduals_test/len(y_expected_test))
# print("standard error test mode= ", str(std_error_test))


# #to calculate R-square
# #standarddevparams2_test = np.sqrt(np.diag(covariance_test))
# squaresum_test = np.sum((y_test-np.mean(y_test))**2)
# R2 = 1 - (squaresumofresiduals_test/squaresum_test)
# print("R-square test mode= ",  R2)

# print("\n\n\n\n")


#====== end testing =====================
#====================



#axs[0].savefig('populationvsemployed_linearfit.png')



#print(' model error: ', np.linalg.norm(objective_function(np.array(x),*fit_paramsL)))
#print(' SJ model error: ', np.linalg.norm(covariances))


