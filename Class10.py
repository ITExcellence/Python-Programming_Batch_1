# absolute value
# num2 = -60

# print(num2)
# print(abs(num2))

#  Rounding to n decimal places
# n = 3.145968085778
# print(round(n, 3))

# n = 2**8
# n2 = pow(2, 8)

# print(n2)

import math, random

# print(round(math.pi, 2))

# Build a calculator that takes the radius of a circle and provides the area and circumference


r = float(input("Enter the radius: "))

area = math.pi*r*r
area = round(area, 2)

cmf = 2*math.pi*r
cmf = round(cmf, 2)

print(f"The area of the circle is {area} and the circumference is {cmf}.")