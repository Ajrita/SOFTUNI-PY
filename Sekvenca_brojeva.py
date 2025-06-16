"""Write a program that reads n number of integers. Print the largest and the smallest number among the entered ones."""

import sys
n = int(input())
max = - sys.maxsize #-9223372036854775807
min = sys.maxsize #9223372036854775807
for i in range (0, n): #for i in range (1, n + 1):
        num = int(input()) #17,5,20
        if num < min: #17<9223372036854775807, 5<17, 20<5
            min = num #min = 17 --> 5
        if num > max: #17 > -9223372036854775807, 5>17, 20>17
            max = num #max = 17 --> max = 20
print(f"Max number: {max}")
print(f"Min number: {min}")