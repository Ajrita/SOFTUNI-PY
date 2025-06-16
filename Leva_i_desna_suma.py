"""Write a program that reads 2 * n number of integers given by the user and checks if the sum of the first n numbers
(left sum) is equal to the sum of the second n numbers (right sum). If equal, prints "Yes, sum = " + sum; otherwise
prints "No, diff = " + diff. The difference is calculated as a positive number (in absolute value)."""

n = int(input())
leva_suma = 0
desna_suma = 0

for i in range (0, n):
    leva_suma += int(input())
for i in range (0, n):
    desna_suma += int(input())

if leva_suma == desna_suma:
    print(f"Yes, sum = {leva_suma}")
else:
    print(f"No, diff = {abs(leva_suma - desna_suma)}")
