# Class 1
"""
Created on Tue Oct  9 15:11:43 2018

@author: Thomaz
"""

import numpy as np
import matplotlib.pyplot as plt

#
b = np.linspace(10, 40, 31)
print(b)
# length of the beam
L1 = 210
# thickness of material
t = 18
# young modulus
E1 = 2300
Fmd1 = 12.46


def Displacement_Stress_Point_A(Fh):
    # displacement formula
    Wa = Fh * L1 ** 3 / (3 * E1 * t * b ** 3 / 12)
    print("Disp.", Wa)

    # stress formula
    Sa = (Fh * L1) * 6 / (t * b ** 2)
    print("Stress", Sa)

    # figure canvas
    fig = plt.figure()#.figure(figsize=(12, 6))

    # axes coord as fractions of the canvas (width and height)
    left, bottom, width, height = 0.1, 0.1, 0.7, 0.7
    ax = fig.add_axes((left, bottom, width, height), facecolor="#e1e1e1")

    # create graphics
    ax.plot(b, Wa, color="gray", label="Wa = Displacement", lw=2, ls='--')
    ax.plot(b, Sa, color="green", label="Sa = Stress", lw=2, ls='-')
    ax.plot((0, 40), (Fmd1, Fmd1), color="red", label="Breaking Point", lw=1)

    ax.set_xlabel("b")
    ax.set_ylabel("Wa and Sa")

    ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.0)
    ax.set_title("Displacement and Stress", fontsize=14, fontname="arial", color="black")

    fig.savefig("S9_class1_disp_stress_cantilever_beam.png", dpi=300)


Displacement_Stress_Point_A(60)

# Class 2

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 09:39:42 2018

@author: Thomaz
"""

# compare Entities

# greater than
1 > 2
# less than
1 < 2
# greater than or Equal to
1 >= 1
# less than or Equal to
1 <= 4
# equality
1 == 1
1 == "1"
'hi' == 'bye'
# inequality
1 != 2

# creating logic - boolean test

# AND
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# multiple logical operators
a = 3  # test a = 3.0
(1 == 2) or (2 == 5) or (3 == a)

# conditions - if,elif, else Statements
a = 3

# if
if 2 > 1:
    print(a)

# if, else
if 2 > a:
    print('bigger')
else:
    print('lower')

# if, elif, else
if 1 == a:
    print('first')
elif 2 == a:
    print('middle')
else:
    print('Last')

# control flow - FOOR LOOP
# str(n)

axis = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

label_list = []
for i in axis:
    for n in numbers:
        label = i + str(n)
        label_list.append(label)

print(label_list)

# foor loop with tuples - ex. of application - coordenates
points = [(0, 0, 3), (1, 3, 6), (4, 8, 9), (3, 6, 9)]
# points2  = points.reverse(points)

# solutions to flip numbers

# pavel solution
listx = []
listy = []
listz = []
for x, y, z in points:
    listx.append(x)
    listy.append(y)
    listz.append(z)
list2 = [tuple(listx), tuple(listy), tuple(listz)]

new_list = []

count = 0
while count < len(points):
    list1 = []
    for x, y, z in points:
        list1.append(x), list1.append(y), list1.append(z)
    pt = list1[count::3]
    new_list.append(pt)
    count = count + 1
print(new_list)

# solution numpy - using libraries
import numpy as np

new_list = np.transpose(points)
print(new_list)

# spliting the points
for i in points:
    print(i)

# working with a specific axis xyz
for x, y, z in points:
    print(x)
    print(y)
    print(z)

# while loop - perform an action until a condition is true
support = 100  # KN
load = 1

while load < support:
    print('i is: {}'.format(load))

    # add load = load + 10

# combining while and if, else statements
x = 100
y = 20

x = 1
while x < 100:
    if x <= 20:
        z = 10
        pto = (x, z)
        print('pto =', pto)
        x = x + 1

    elif (x > 20 and x <= 50):
        z = x
        pto1 = (x, z)
        print('pto1 =', pto1)
        x = x + 1
    else:
        z = 100 - x
        # print ('x', x)
        # print ('z', z)
        pto2 = (x, z)
        print('pto2 =', pto2)
        x = x + 1

########################################### Class 3_ Tensgerity
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:31:49 2019

@author: Thomaz
"""

import numpy as np
import matplotlib as mpl

mpl.use('qt5agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from scipy import optimize
import sympy

sympy.init_printing()


def tensegrity(n, Ld, rL, rU, i):
    """
    input:
    n  = number of rods; number of corners of a basis polygon (unit)
    Ld = length of a rod (cm)
    rL = radius of lower basis polygon (cm)
    rU = radius of upper basis polygon (cm)
    i  = number of possible starting positions of rods (by default = 1)

    output:
    Ta = additional twisting angle
    ß  = angle between lower points or upper points adjacent rods
    Lz = length of vertical ropes
    h  = height of the simplex modulus
    a1 = length of ropes between rods in the lower basis polygon
    a2 = length of ropes between rods in the upper basis polygon
    """

    # Set and calculate constants
    ß = 2 * np.pi / n
    a1 = 2 * rL * np.sin(ß / 2)
    a2 = 2 * rU * np.sin(ß / 2)

    def lz(Ta):
        return np.sqrt((Ld ** 2 - rL ** 2 - rU ** 2) + 2 * rL * rU * np.cos(i * ß + np.radians(Ta)))

    # Optimize
    Ta_min = optimize.brent(lz, brack=(0, 40))

    # Calculating variables
    Ta = np.linspace(0, 360, 361)
    print(Ta)
    h = np.sqrt(Ld ** 2 + 2 * rL * rU * np.cos(i * ß + np.radians(Ta)))

    # figure canvas
    fig = plt.figure(figsize=(6, 6))

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(Ta, lz(Ta), color="green", label="Rotation in degrees", lw=2, ls='-')
    ax.plot(Ta_min, lz(Ta_min), "o", markersize=10)

    print("Lz_min: ", lz(Ta_min))
    print("Ta_min:", Ta_min)


tensegrity(3, 40, 10, 10, 1)

########################################### Class 4_ PLOTING 2D

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib as mpl

mpl.use('qt5agg')
import matplotlib.pyplot as plt
import numpy as np

# figures , axes, line properties, legends

# figures
# axes coordinates as fractions of the canvas width and height
fig = plt.figure(figsize=(12, 4), facecolor="#f1f1f1")
left, bottom, width, height = .1, .1, .8, .8

ax = fig.add_axes((left, bottom, width, height))

# values for a function
x = np.linspace(0, 2, 1000)
y = np.cos(40 * x)

ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.draw()
plt.show()
fig.savefig("graphic.png", dpi=150, facecolor="#f1f1f1")

########################################### Class 5 _ PLOTING 3D
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:36:24 2019

@author: Thomaz
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.sans-serif'] = 'stix'

fig, axes = plt.subplots(1, 1, figsize=(4, 4), subplot_kw={'projection': '3d'})

def title_and_labels(ax, title):
    ax.set_title(title)
    ax.set_xlabel("$x$", fontsize=16)
    ax.set_ylabel("$y$", fontsize=16)
    ax.set_zlabel("$z$", fontsize=16)

r = np.linspace(0, 10, 100)
p = axes.plot(np.cos(r), np.sin(r), 6 - r)
#cb = fig.colorbar(p, ax=axes[0], shrink=0.6)
title_and_labels(axes, "plot")

fig.savefig("ch4-3d-plots.png", dpi=200)

########################################### Class 6 _ ????


