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

#the following are the functions that will be returned when their name is called in function_return method.

def simpleLinear(x,a,b): return a+(b*x)
def test (x):return x
def quadratic(x,a,b,c): return a+(b*x)+c*(x**2)
def cubic(x,a,b,c,d): return a+(b*x)+(c*(x**2))+(d*(x**3))
def saturationGrowthRate(x,a,b):return a*(x/(b+x))  #from chapra
def simpleExponential(x,a,b):return a*np.exp(b*x) #from chapra
def simplePower(x,a,b):return a*(x**b) #from chapra
def polyRatio11(x,a,b,c): return (a+(b*x))/(1+(c*x))
def polyRatio22(x,a,b,c,d,e): return (a+(b*x)+(c*(x**2)))/(1+(d*x)+(e*(x**2)))
def polyRatio33(x,a,b,c,d,e,f,g): return (a+(b*x)+c*(x**2)+d*(x**3))/(1+(e*x)+f*(x**2)+g*(x**3))
def polyRatio44(x,a,b,c,d,e,f,g,h,i): return (a+(b*x)+c*(x**2)+d*(x**3)+e*(x**4)) / (1+(f*x)+g*(x**2)+h*(x**3)+i*(x**4))
def michaelisMenten(x,a,b): return (a*x)/(b+x)
def reciprocal(x,a,b): return 1/(a+b*x)
def bleasdaleNelder(x,a,b,c): return ((a+(b*x))**(-1/c))
def farazdaghiHarris(x,a,b,c): return 1/(a+b*(x**c))
def holliday(x,a,b,c): return 1/(a+(b*x)+(c*(x**2)))
def exponential(x,a,b): return np.exp(a*(x-b))
def threeParameterLogistic(x,a,b,c): return a/(1+b*(np.exp(-c*x)))
def gompertz(x,a,b,c): return a*(np.exp(-np.exp(-b*(x-c))))
def weibull(x,a,b,c,d): return a-(a-b)*np.exp(- (c*np.absolute(x))**d)
def richards(x,a,b,c,d): return a*(1+(b-1)*np.exp(-c*(x-d)))**(1/(1-b))
def logarithmic(x,a,b): return b*(np.log(np.absolute(x)-a)) #this fn > 2
def power(x,a,b): return a*(1-(b**x))
def powerToPower(x,a,b,c): return a*(x**(b*(x**c)))
def sumExponentials(x,a,b,c,d): return a*(np.exp(-b*x))+c*(np.exp(-d*x))
def exponential1(x,a,b,c): return a*(x**b)*np.exp(-c*x)
def exponential2(x,a,b,c,d): return (a+b*x)*np.exp(-c*x)+d
def normal(x,a,b,c,d): return a+b*(np.exp(-c*(x-d)**2))
def lognormal(x,a,b,c,d): return a+(b/x)*np.exp(-c*(np.log(np.absolute(x))-d)**2)
def exponentialVariation(x,a,b): return a*np.exp(-b*x)
def michaelisMenten2(x,a,b,c,d): return (a*x/(b+x)) + (c*x/(d+x))
def michaelisMenten3(x,a,b,c,d,e,f): return a*x/(b+x) + c*x/(d+x)+ e*x/(f+x)
def linearLinear(x,a,b,c,d): return a + (b*x) + (c*(x-d)*np.sign(x-d))
def linearQuadratic(x,a,b,c,d,e): return a+(b*x)+c*(x**2)+(x-d)*np.sign((x-d)*(c*(x+d)+e))
def quadraticLinear(x,a,b,c,d,e,f): return a+(b*x)+(c*(x**2))+((x-d)*np.sign(x-d)*(e*(x+d)+f))
def quadraticQuadratic(x,a,b,c,d,e,f): return a+(b*x)+c*(x**2)+(x-d)*np.sign(x-d)*(e*(x+d)+f)
def linear3(x,a,b,c,d,e,f): return a+(b*x)+(c*(x-d)*np.sign(x-d))+(e*(x-f)*np.sign(x-f))
def gompertz2(x,a,b): return np.exp((a/b)*(1-np.exp(b*x)))
def hill2(x,a,b,c): return (a*(x**c))/((b**c)+(x**c))
def sum3Exponentials(x,a,b,c,d,e,f): return a*(np.exp(-b*x))-c*(np.exp(-d*x))+e*(np.exp(-f*x))
def gaussian(x,a,b,c): return  a*np.exp(-np.power(x - b, 2)/(2*np.power(c, 2)))



#this function returns individual function based on the name passed. 
#to curve fit a matrix of mulitple models, use the function_return_all function.

def function_return(funcname):
    
        if funcname == "all":
            raise Exception('please use the all_function method')  
            

        elif funcname == "simpleLinear" :return simpleLinear
        elif funcname == "test" :return test
        elif funcname == "quadratic" :return quadratic
        elif funcname == "cubic" :return cubic
        elif funcname == "saturationGrowthRate" :return saturationGrowthRate #from Chapra
        elif funcname == "simpleExponential":return simpleExponential #form Chapra
        elif funcname == "simplePower":return simplePower #from Chapra
        elif funcname == "polyRatio11" :return polyRatio11
        elif funcname == "polyRatio22" :return polyRatio22
        elif funcname == "polyRatio33" :return polyRatio33
        elif funcname == "polyRatio44" :return polyRatio44
        elif funcname == "michaelisMenten" :return michaelisMenten
        elif funcname == "reciprocal" :return reciprocal
        elif funcname == "bleasdaleNelder" :return bleasdaleNelder #needs only positive values
        elif funcname == "farazdagiHarris" :return farazdaghiHarris #needs only positive values
        elif funcname == "holliday" :return holliday
        elif funcname == "exponential" :return exponential
        elif funcname == "threeParameterLogistic" :return threeParameterLogistic
        elif funcname == "gompertz" :return gompertz
        elif funcname == "weibull" :return weibull
        elif funcname == "richards" :return richards
        elif funcname == "logarithmic" :return logarithmic
        elif funcname == "power" :return power
        elif funcname == "powertopower" :return powerToPower
        elif funcname == "sumexponentials" :return sumExponentials
        elif funcname == "exponential1" :return exponential1
        elif funcname == "exponential2" :return exponential2
        elif funcname == "normal" :return normal
        elif funcname == "lognormal" :return lognormal
        elif funcname == "exponentialVariation" :return exponentialVariation
        elif funcname == "michaelisMenten2" :return michaelisMenten2
        elif funcname == "michaelisMenten3" :return michaelisMenten3
        elif funcname == "linearLinear" :return linearLinear
        elif funcname == "linearQuadratic" :return linearQuadratic
        elif funcname == "quadraticLinear" :return quadraticLinear
        elif funcname == "quadraticQuadratic" :return quadraticQuadratic
        elif funcname == "linear3" :return linear3
        elif funcname == "gompertz2" :return gompertz2
        elif funcname == "hill2" :return hill2
        elif funcname == "sum3Exponentials" :return sum3Exponentials
        elif funcname == "gaussian" :return gaussian
        else:
            raise Exception('function not found, please consult documentation here: \n https://github.com/sjosephnyc1987/funcspinner')
        

#this function returns a dictionary of all the curves cataloged in this module
#spin through them in a loop to get a matrix of results.

def function_return_all(funcname_all):
    
        if funcname_all == "all":
            
            return {'simpleLinear':simpleLinear ,'test':test,'quadratic':quadratic
                    ,'cubic':cubic,'saturationGrowthRate':saturationGrowthRate 
                    ,'simpleExponential':simpleExponential ,'simplePower':simplePower,'polyRatio22':polyRatio22
                    ,'polyRatio33':polyRatio33,'polyRatio44':polyRatio44,'michaelisMenten':michaelisMenten
                    ,'reciprocal':reciprocal,'bleasdaleNelder':bleasdaleNelder
                    ,'farazdagiHarris':farazdaghiHarris ,'holliday':holliday
                    ,'exponential':exponential ,'threeParameterLogistic':threeParameterLogistic
                    ,'gompertz':gompertz ,'weibull':weibull
                    ,'richards':richards ,'logarithmic':logarithmic ,'power':power ,'powertopower':powerToPower
                    ,'sumexponentials':sumExponentials ,'exponential1':exponential1,'exponential2':exponential2
                    ,'normal':normal ,'lognormal':lognormal ,'exponentialVariation':exponentialVariation
                    ,'michaelisMenten2':michaelisMenten2 ,'michaelisMenten3':michaelisMenten3
                    ,'linearLinear':linearLinear ,'linearQuadratic':linearQuadratic ,'quadraticLinear':quadraticLinear
                    ,'quadraticQuadratic':quadraticQuadratic ,'linear3':linear3
                    ,'gompertz2':gompertz2,'hill2':hill2,'sum3Exponentials':sum3Exponentials ,'gaussian':gaussian}
            
        #REMOVED  - need to be added back
        #'polyratio33':polyratio33 
        #'exponential':exponential 
        #'monomolecular':monomolecular 
        #'linearquadratic':linearquadratic ,
           
        else:
            raise Exception('this function only accepts the param all, you sent - ', str(funcname_all))


        
        


