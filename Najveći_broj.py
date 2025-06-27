"""Write a program that, until it receives the "Stop" command, reads integers entered by the user, finds the largest
among them, and prints it. One number is entered per line."""
import sys
unos = input()
max = -sys.maxsize #-9223372036854775807

while unos != "Stop":
    n = int(unos)
    if n > max:
        max = n
    unos = input()
print(max)


