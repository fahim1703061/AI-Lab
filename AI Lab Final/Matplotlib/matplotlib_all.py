import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

# plt.plot([1,2,3,4,5,6])
# plt.ylabel('some numbers')
# plt.show()

# plt.plot([1,2,3,4], [1,4,9,16])
# plt.show()

############

# plt.plot([1,2,3,4], [1,3,7,13], 'ro')
# plt.axis([0,6,0,20])
# plt.show()

#############

# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)

# #red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

###############

# def f(t):
#   return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure(1)
# plt.subplot(3,1,1)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(3,1,2)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()

# t = np.arange(0., 5., 0.2)

# #red dashes, blue squares and green triangles
# plt.subplot(3,1,3)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

###############

# @def  Working with text

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, density=True, stacked = True, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

###############