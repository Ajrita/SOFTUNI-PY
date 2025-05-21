"""Write a program that reads an angle in radians (floating-point number)
 and converts it into degrees. Use the formula: angle = radian* 180 / π."""

from math import pi

rad = float(input())
degrees = rad*180/pi
print(degrees)