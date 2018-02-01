import numpy as np

nx, ny = (3, 2)
print nx, ny

x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)

xv, yv = np.meshgrid(x, y)
print x, y
print xv
print yv
