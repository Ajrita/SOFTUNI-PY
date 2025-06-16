"""Write a program that reads n number of integers given by the user and checks whether the sum of the numbers in
 even positions is equal to the sum of the numbers in odd positions.
⦁	If the sums are equal print two lines: "Yes" and on a new line "Sum = " + sum;
⦁	If the sums are not equal print two lines: "No" and on a new line "Diff = " + the difference;
The difference is calculated by absolute value. """

n = int(input())
suma_parnih = 0
suma_neparnih = 0

for i in range (1, n + 1):
    num = int(input())
    if i % 2 ==0:
        suma_parnih +=num
    else:
        suma_neparnih +=num
if suma_parnih == suma_neparnih:
    print("Yes")
    print(f"Sum = {suma_parnih}")
else:
    print("No")
    print(f"Diff = {abs(suma_parnih-suma_neparnih)}")