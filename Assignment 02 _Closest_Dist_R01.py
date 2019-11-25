# Assignment_02 : Shortest distance from a point to a line
# Author: Mahmoud Abdel Mohsen

# Import useless Libraries
import sympy as sp
import math
# from sympy import Abs, div, add
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Plot settings:

# General Settings:

# mpl.use('Qt5Agg') # Windows version
mpl.use('MacOSX')
plt.show()

# Go Dark
plt.style.use('dark_background')

mpl.rcParams['figure.facecolor'] = '#141414'
mpl.rcParams['axes.facecolor'] = '#141414'
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl. rcParams['text.usetex'] = True


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

# Declare point variables
x01 = 1
x02 = 2
x0 = np.array([x01, x02])

# Line function
def ln(a0, a1, a2, x1):
    for i in x1:
        x2t = (-a0 - (a1 * i)) / a2
        x2.append(x2t)
    return x2


# Point Function :

def pn(x01, x02):
    x0 = np.array([x01, x02])
    return x0


# Call line Function to get x2
ln(4, 3, 5, x1)

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(10, 7))
# Line Plot
ax.plot(x1, x2, label='$h(x)= a_0 + a_1x_1 + a_2x_2 = 0$')
# Point plot
ax.plot(x01, x02, marker='o')


# Plot settings
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.set_title('Linear optimisation (Shortest distance between line and a point)')
ax.set_xlabel('$(x_1)$', x=1, fontsize=14)
ax.set_ylabel('$(x_2)$', y=0, fontsize=14)
ax.legend(fontsize=14, frameon=False)


ax.annotate('$X^0 = (x^0_1,x^0_2)$', xy=(x01, x02), fontsize=14, xycoords="data", xytext=(2, 1.95), arrowprops=dict(arrowstyle="->"))

# Axis settings
ax.axis('equal')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(.25))

# Grid settings
ax.grid(color="grey", alpha=50, which="major", axis='x', linestyle='-', linewidth=0.25)
ax.grid(color="grey", alpha=50, which="major", axis='y', linestyle='-', linewidth=0.25)
ax.grid(color="grey", alpha=50, which="minor", axis='x', linestyle=':', linewidth=0.1)
ax.grid(color="grey", alpha=50, which="minor", axis='y', linestyle=':', linewidth=0.1)

# numerical solution
# Define distance equation (From Lecture 1, page 9)

d = np.divide(np.absolute(np.vdot(at, x0)+a0), np.sqrt(np.vdot(at, a)))

print(d)
# ax.annotate(xycoords="data", xytext=(2, 1.95),'$d = ((a^TX^0-b)/sqrt(a^ta$')
ax.text(-5, -2, "$d = \\frac{|a^TX^0-b|}{\sqrt{a^Ta}}=$ %f"%(d), fontsize=16)
# Symbolic solution
# define Symbols
# a, a1, a2, at, b, d, x, x0, x1, x2, x10, x20 = sp.symbols('a, a_1, a_2, a^t, b, d, x, x^0, x_1, x_2, x_1^0, x_2^0')
