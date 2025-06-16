"""Write a program that reads n number of integers entered by the user and sums them.
⦁	From the first line of the input, the count of numbers n is entered.
⦁	From the next n lines, one integer is entered at a time.
The program has to read the numbers, sum them and print their sum."""

n = int(input())
sum = 0

for i in range (1, n +1):
    value = int(input())
    sum += value
print(sum)