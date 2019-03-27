import numpy as np
import matplotlib as plot 
import math
import matplotlib.pyplot as plt
#float a,b,c,d,e,f,N
sp=float(input("enter sp value:"))
sl=float(input("enter sl value:"))
ws=float(input("enter ws value:"))
wp=float(input("enter wp value:"))
a=(1/((sp)**2))-1
b=(1/((sl)**2))-1
c=float(a/b)
d=wp/ws
e=np.log10(c)
f=np.log10(d)
N=np.ceil((0.5)*(e/f))
g=(1/(sp**2))-1
k=g**(1/(2*N))
wc=wp/k
print N
print wc
w=np.arange(0,1000,1)
j=[]
for w in range(1000):
  l=(w/wc)**(2*N)
  m=1+l
  o=m**(0.5)
  n=1/o
  j.append(n)
plt.plot(j)
plt.show()
   


