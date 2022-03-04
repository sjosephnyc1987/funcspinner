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


#must take the independent variable as the first argument.

def test(x,*args):
    #need at least one argument
    if len(args)>=0:
        a=list(args)[1]
        print(a)
        return a*x

def simplelinear(x,a,b): return a+(b*x)
def quadratic(x,a,b,c): return a+(b*x)+c*(x**2)
def cubic(x,a,b,c,d): return a+(b*x)+(c*(x**2))+(d*(x**3))
def polyratio11(x,a,b,c): return (a+(b*x))/(1+(c*x))
def polyratio22(x,a,b,c,d,e): return (a+(b*x)+(c*(x**2)))/(1+(d*x)+(e*(x**2)))
def polyratio33(x,a,b,c,d,e,f,g): return (a+(b*x)+c*(x**2)+d*(x**3))/(1+(e*x)+f*(x**2)+g*(x**3))
def polyratio44(x,a,b,c,d,e,f,g,h,i): return (a+(b*x)+c*(x**2)+d*(x**3)+e*(x**4)) / (1+(f*x)+g*(x**2)+h*(x**3)+i*(x**4))
def michaelismenten(x,a,b): return (a*x)/(b+x)
def reciprocal(x,a,b): return 1/(a+b*x)
def bleasdalenelder(x,a,b,c): return ((a+(b*x))**(-1/c))
def farazdaghiharris(x,a,b,c): return 1/(a+b*(x**c))
def holliday(x,a,b,c): return 1/(a+(b*x)+(c*(x**2)))
def exponential(x,a,b): return np.exp(a*(x-b))
def monomolecular(x,a,b,c): return a*(1-np.exp(-b*(x-c)))
def threeparameterlogistic(x,a,b,c): return a/(1+b*(np.exp(-c*x)))
def fourparameterlogistic(x,a,b,c,d): return (d+(a-d))/(1+b*(np.exp(-c*x)))
def gompertz(x,a,b,c): return a*(np.exp(-np.exp(-b*(x-c))))
def weibull(x,a,b,c,d): return a-(a-b)*np.exp(- (c*np.absolute(x))**d)
def morganmercerfloding(x,a,b,c,d): return (a-(a-b))  / (1+(c*np.absolute(x))**d)
def richards(x,a,b,c,d): return a*(1+(b-1)*np.exp(-c*(x-d)))**(1/(1-b))
def logarithmic(x,a,b): return b*(np.log(np.absolute(x)-a))
def power(x,a,b): return a*(1-(b**x))
def powertopower(x,a,b,c): return a*(x**(b*(x**c)))
def sumexponentials(x,a,b,c,d): return a*(np.exp(-b*x))+c*(np.exp(-d*x))
def exponential1(x,a,b,c): return a*(x**b)*np.exp(-c*x)
def exponential2(x,a,b,c,d): return (a+b*x)*np.exp(-c*x)+d
def normal(x,a,b,c,d): return a+b*(np.exp(-c*(x-d)**2))
def lognormal(x,a,b,c,d): return a+(b/x)*np.exp(-c*(np.log(np.absolute(x))-d)**2)
def exponentialVariation(x,a,b): return a*np.exp(-b*x)
def michaelismenten2(x,a,b,c,d): return (a*x/(b+x)) + (c*x/(d+x))
def michaelismenten3(x,a,b,c,d,e,f): return a*x/(b+x) + c*x/(d+x)+ e*x/(f+x)
def linearlinear(x,a,b,c,d): return a + (b*x) + (c*(x-d)*np.sign(x-d))
def linearquadratic(x,a,b,c,d,e): return a+(b*x)+c*(x**2)+(x-d)*np.sign((x-d)*[c*(x+d)+e])
def quadraticlinear(x,a,b,c,d,e,f): return a+(b*x)+(c*(x**2))+((x-d)*np.sign(x-d)*[e*(x+d)+f])
def quadraticquadratic(x,a,b,c,d,e,f): return a+(b*x)+c*(x**2)+(x-d)*np.sign(x-d)*[e*(x+d)+f]
def linear3(x,a,b,c,d,e,f): return a+(b*x)+(c*(x-d)*np.sign(x-d))+(e*(x-f)*np.sign(x-f))
def gompertz2(x,a,b): return np.exp((a/b)*(1-np.exp(b*x)))
def hill2(x,a,b,c): return (a*(x**c))/((b**c)+(x**c))
def sum3exponentials(x,a,b,c,d,e,f): return a*(np.exp(-b*x))-c*(np.exp(-d*x))+e*(np.exp(-f*x))
def gaussian(x,a,b,c): return  a*np.exp(-np.power(x - b, 2)/(2*np.power(c, 2)))



def function_return(funcname):
    
        if funcname == "all":
            print ("we will be running thru all the functions")

        elif funcname == "simplelinear" :return simplelinear
        elif funcname == "test" :return test
        elif funcname == "quadratic" :return quadratic
        elif funcname == "cubic" :return cubic
        elif funcname == "polyratio11" :return polyratio11
        elif funcname == "polyratio22" :return polyratio22
        elif funcname == "polyratio33" :return polyratio33
        elif funcname == "polyratio44" :return polyratio44
        elif funcname == "michaelismenten" :return michaelismenten
        elif funcname == "reciprocal" :return reciprocal
        elif funcname == "bleasdalenelder" :return bleasdalenelder
        elif funcname == "farazdaghiharris" :return farazdaghiharris
        elif funcname == "holliday" :return holliday
        elif funcname == "exponential" :return exponential
        elif funcname == "monomolecular" :return monomolecular
        elif funcname == "threeparameterlogistic" :return threeparameterlogistic
        elif funcname == "fourparameterlogistic" :return fourparameterlogistic
        elif funcname == "gompertz" :return gompertz
        elif funcname == "weibull" :return weibull
        elif funcname == "morganmercerfloding" :return morganmercerfloding
        elif funcname == "richards" :return richards
        elif funcname == "logarithmic" :return logarithmic
        elif funcname == "power" :return power
        elif funcname == "powertopower" :return powertopower
        elif funcname == "sumexponentials" :return sumexponentials
        elif funcname == "exponential1" :return exponential1
        elif funcname == "exponential2" :return exponential2
        elif funcname == "normal" :return normal
        elif funcname == "lognormal" :return lognormal
        elif funcname == "exponentialvariation" :return exponentialVariation
        elif funcname == "michaelismenten2" :return michaelismenten2
        elif funcname == "michaelismenten3" :return michaelismenten3
        elif funcname == "linearlinear" :return linearlinear
        elif funcname == "linearquadratic" :return linearquadratic
        elif funcname == "quadraticlinear" :return quadraticlinear
        elif funcname == "quadraticquadratic" :return quadraticquadratic
        elif funcname == "linear3" :return linear3
        elif funcname == "gompertz2" :return gompertz2
        elif funcname == "hill2" :return hill2
        elif funcname == "sum3exponentials" :return sum3exponentials
        elif funcname == "gaussian" :return gaussian



        
# import inspect
# ee = inspect.getsource(funky)
# print(eel)
# eel = inspect.getsource(funky("simplelinear"))
# print(eel)


