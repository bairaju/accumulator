import matplotlib.pyplot as plt
import numpy as np
n=input("enter x length:")
x=[]
y=[]
for i in range(n):
	a=input("enter elements:")
	x.append(a)
print(x)
g=n
for i in range(n):
	z=x[g-1-i]
	y.append(z)
print(y)
d=n+g-1
while n<d:
	x.append(0)
	n=n+1
s=0
m=[]
for i in range(d):
	for j in range(g):
		s=s+((y[j])*(x[i-j]))
	m.append(s)
	s=0
print(m)
l=np.arange(0,d,1)
plt.subplot(3,1,1)
plt.stem(x)
plt.subplot(3,1,2)
plt.stem(y)
plt.subplot(3,1,3)
plt.stem(m)
plt.show()
