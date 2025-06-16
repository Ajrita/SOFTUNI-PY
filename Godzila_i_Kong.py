"""Filming for the long-awaited film "Godzilla vs. Kong" begins. Screenwriter Adam Wingard asks you to write
a program to calculate whether the funds provided are enough to shoot the film. The photos will require
a certain number of extras, clothing for each extra, and decor.
It is known that:
⦁	The set for the film is worth 10% of the budget.
⦁	For more than 150 extras, there is a 10% discount on clothing.
3 lines are read from the console:
⦁	Movie Budget- a floating-point number in the interval [1.00… 1000000.00]
⦁	Number of extras - an inter in the range [1…500]
⦁	Price for clothing of one extra – floating-point in the interval [1.00… 1000.00]
Two rows are printed on the console:
⦁	If the money for decor and clothes is more than the budget:
⦁	"Not enough money!"
⦁	"Wingard needs {needed money for the movie} USD more."
⦁	If the money for decor and clothes is less than or equal to the budget:
⦁	"Action!"
⦁	"Wingard starts filming with {money left} USD left."
The result must be formatted to the second decimal symbol."""

budžet = float(input())
dodaci_količina = int(input())
odelo_cena = float(input())

fset = budžet/10
odeća = dodaci_količina * odelo_cena
trošak = odeća + fset

if dodaci_količina > 150:
   trošak = (odeća - (odeća/10)) + fset # trošak = odeća * 0.9 + fset

nedovoljno = trošak - budžet
dovoljno = budžet - trošak

if trošak > budžet:
    print("Not enough money!")
    print(f"Wingard needs {(nedovoljno):.2f} USD more.")
elif budžet >= trošak:
    print("Action!")
    print(f"Wingard starts filming with {(dovoljno):.2f} USD left.")

