import numpy as a
from operations import vector_addition,vector_subtract,vector_multiple,vector_mag,vector_dot,matrix_tranform,square
from visualizer import vector_draw,matrix_draw
print("""
╔══════════════════════════════════════╗
║      NUMPY LINEAR ALGEBRA            ║
║           VISUALIZER                 ║
╚══════════════════════════════════════╝
""")
print("1. Vector Addition")
print("2. Matrix Transformation")
print("3. Exit")
Enter=int(input("enter your choice: "))
if(Enter==1):
    A=int(input("enter i compoment of A:"))
    A2=int(input("enter j component of A:"))
    B=int(input("enter i component of B:"))
    B2=int(input("enter j component of B:"))
    n=a.array([A,A2])
    p=a.array([B,B2])
    result=vector_addition(n,p)
    print("1. Addition")
    print("2. subtractions")
    print("3. multiple")
    print("4. Magnitude")
    print("5. Dot product")
    Enter=int(input("Enter the choice:"))
    if(Enter==1):
        print("Addition",vector_addition(n,p))
    elif(Enter==2):
        print("Subtraction",vector_subtract(n,p))
    elif(Enter==3):
        print("Multiple",vector_multiple(n,p))
    elif(Enter==4):
        print("Magnitude",vector_mag(n))
    elif(Enter==5):
        print("Dot product",vector_dot(n,p))   
    Enter2=str(input("do you want to visualize: "))
    if(Enter2.lower()=="yes"):                   
        vector_draw(n,p,result)
    else:
        exit    
elif(Enter==2):
    a = int(input("Enter row 1, column 1: "))
    b = int(input("Enter row 1, column 2: "))
    c = int(input("Enter row 2, column 1: "))
    d = int(input("Enter row 2, column 2: "))
    v1=int(input("Enter the vector i: "))
    v2=int(input("Enter the vector j: "))
    d=a.array([[a,b],[c,d]])
    v=a.array([v1,v2])
    s=a.array([[0,0],[1,0],[1,1],[0,1]])
    matmul=matrix_tranform(d,v)
    print("Transformed: ",square(d,s))
    matrix_draw(v,matmul)
else:
    exit
    






