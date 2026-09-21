
class GeometricFigure:
    def area(self):
        print("find the Area of a Geomtric Figure")


class Sqaure(GeometricFigure):
    def area(slef):
        side=10
        result=(side * side)
        print("Area of Square :",result)

class Reactangle(GeometricFigure):
    def area(slef):
        length=5
        breadth=12
        result=(length * breadth)
        print("Area of Reactangle :",result)

class Circle(GeometricFigure):
    def area(self):
        pi=3.14
        radius=4
        result=pi * radius * radius
        print("Area of Circle :",result)

figure=GeometricFigure()
figure.area()

sqaure=Sqaure()
rect=Reactangle()
circle=Circle()

figure=sqaure
figure.area()

figure=rect
figure.area()

figure=circle
figure.area()
