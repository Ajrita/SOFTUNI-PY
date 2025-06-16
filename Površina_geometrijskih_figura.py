"""Write a program in which the user enters the type and dimensions of a geometric figure
and calculates its area. The figures are of four types: square, rectangle, circle, and triangle.
The first line of the input reads the type of figure
(string with the following options: square, rectangle, circle, or triangle).
⦁	If the figure is a square: on the next line read a floating-point number - the length of its side
⦁	If the figure is a rectangle: on the next two lines read two floating-point numbers - the lengths of its sides
⦁	If the figure is a circle: on the next line read a floating-point number - the radius of the circle
⦁	If the figure is a triangle: on the next two lines read two floating-point numbers - the length of its
side and the length of the height to it. Round the result up to 3 digits after the decimal point."""
import math
figura = input()

if figura == 'square':
    a = float(input())
    P = a * a
    print(f"{P:.3f}")
elif figura == 'rectangle':
    a = float(input())
    b = float(input())
    P = a * b
    print(f"{P:.3f}")
elif figura == 'circle':
    r = float(input())
    P = math.pi * r *r
    print (f"{P:.3f}")
elif figura == 'triangle':
    a = float(input())
    h = float(input())
    P = a * h / 2
    print(f"{P:.3f}")


