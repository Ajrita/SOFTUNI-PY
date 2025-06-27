"""Write a program that reads an integer from the console and on each following line integers until their sum is
greater than or equal to the original number. When the reading is finished, print the sum of the entered numbers."""

num = int(input())
sum = 0
while sum < num:
    broj = int(input())
    sum += broj
print(sum)