# Damped Oscillator

import numpy as np
from matplotlib import pyplot as plt


# Declare Initial Conditions
t = np.linspace(1,100,10000)
A = 1
B = 0.08
w1 = 4
S = 1
x = (A * np.exp(-B*t)) * np.cos(w1*t - S)

# Plot underdamped oscillations
plt.figure(1)
plt.plot(t, x)
plt.xlim([-11.15, 111.15])  # Increase plot dimensions
plt.ylim([-1.15, 1.15])
plt.title("Underdamped Oscillator's Motion")
plt.xlabel("Time (s)")
plt.ylabel("Displacement from equilibrium in y direction (m)")

plt.show()  # set plot(s) properties above before showing
