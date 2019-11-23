# Assignment_02 : Shortest distance from a point to a line
# Author: Mahmoud Abdel Mohsen

# Import useless Libraries
import sympy as sp
import math
# from sympy import Abs, div, add
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# mpl.use('Qt5Agg')
mpl.use('MacOSX')
plt.show()
# Go Dark
plt.style.use('dark_background')

mpl.rcParams['figure.facecolor'] = '#141414'
mpl.rcParams['axes.facecolor'] = '#141414'
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False


# define Symbols
# a, a1, a2, at, b, d, x, x0, x1, x2, x10, x20 = sp.symbols('a, a_1, a_2, a^t, b, d, x, x^0, x_1, x_2, x_1^0, x_2^0')

# Define line equation: based on h(x)= a0 + a1x1 + a2x2 = 0
# Define point X0 = (x01,x02)

# declare Line variables
a0 = 5
a1 = 3
a2 = 4
a = np.array([a1, a2])
at = a[:, np.newaxis]  # Transpose in numpy dose not work on 1D
x1 = np.linspace(-5, 5, 50)
x2 = []
# declare point variables
x01 = 1
x02 = 2


# line function
def ln(a0, a1, a2, x1):
    for i in x1:
        x2t = (-a0 - (a1 * i)) / a2
        x2.append(x2t)
    return (x2)


# point Function :

def pn(x01, x02):
    x0 = np.array([x01, x02])
    return x0


# call line Function to get x2
ln(4, 3, 5, x1)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(x1, x2)
ax.plot(x01, x02, marker='o')


# Define Equation
# x = sp.symbols('x')
# print (type(x))
# sp.pprint(x)
