"""Write a program that reads a positive integer n entered by the user and prints the numbers from n to 1 in
reverse order. The entered number n will always be greater than 1. """

n = int(input())
for i in range (n, 0, -1):
    print(i)