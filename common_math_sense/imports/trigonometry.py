from math import *
from decimal import getcontext

getcontext().prec = 1000

def sine(angle):
    print(sin(angle))

def cosine(angle):
    print(cos(angle))

def tangent(angle):
    print(tan(angle))

def hyperbolic_sine(angle):
    print(sinh(angle))

def hyperbolic_cosine(angle):
    print(cosh(angle))

def hyperbolic_tangent(angle):
    print(tanh(angle))

def inverse_sine(angle):
    print(asin(angle))

def inverse_cosine(angle):
    print(acos(angle))

def inverse_tangent(angle):
    print(atan(angle))

def inverse_hyperbolic_sine(angle):
    print(asinh(angle))

def inverse_hyperbolic_cosine(angle):
    print(acosh(angle))

def inverse_hyperbolic_tangent(angle):
    print(atanh(angle))