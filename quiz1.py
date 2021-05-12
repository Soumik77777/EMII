import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def Psi(x, y):
    return (np.sin(x) + np.cos(x)) * (np.sin(y) + np.cos(y))

x = np.linspace(0, 7, 50)
y = np.linspace(0, 7, 50)
X, Y = np.meshgrid(x, y)

Field = Psi(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Field)
plt.show()
