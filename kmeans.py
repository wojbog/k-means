from Punkt2 import Punkt2
import matplotlib.pyplot as plt
class kmeans:



    def __init__(self,tab,k,n):

        self.tab=tab
        self.k=k
        self.n=n
        self.ilosc=len(tab)
        self.iloscCentro=len(k)
        self.grupy=[0]*len(tab)

    def getIlosc(self):
        return self.ilosc

    def getIloscCentro(self):

        return self.iloscCentro

    def grupowanie(self):
        for i in range(self.n):
            self.Fkmeans()


    def Fkmeans(self):
        #print('e')
        gr=[0]*self.getIloscCentro()


        for j in range(self.getIlosc()):
            self.tab[j].setCentroid(self.k)
            r = self.tab[j].getCentroid()
            self.grupy[j]=r
            gr[r]+=1
                #grr[r].append(self.tab[j])

        xs=[0]*self.getIloscCentro()
        ys = [0] * self.getIloscCentro()
        for h in range(self.getIlosc()):
            xs[self.grupy[h]]+=self.tab[h].getX()
            ys[self.grupy[h]]+= self.tab[h].getY()
        for f in range(self.getIloscCentro()):
            if(xs[f]>0 and ys[f]>0):
                self.k[f].setX((xs[f] / gr[f]))
                self.k[f].setY((ys[f] / gr[f]))
            '''   
            for h in range(self.getIloscCentro()):
                xs = 0
                ys = 0
                if (gr[h]> 0):
                    for f in range(len(grr[h])):
                        xs += grr[h][f].getX()
                        ys += grr[h][f].getY()

                    self.k[h].setX((xs / len(grr[h])))
                    self.k[h].setY((ys / len(grr[h])))
            print('e')
            # wys(grr,k)
            '''
       # return [tab, k]
    def pokaz(self):
        kolory=['blue','green','red','black']
        xr=[]
        yr=[]
        for i in range(self.getIloscCentro()):
            xr.append(self.k[i].getX())
            yr.append(self.k[i].getY())
        plt.plot(xr, yr, 'x')
        for i in range(self.getIlosc()):
            plt.scatter(self.tab[i].getX(), self.tab[i].getY(), color=kolory[self.grupy[i]])

        plt.show()


