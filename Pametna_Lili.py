"""Lily is now N years old. For every birthday she receives a present.
⦁	For the odd birthdays (1, 3, 5...n) she receives toys.
⦁	For the even birthdays (2, 4, 6...n) she receives money.
For the second birthday, she receives 10.00 USD, and the amount increases by 10.00 USD for each following even birthday
(2 -> 10, 4 -> 20, 6 -> 30...etc.). Over the years, Lily has been secretly saving this money. Lily's brother, in the
years that she receives money, takes 1.00 USD of it. Lily sold the toys, she received over the years, for P USD each
and added the amount to the saved money. With the money, she wanted to buy a washing machine for X USD. Write a program
to calculate how much money she has collected and whether she has enough to buy a washing machine.
Input Data
The program reads 3 numbers entered by the user on separate lines:
⦁	Lily's age – an integer in the range [1...77]
⦁	Price of the washing machine – a floating-point number in the range [1.00...10 000.00]
⦁	Unit price of a toy – an integer in the range [0...40]
Output Data
Print on the console on a single line:
⦁	If Lily's money is enough:
⦁	"Yes! {N}" - where N is the remaining money after the purchase
⦁	If the money is not enough:
⦁	"No! {М}" - where M is the needed amount
The numbers N and M must be formatted to 2 digits after the decimal point."""

godine = int(input())
cena_veš_mašine = float(input())
cena_igračke = int(input())
suma = 0
godišnje = 0
igračka = 0

for i in range (1, godine + 1):
    if i % 2 == 0:
        godišnje += 1
        suma += godišnje * 10
    else:
        igračka += cena_igračke
ukupna_suma = suma - godišnje + igračka
razlika =  abs (ukupna_suma - cena_veš_mašine)

if ukupna_suma >=  cena_veš_mašine:
    print(f"Yes! {razlika:.2f}")
else:
    print(f"No! {razlika:.2f}")