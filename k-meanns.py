import numpy as np
import matplotlib.pyplot as plt
from Punkt2 import Punkt2

kolory=['b','g','r','c','m','y','k']


def tworzenie(x,y):
    n=len(x)
    tab=[]
    for i in range(n):
        pkt=Punkt2(x[i],y[i])
        tab.append(pkt)
    return tab

def przy(t):
    s=[]
    g=[]
    d=[]
    s.append(g)
    s.append(d)
    del g,d
    for i in range(len(t)):
        s[0].append(t[i].getX())
        s[1].append(t[i].getY())
    return s



def wys(gr,k):

    for i in range(len(k)):
        if(len(gr[i])!=0):
            z=przy(gr[i])
            plt.plot(z[0], z[1], 'o'+kolory[i])
        z = przy(k[i])
        plt.plot(z[0], z[1], '+'+kolory[i])
    plt.show()


def kmeans(k,tab):
    print('e')
    grr = [[], [], []]

    n=1
    for i in range(n):
        for j in range(len(tab)):
            tab[j].setCentroid(k)
            r=tab[j].getCentroid()
            grr[r].append(tab[j])

        for h in range(len(k)):
            xs=0
            ys=0
            if (len(grr[h]) != 0):
                for f in range(len(grr[h])):
                    xs+=grr[h][f].getX()
                    ys+=grr[h][f].getY()

                k[h].setX((xs/len(grr[h])))
                k[h].setY((ys / len(grr[h])))
        print('e')
        #wys(grr,k)
    return [tab,k]

# Setup, and create the data to plot
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
plt.plot(xr,yr,'x')
plt.plot(x,y,'o')
plt.show()
pktw=tworzenie(x,y)
sr=tworzenie(xr,yr)
el=kmeans(sr,pktw)
el=kmeans(el[1],el[0])
for i in range(len(el)):
    print(el[0][i])
    print(el[0][i].getCentroid())
xr=[]
yr=[]
for i in range(len(el[1])):
    xr.append(el[1][i].getX())
    yr.append(el[1][i].getY())
plt.plot(xr,yr,'x')
plt.plot(x,y,'o')
plt.show()
print("koniec")

