import sys
import os

sys.path.append('/application/geometric lib')

import circle
import square

a = int(input("Укажите сторону квадрата: "))
print("Площадь квадрата =", square.area(a))
print("Периметр квадрата =", square.perimeter(a))

r = int(input("Укажите радиус круга: "))
print("Площадь круга =", circle.area(r))
print("Длина окружности =", circle.perimeter(r))
