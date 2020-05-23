import math

class Punkt2:
    '''
    Klasa reprezentująca punkt na płaszczyźnie
    Zastosowano współrzędne kartezjańskie
    '''

    licznik = 0;

    def __init__(self, c1, c2, polar = False ):
        '''
        Konstruktor tworzący prywatne składowe kartezjańskie x,y i zwiększający licznik ilości obiektów typu Punkt2
        :param c1: jeżeli polar == False, to c1 oznacza x, w przeciwnym przypadku c1 oznacza współrzędną biegunową r
        :param c2: jeżeli polar == False, to c2 oznacza y, w przeciwnym przypadku c2 oznacza współrzędną biegunową phi
        :param polar: jeżeli polar == False (domyślnie), to c1,c2 == x,y, w przeciwnym przypadku c1,c2 == r,phi
        '''

        print ("Wywołanie konstruktora: ", c1, ",", c2)
        if not polar:
            self.__x = c1
            self.__y = c2
        else:
          self.__x = c1 * math.cos(c2)
          self.__y = c1 * math.sin(c2)
        self.cen=-1
        Punkt2.licznik += 1
        print("licznik = ", Punkt2.licznik)


    def __del__(self):
        '''
        Destruktor obiektu - wywoływany automatycznie przez managera pamieci przy usuwaniu obiektu

        :return: None
        '''

        print("Wywołanie destruktora: ", self.__x, ",", self.__y)
        Punkt2.licznik -= 1;
        print("licznik = ", Punkt2.licznik)


    def setX(self,x):
        '''
        Funkcja zmieniająca współrzędną x
        :param x: nowa wartość dla x
        :return: None
        '''

        self.__x = x

    def setY(self,y):
        '''
             Funkcja zmieniająca współrzędną x
             :param y: nowa wartość dla y
             :return: None
             '''

        self.__y = y

    def getX(self):
        '''
        Funkcja zwracająca wartość współrzędnej x
        :return: x
        '''
        return self.__x

    def getY(self):
        '''
        Funkcja zwracająca wartość współrzędnej y
        :return: y
        '''
        return self.__y

    def getEuclidNorm(self):
        '''
        Funkcja obliczająca normę euklidesową punktu, tzn. odległość od środka układu
        :return: sqrt(x**2+y**2)
        '''
        return math.sqrt( self.__x**2 + self.__y**2 )

    def getDistance(self, p):
        '''
        Funkcja obliczająca odległość punktu (x,y) od innego punktu p
        :param p: punkt typu Punkt2
        :return: odległość pomiędzy (x,y) oraz p
        '''
        return  (self.__x-p.__x)**2 + (self.__y-p.__y)**2

    def __str__(self):
        '''
        przeładowanie funkcji str() na rzecz klasy Punkt2
        Bezpośrednio wywoływane przez instrukcję print(p), gdzie p jest typu Punkt2
        :return: wydruk w formacie: (x,y)
        '''
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

    def __repr__(self):
        '''
        przeładowanie funkcji repr() na rzecz klasy Punkt2
        Bezpośrednio wykorzystywane w konsoli jako drukarka, gdy nie stosujemy jawnie print
        :return: wydruk w formacie: (x,y)
        '''
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

    def getPolarCoords(self):
        '''
        Funkcja obliczająca współrzędne biegunowe na podstawie kartezjańskich
        Do obliczenia phi wykorzystujemy uogólniony arcus tangens (zob. https://en.wikipedia.org/wiki/Atan2)
        :return: [r,phi]
        '''
        r = self.getEuclidNorm()
        phi = math.atan2(self.__y, self.__x)
        return [r,phi]

    def setCentroid(self,k):
        n=len(k)
        m=self.getDistance(k[0])
        wy=0
        for i in range(1,n):
            if (self.getDistance(k[i]) < m):
                m=self.getDistance(k[i])
                wy=i
        self.cen=wy


    def getCentroid(self):
        '''

        :return: numer przynależności do grupy
        '''
        return self.cen