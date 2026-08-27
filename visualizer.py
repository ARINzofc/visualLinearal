import numpy as p
import matplotlib.pyplot as plt
def vector_draw(a,b,c):
    combine = p.concatenate((a, b, c))
    limit=p.max(p.abs(combine))+5
    plt.quiver(0,0,a[0],a[1], angles="xy", scale_units="xy", scale=1,color="blue")
    plt.quiver(0,0,b[0],b[1], angles="xy", scale_units="xy", scale=1,color="green")
    plt.quiver(0,0,c[0],c[1], angles="xy", scale_units="xy", scale=1,color="red")

    plt.text(a[0],a[1] , "A")
    plt.text(b[0],b[1] , "B")
    plt.text(c[0],c[1] , "A+B")
    plt.axhline(0)
    plt.axvline(0)
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    plt.grid()
    plt.show()
def matrix_draw(a,c):
    plt.title("Matrix Transformation")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    combine=p.concatenate((a,c))
    limit=p.max(p.abs(combine))+1
    
    plt.quiver(0,0,a[0],a[1], angles="xy", scale_units="xy", scale=1,color="blue")
    plt.quiver(0,0,c[0],c[1], angles="xy", scale_units="xy", scale=1,color="red")
    
    plt.text(a[0],a[1] , "original")
    plt.text(c[0],c[1] , "transformed")
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()
def eignvector(e):   
    v1=e[:, 0]
    v2=e[: ,1] 
    plt.title("Eignvector Transformation")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    combine=p.concatenate((v1,v2))
    limit=p.max(p.abs(combine))+1
    plt.quiver(0,0,v1[0],v1[1], angles="xy", scale_units="xy", scale=1,color="blue")
    plt.quiver(0,0,v2[0],v2[1], angles="xy", scale_units="xy", scale=1,color="red")
    plt.text(v1[0],v1[1] , "Eigenvector 1")
    plt.text(v2[0],v2[1] , "Eigenvector 2")
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()
def vector_draw2(a,b,c):
    combine = p.concatenate((a, b, c))
    limit=p.max(p.abs(combine))+5
    plt.quiver(0,0,a[0],a[1], angles="xy", scale_units="xy", scale=1,color="blue")
    plt.quiver(0,0,b[0],b[1], angles="xy", scale_units="xy", scale=1,color="green")
    plt.quiver(0,0,c[0],c[1], angles="xy", scale_units="xy", scale=1,color="red")

    plt.text(a[0],a[1] , "A")
    plt.text(b[0],b[1] , "B")
    plt.text(c[0],c[1] , "A-B")
    plt.axhline(0)
    plt.axvline(0)
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    plt.grid()
    plt.show()
def vector_draw3(a,b,c):
    combine = p.concatenate((a, b, c))
    limit=p.max(p.abs(combine))+5
    plt.quiver(0,0,a[0],a[1], angles="xy", scale_units="xy", scale=1,color="blue")
    plt.quiver(0,0,b[0],b[1], angles="xy", scale_units="xy", scale=1,color="green")
    plt.quiver(0,0,c[0],c[1], angles="xy", scale_units="xy", scale=1,color="red")

    plt.text(a[0],a[1] , "A")
    plt.text(b[0],b[1] , "B")
    plt.text(c[0],c[1] , "A*B")
    plt.axhline(0)
    plt.axvline(0)
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    plt.grid()
    plt.show()    
def vector_draw4(a,b,c):
    combine = p.concatenate((a, b, c))
    limit=p.max(p.abs(combine))+5
    plt.quiver(0,0,a[0],a[1], angles="xy", scale_units="xy", scale=1,color="blue")
    plt.quiver(0,0,b[0],b[1], angles="xy", scale_units="xy", scale=1,color="green")
    plt.quiver(0,0,c[0],c[1], angles="xy", scale_units="xy", scale=1,color="red")

    plt.text(a[0],a[1] , "A")
    plt.text(b[0],b[1] , "B")
    plt.text(c[0],c[1] , "A.B")
    plt.axhline(0)
    plt.axvline(0)
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    plt.grid()
    plt.show() 
def vector_draw5(a,b,c):
    combine = p.concatenate((a, b, c))
    limit=p.max(p.abs(combine))+5
    plt.quiver(0,0,a[0],a[1], angles="xy", scale_units="xy", scale=1,color="blue")
    plt.quiver(0,0,b[0],b[1], angles="xy", scale_units="xy", scale=1,color="green")
    plt.quiver(0,0,c[0],c[1], angles="xy", scale_units="xy", scale=1,color="red")

    plt.text(a[0],a[1] , "A")
    plt.text(b[0],b[1] , "B")
    plt.text(c[0],c[1] , "A on B")
    plt.axhline(0)
    plt.axvline(0)
    plt.xlim(-limit,limit)
    plt.ylim(-limit,limit)
    plt.grid()
    plt.show()














