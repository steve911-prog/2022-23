from math import *

def s_rectangle(a,b):
    result = a*b
    print(result,"cm")
    return result

def s_triangle_geron(a,b,c):
    p = a+b+c
    result = sqrt(p*(p-a)*(p-b)*(p-c))
    print(result,"cm")
    return result

def s_triangle_h(a,h):
    result = 0.5*a*h
    print(result,"cm")
    return result  

def s_quadrat(a):
    result = a**2
    print(result,"cm")
    return result



p = input("do you want to go? :) ")
