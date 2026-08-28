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
def unit_vector(v):
    magnitude=a.linalg.norm(v)
    if a.close(magnitude,0):
        print("Error")
        return None
    else:    
        return v/magnitude
def projection(v,p):
    magnitude=a.linalg.norm(p)
    if a.isclose(magnitude,0):
        print("Error: Cannot project onto a zero vector")
        return None
    else:
        projection=(a.dot(v,p)/a.dot(p,p))*p
    return projection
def linear_combination(v,p,alpha,beta):
    return alpha*v+beta*p
def linear_independece(v,k):
    if(a.linalg.det(v,k)==0):
        return "linearly dependent"
    else:
        return "linearly independent"
