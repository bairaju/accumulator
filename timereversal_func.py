import matplotlib.pyplot as plt
import numpy as np
def tr(x):
	y=[]
	g=len(x)
	for i in range(g):
		z=x[g-i-1]
		y.append(z)
	for i in range(g-1):
		e=0
		y.append(e)
	return y
def convol(x,h):
	g=len(x)
	c=g+g-1
	s=0
	b=[]
	for i in range(c):
		for j in range(g):
			s=s+((x[j])*(h[i-j]))
		b.append(s)
		s=0
	return b
n=input("enter length:")
q=[]
for i in range(n):
	s=input("enter elements:")
	q.append(s)
print(q)
k=tr(q)
print(k)
w=convol(q,k)
print(w)
plt.stem(w)
plt.show()			
