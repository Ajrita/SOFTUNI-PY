"""Write a program that reads n number of integers entered by the user and checks if among them exists a number that
is equal to the sum of all others. If there are such an element print "Yes" and on a new line "Sum = " + its value
If there are no such element print "No" and on a new line "Diff = " + the difference between the largest element
and the sum of the others (by absolute value)"""
import sys
n = int(input())
max = -sys.maxsize #-9223372036854775807
suma = 0
for i in range (1, n +1):
    num = int(input())
    suma +=num
    if num > max:
        max = num
suma = suma - max
if suma == max:
    print("Yes")
    print(f"Sum = {suma}")
else:
    print("No")
    print(f"Diff = {abs(suma-max)}")