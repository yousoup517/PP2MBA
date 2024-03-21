#ex1
import math
degrees = float(input())
radians = degrees * (math.pi / 180)
print(round(radians,6))
#ex2
h = float(input())
b1 = float(input())
b2 = float(input())
area = 0.5 * (b1 + b2) * h
print(area)
#ex3
n = int(input())
s = int(input())
area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print(int(area))
#ex4
l = float(input())
h = float(input())
area = l*h
print(area)