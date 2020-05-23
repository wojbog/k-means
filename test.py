from Punkt2 import Punkt2

pkt=Punkt2(2,2)

tab=[Punkt2(10,15),Punkt2(1,1),Punkt2(2,5)]

pkt.setCentroid(tab)
print("centroid: ")
print(tab[pkt.getCentroid()])

n = 3
m = 4
g = [[0] * m for i in range(n)]

for i in range(5):
    g[i].append(i)
    print("elo")

print(g)