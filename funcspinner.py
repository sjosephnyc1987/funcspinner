#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:46:12 2022

Funcspinner is a library of curve fitting functions that can be used as the objective
function when a curve is being fit.

Check Medium please

@author: stephenjoseph
"""


import numpy as np

def funky(funcname):
    
        if funcname == "all":
            print ("we will be running thru all the functions")

        elif funcname ==  "simplelinear": 
            return simplelinear
        elif funcname ==  "quadratic": return quadratic
        elif funcname ==  "cubic" :return cubic
        elif funcname ==  "polyratio11" :return polyratio11
        elif funcname ==  "polyratio22" :return polyratio22
        elif funcname ==  "polyratio33" :return polyratio33
        elif funcname ==  "polyratio44" :return polyratio44
        elif funcname ==  "michaelismenten" :return michaelismenten
        elif funcname ==  "reciprocal" :return reciprocal
        elif funcname ==  "bleasdalenelder" :return bleasdalenelder
        elif funcname ==  "farazdaghiandharris" :return farazdaghiandharris
        elif funcname ==  "holliday" :return holliday
        elif funcname ==  "exponential" :return exponential
        elif funcname ==  "monomolecular" :return monomolecular
        elif funcname ==  "threeparameterlogistic" :return threeparameterlogistic
        elif funcname ==  "fourparameterlogistic" :return fourparameterlogistic
        elif funcname ==  "gompertz" :return gompertz
        elif funcname ==  "weibull" :return weibull
        elif funcname ==  "morganmercerfloding" :return morganmercerfloding
        elif funcname ==  "richards" :return richards
        elif funcname ==  "logarithmic" :return logarithmic
        elif funcname ==  "power" :return power
        elif funcname ==  "powertopower" :return powertopower
        elif funcname ==  "sumofexponentials" :return sumofexponentials
        elif funcname ==  "exponentialtype1" :return exponentialtype1
        elif funcname ==  "exponentialtype2" :return exponentialtype2
        elif funcname ==  "normal" :return normal
        elif funcname ==  "lognormal" :return lognormal
        elif funcname ==  "exponential" :return exponential
        elif funcname ==  "michaelismenten2" :return michaelismenten2
        elif funcname ==  "michaelismenten3" :return michaelismenten3
        elif funcname ==  "linearlinear" :return linearlinear
        elif funcname ==  "linearquadratic" :return linearquadratic
        elif funcname ==  "quadraticlinear" :return quadraticlinear
        elif funcname ==  "quadraticquadratic" :return quadraticquadratic
        elif funcname ==  "linearlinearlinear" :return linearlinearlinear
        elif funcname ==  "gompertz2" :return gompertz2
        elif funcname ==  "hill2" :return hill2
        elif funcname ==  "sumof3exponentials" :return sumof3exponentials
        elif funcname ==  "gaussian" :return gaussian

#must take the independent variable as the first argument.

def simplelinear(x,a,b): return (a*x)+b

def quadratic(x,a,b,c): return a + (b*x) + c*(x**2)

def cubic(x,a,b,c,d): return a+(b*x)+(c*(x**2))+(d*(x**3))

def polyratio11(): return ((A+B*X)/(1+C*X))

def polyratio22(): return (A+(B*X)+(C*(X**2)))/(1+(D*X)+(E(X**2)))

def exponential(x,a,b):return np.exp(a*(x-b))
    


# import inspect
# ee = inspect.getsource(funky)
# print(eel)
# eel = inspect.getsource(funky("simplelinear"))
# print(eel)


