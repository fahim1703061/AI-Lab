import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
#evenly sampled time at 200ms intervals
t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()



import numpy as np
import matplotlib.pyplot as plt
mu,sigma = 100, 15
x = mu+sigma*np.random.randn(10000)
n,bins,patches = plt.hist(x, 50, normed=1, facecolor='g',alpha=0.75)


plt.xlevel('Smarts')
plt.ylevel('Probability')
plt.title('Histogram of IQ')
plt.text(60,.025,r'$\mu=100,\\sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()