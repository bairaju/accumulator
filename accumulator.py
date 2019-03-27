import matplotlib.pyplot as plt
import numpy as np
n=input("enter no of samples:")
l=np.arange(0,n,1)
x=[]
s=0
for i in range(0,n,1):
     s=s+i
     x.append(s)
print (x)
plt.stem(l,x)
plt.show()


