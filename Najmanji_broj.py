"""Write a program that, until it receives the "Stop" command, reads integers entered by the user, finds the least
among them, and prints it. One number is entered per line."""

import  sys
unos = input()
min = sys.maxsize #9223372036854775807

while unos != "Stop":
    n = int(unos)
    if n < min:
        min = n
    unos = input()
print(min)
