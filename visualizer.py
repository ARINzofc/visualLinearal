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
    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid()
    plt.show()









