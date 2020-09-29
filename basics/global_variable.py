# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 20:48:18 2018

@author: Ashusan
"""

x="glbal"

def foo():
        print("x inside:", x)

foo()
print("x outside:", x)

x="glbal"

def foo():
        x=x*2
        print(x)


foo()


x="glb"

def foo():
    global y
    y="lcl"
    print(x)
    
    
foo()

print(y)



x = 5

def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x)


def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()

x = 5

def foo():
    y = "local"
    global x
    x = x * 2
    print(x)
    print(y)
    
foo()