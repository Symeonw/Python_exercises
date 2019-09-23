import matplotlib.pyplot as plt
import math
import random
import numpy
%matplotlib inline 

u = range(-100,100)
y = [x**2 - x+2 for x in u]
plt.plot(u,y)
plt.show()
plt.annotate('(0,0)', xy=(0,0)
plt.close()

x = range(1,100)
y = [math.sqrt(n) for n in x]
plt.plot(x,y)
plt.show()
plt.close()

x = range(1,6)
y = [ n**3 for n in x]
plt.plot(x,y)
plt.show()
plt.close()

x = numpy.arange(1,10,0.1)
y = [math.tan(n) for n in x]
plt.plot(x,y)
plt.show()
plt.close()

x = range(1,100)
y = [2**n for n in x]
plt.ylim(0,200)
plt.plot(x,y)
plt.show()
plt.close()

a = [n for n in range(1,100)]
b = [2**n for n in a]
c = [n for n in numpy.arange(1,10,0.1)]
d = [math.tan(n) for n in c]
e = [ n for n in range(1,6)]
f = [ n**3 for n in e]
g = [n for n in range(1,100)]
h = [math.sqrt(n) for n in x]
i = [x for x in range(-100,100)]
j = [x**2 - x+2 for x in u]

plt.subplot(221)
plt.plot(a,b)
plt.subplot(222)
plt.plot(c,d)
plt.subplot(223)
plt.plot(e,f)
plt.subplot(224)
plt.plot(g,h)










