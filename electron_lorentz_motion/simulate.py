import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D  # noqa

# I putted realistic values.....
e = 1.602e-19       # electron charge [C]
m = 9.11e-31        # electron mass [kg]
B = np.array([0.0, 0.0, 0.05])   #magnetic flux density [T]
E = np.array([0.0, 100.0, 0.0])  # electron field[V/m]

r = np.array([0.0, 0.0, 0.0])        # coordinate [m]
v = np.array([1e5, 1e5, 1e5])        # velosity [m/s]

dt =1e-11
steps = 1000

frames = []

#　　　　 
for i in range(steps):
    
    a = (-e / m) * (E + np.cross(v, B)) # Lorentz's law

    
    v += a * dt
    r += v * dt

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter(r[0], r[1], r[2], s=20, color="blue")

    lim = 5e-3
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)

    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.set_zlabel("z [m]")
    ax.view_init(elev=10,azim=90)

    plt.tight_layout()
    fname = f"{i}.png"
    plt.savefig(fname)
    plt.close()
    frames.append(Image.open(fname))


