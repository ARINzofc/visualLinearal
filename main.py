import numpy as a
from operations import vector_addition,vector_subtract,vector_multiple,vector_mag,vector_dot
from visualizer import vector_draw
print("Linear Algebra Visualizer")


n=a.array([1,2])
p=a.array([3,-5])
d=a.dot(n,p)
result=vector_addition(n,p)
print("Addition",vector_addition(n,p))
print("subtractions",vector_subtract(n,p))
print("multiple",vector_multiple(n,p))
print("Magnitude",vector_mag(n))
print("Dot product",vector_dot(n,p))
vector_draw(n,p,result)




