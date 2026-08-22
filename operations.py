import numpy as a
def vector_addition(a,b):
    return a+b
def vector_subtract(a,b):
    return a-b
def vector_multiple(a,b):
    return a*b
def vector_mag(v):
    c=a.linalg.norm(v)
    return c
def vector_dot(c,b):
    c=a.dot(c,b)
    return c
def matrix_tranform(t,y):
    c=a.linalg.matmul(t,y)
    return c
def square(r,p):
    tranformed=(r@p.T).T
    return tranformed
