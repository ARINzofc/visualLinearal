import numpy as a
from operations import vector_addition,vector_subtract,vector_multiple,vector_mag,vector_dot,matrix_tranform,square
from visualizer import vector_draw,matrix_draw,draw_vector
print("Linear Algebra Visualizer")
print("1. Vector Addition")
print("2. Matrix Transformation")
print("3. Exit")
Enter=int(input("enter your choice: "))
if(Enter==1):
    A=int(input("enter the vector for A:"))
    A2=int(input("enter the vector for A:"))
    B=int(input("enter the vector for B:"))
    B2=int(input("enter the vector for B:"))
    n=a.array([A,A2])
    p=a.array([B,B2])
    result=vector_addition(n,p)
    print("Addition",vector_addition(n,p))
    print("subtractions",vector_subtract(n,p))
    print("multiple",vector_multiple(n,p))
    print("Magnitude",vector_mag(n))
    print("Dot product",vector_dot(n,p))
    vector_draw(n,p,result)
elif(Enter==2):
    r1a=int(input("Enter matrix row 1: "))
    r2a=int(input("Enter matrix row 1: "))
    r1b=int(input("Enter matrix row 2: "))
    r2b=int(input("Enter matrix row 2: "))
    v1=int(input("Enter the vector x: "))
    v2=int(input("Enter the vector y: "))
    d=a.array([[r1a,r2a],[r1b,r2b]])
    v=a.array([v1,v2])
    s=a.array([[0,0],[1,0],[1,1],[0,1]])
    matmul=matrix_tranform(d,v)
    print("Transformed: ",square(d,s))
    matrix_draw(v,matmul)
else:
    exit
    











