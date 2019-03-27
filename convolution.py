import matplotlib.pyplot as plt
import numpy as np
n=input("enter x length:")
k=input("enter h length:")

x=[]
for i in range(n):
	z=input("enter elements:")
	x.append(z)
print(x)
h=[]
for i in range(n+k-1):
	b=input("enter elements:")
	h.append(b)
print(h)
s=0
a=[]

for i in range(n+k-1):
	for j in range(n):
		s=s+((x[j])*(h[i-j]))
	a.append(s)
	s=0		
print(a)
l=np.arange(0,n+k-1,1)
plt.stem(l,a)
plt.show()
