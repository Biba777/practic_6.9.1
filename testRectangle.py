from rectangle import Rectangle, Square, Circle

r1 = Rectangle(10, 5)
r2 = Rectangle(15, 5)

print(r1.get_area())
print(r2.get_area())


s1 = Square(5)
s2 = Square(3)

print(s1.get_area_square(),
      s2.get_area_square())

c1 = Circle(6)
c2 = Circle(10)

print(c1.get_area_circle(),
      c2.get_area_circle())

figures = [r1, r2, s1, s2, c1, c2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())