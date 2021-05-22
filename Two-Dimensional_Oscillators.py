# Two Dimensional Oscillators Plots
#  ---------------------------------
import math
from matplotlib import pyplot as plt
import numpy as np

# -----------------------------------------------------------------------
# The simplest 2D/3D oscillator is the isotropic harmonic oscillator, for
# which the restoring force is proportional to the displacement from
# equilibrium, with the same constant of proportionality k in all
# directions: F = -kr.
#
# Important 3D examples of such oscillators are an atom vibrating near its
# equilibrium in a symmetrical crystal, and a proton (or neutron) as it
# moves inside a nucleus.
# ------------------------------------------------------------------------
# Declare initial conditions

A = 1  # Amplitude
t = np.linspace(0, 10, 1000)  # Time (s)
w1 = 10  # Angular Freq (rad/s)
w2 = 5
w3 = pow(2, 1/2)
w4 = 1
S = np.array([0, math.pi/2, math.pi/4]) # Make a list then loop through for each plot
numS = len(S)  # Allows for any number of values of S

# ------------------------------------------------------------------------
# Plot 2D isotropic oscillator with different relative phases
# Hold must be on otherwise each plot overrides the last

plt.figure(1)
for i in range(numS):

    x = A * np.cos(w2*t)
    y = A * np.cos((w2 * t) - S[i])
    plt.plot(x, y, '-')

plt.xlim([-1.15, 1.15]) # Increase plot dimensions
plt.ylim([-1.15, 1.15])
plt.title("2D Isotropic Oscillator's Motion (With Same Ang. Freq)")
plt.xlabel("Displacement from equilibrium in x direction (m)")
plt.ylabel("Displacement from equilibrium in y direction (m)")

# -----------------------------------------------------
# Possibly Change axes spine positions
# ax = plt.gca()  # gca stands for 'get current axis'
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data',0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data',0))
# -----------------------------------------------------

# If w1/w2 is rational then the motion is periodic.

plt.figure(2)
for i in range(numS):

    x = A * np.cos(w1*t)
    y = A * np.cos((w2*t) - S[i])
    plt.plot(x, y, '-')

plt.xlim([-1.15, 1.15])
plt.ylim([-1.15, 1.15])
plt.title("Periodic Motion")
plt.xlabel("Displacement from equilibrium in x direction (m)")
plt.ylabel("Displacement from equilibrium in y direction (m)")

# If w1/w2 is irrational then the motion never repeats itself.
# This type of motion is called quasiperiodic
# The motion of x and y is periodic, but because the two periods are incompatible, r = (x,y) is not.
plt.figure(3)
for i in range(numS):

    x = A * np.cos(w3*t)
    y = A * np.cos((w4*t) - S[i])
    plt.plot(x, y,  '-')

plt.xlim([-1.15, 1.15])
plt.ylim([-1.15, 1.15])
plt.title("Quasiperiodic Motion")
plt.xlabel("Displacement from equilibrium in x direction (m)")
plt.ylabel("Displacement from equilibrium in y direction (m)")

# Finally, show all figures currently saved
plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# Notes:
# 1. Choosing elements of array requires square brackets, not curved brackets
# 2. Use np. for cos function as this cos function can handle array inputs, unlike math cos function which gives scalar
# 3. Use range() function on length of array to create array of integers then for loop loops through this array where
# ... the elements act as indices of loop.
# 4. Figures for multiple plots when plt.show() is used. They are somewhat 'saved' until this is used.
# 5. Length function is lens()
