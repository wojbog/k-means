from Punkt2 import Punkt2
from kmeans import kmeans
import numpy as np

def tworzenie(x,y):
    n=len(x)
    tab=[]
    for i in range(n):
        pkt=Punkt2(x[i],y[i])
        tab.append(pkt)
    return tab
y1 = np.random.randint(5000,10000,20)
x1 = np.random.randint(5000,10000,20)
y2 = np.random.randint(1,5000,10)
x2 = np.random.randint(1,5000,10)
y3 = np.random.randint(5000,10000,10)
x3 = np.random.randint(1,5000,10)
xr=np.random.randint(1,10000,3)
yr=np.random.randint(1,10000,3)
x=[]
y=[]
x.extend(x1)
x.extend(x3)
x.extend(x2)
y.extend(y1)
y.extend(y2)
y.extend(y3)
'''
x=[1,2,3,4,5,1,2,3,4,5,5,6,7,8,9,10]
y=[1,2,3,4,5,1,2,3,4,5,5,6,7,8,9,10]
xs=[0,5]
ys=[5,8]
'''

t=tworzenie(x,y)
s=tworzenie(xr,yr)

ob=kmeans(t,s,8)
ob.pokaz()
ob.grupowanie()
ob.pokaz()
