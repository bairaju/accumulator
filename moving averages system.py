import numpy as np
import matplotlib.pyplot as plt
Fs=500
f=5
sample=500
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plt.subplot(411)
plt.plot(x,y)
wave=np.sin(x)
m=np.random.rand(wave.shape[0])
plt.subplot(412)
plt.plot(x,m)
c=y+m
plt.subplot(413)
plt.plot(x,c)
l=[]
s=0
p=input("enter order of p:")
for n in range(0,500,1):
      for k in range(0,int(p)-1,1):
              s=s+c[n-k]
      z=float((s)/(p))
      l.append(z)
      s=0
plt.subplot(414)
plt.plot(x,l)
plt.show()

