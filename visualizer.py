import numpy as p
import matplotlib.pyplot as plt
def vector_draw(a,b,c):
    plt.quiver(0,0,a[0],a[1], angles="xy", scale_units="xy", scale=1)
    plt.quiver(0,0,b[0],b[1], angles="xy", scale_units="xy", scale=1)
    plt.quiver(a[0],a[1],c[0],c[1], angles="xy", scale_units="xy", scale=1)
    plt.quiver(b[0],b[1],a[0],a[1], angles="xy", scale_units="xy", scale=1)
    plt.axhline(0)
    plt.axvline(0)
    plt.xlim(-8,8)
    plt.ylim(-8,8)
    plt.grid()
    plt.show()




