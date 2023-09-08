from math import *

class RegularPolygon:
    def __init__(self, n: int = 3, sideL:float = 1, x: float = 0, y: float = 0):
        self.__n = n
        self.__sideL = sideL
        self.__x = x
        self.__y = y

    def get_n(self):
        return self.__n

    def get_side(self):
        return self.__sideL

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_n(self, newN):
        self.__n = newN

    def set_Side(self, newside):
        self.__sideL = newside

    def set_x(self, newX):
        self.__x = newX

    def set_y(self, newY):
        self.__y = newY

    def getArea(self):
        x = pi/self.__n
        Area = (self.__n * (self.__sideL**2))/(4 * tan(x))
        area = "{:.2f} sq. meters".format(Area)
        return area

    def getPerimeter(self):

        z = self.__n * self.__sideL
        perimeter = "{:.2f} units".format(z)
        return perimeter


regpoly = RegularPolygon()
print("Area of RegPolygon: ", regpoly.getArea())
print("Perimeter of RegPolygon: ", regpoly.getPerimeter())
print('')

poly1 = RegularPolygon(6, 4)
print("Area poly1: ", poly1.getArea())
print("Perimeter of poly1: ", poly1.getPerimeter())
print('')

poly2 = RegularPolygon(10, 4, x=5.6, y=7.8)
print("Area of poly2: ", poly2.getArea())
print("Perimeter of poly2: ", poly2.getPerimeter())

