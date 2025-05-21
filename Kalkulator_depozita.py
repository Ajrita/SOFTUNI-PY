"""Write a program that calculates how much you will receive at the end of the deposit period
at a certain interest rate. Use the following formula:
amount = deposited amount + term of the deposit * ((deposited amount * annual interest rate) / 12)
Input Data
3 lines are read from the console:
⦁	Deposit amount – a floating-point number in the interval [100.00 … 10000.00]
⦁	Term of the deposit (in months) – an integer in the interval [1…12]
⦁	Annual interest rate – a floating-point number in the interval [0.00 …100.00]
Output Data
Print the amount on the console at the end of the term. """

depozit = float(input())
vreme = int(input())
kamatna_stopa =float(input())/100 #moramo pretvoriti procenat u decimalan broj; ovo je kamata za godinu dana
iznos = depozit + (vreme * ((depozit * kamatna_stopa)/12)) #depozit sabiramo sa kamatama za određeni broj meseci

print(f"Iznos je {iznos}")