import numpy as np
import matplotlib as plot 
import math
import matplotlib.pyplot as plt
#float a,b,c,d,e,f,N
sp=float(input("enter sp value:"))
sl=float(input("enter sl value:"))
ws=float(input("enter ws value:"))
wp=float(input("enter wp value:"))

a=((1/((sp)**2))-1)**0.5
b=((1/((sl)**2))-1)**0.5
e=a
d=np.arccosh((b/a))
f=np.arccosh((ws/wp))
N=int(d/f)
print "N VALUE IS:",N
w=np.arange(50000)
j=[]
r=[]
for w in range(50000):
	y=1/(1+(e**2)*(np.cosh(N*(np.arccosh(w/wp))))**2)**0.5
	j.append(y)
for w in range(50000):
	g=1/(1+(e**2)*(np.cos(N*(np.arccos(w/wp))))**2)**0.5
	r.append(g)
plt.plot(j)
plt.plot(r)
plt.show()


