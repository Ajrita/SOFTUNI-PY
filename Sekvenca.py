"""Write a program that accepts the number n entered by the user and prints all numbers ≤ n in the sequence:
1, 3, 7, 15, 31... Each following number is calculated by multiplying the previous number by 2 and adding 1. """

n = int(input())
counter = 1
while counter <= n:
    print(counter)
    counter = 2 * counter + 1