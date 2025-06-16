"""Write a program that reads a number n entered by the user and prints the numbers from 1 to n with step 3."""

krajnji_broj = int(input())
for i in range (1, krajnji_broj + 1, 3): #dodajemo + da bi se ispisao i broj koji smo uneli
    print(i) # i+=3