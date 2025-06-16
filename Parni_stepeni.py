"""Write a program that receives a number n and prints the even powers of 2 ≤ 2n: 20, 22, 24, 26, …, 2n. """

n = int(input()) #broj stepena

for i in range (0, n + 1):
    if i % 2 == 0: #bitno nam je da stepen bude paran
        a = pow(2, i) # funkcija za stepenovanje broja; baza i koeficijent
        print(a)

#drugi način
N = int(input)
nume = 1
for i in range (0, N + 1, 2):
    print(nume)
    nume = nume * 2 *2

