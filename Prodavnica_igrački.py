"""Sophie has a toy store. She receives a large order that she must fulfill.
With the money she will earn, she wants to go on a trip.
Toy prices:
⦁	Puzzle - 2.60 USD.
⦁	Talking doll - 3 USD.
⦁	Teddy bear - 4.10 USD.
⦁	Minion - 8.20 USD.
⦁	Truck - 2 USD.
If the ordered toys are 50 or more, the store makes a 25% discount on the total price.
Sophie must give 10% of the earned money for the rent of the store.
Calculate whether the money will be enough for her to go on a trip.

6 lines are read from the console:
⦁	Price of the trip – floating-point in the interval [1.00 … 10000.00]
⦁	Number of puzzles – integer in the interval [0… 1000]
⦁	Number of talking dolls - integer in the interval [0 … 1000]
⦁	Number of teddy bears - integer in the interval [0 … 1000]
⦁	Number of minions - integer in the interval [0 … 1000]
⦁	Number of trucks - integer in the interval [0 … 1000]

On the console print:
⦁	If the money is enough print:
⦁	"Yes! { remaining money } USD left."
⦁	If the money isn’t enough print:
⦁	"Not enough money! { needed money } USD needed."

The result must be formatted to the second decimal symbol.
"""

putovanje = float(input())
puzle = int(input())
lutke = int(input())
mede = int(input())
minjoni = int(input())
kamioni = int(input())

cena = puzle * 2.60 + lutke * 3 + mede * 4.10 + minjoni * 8.20 + kamioni * 2
količina = puzle + lutke + mede + minjoni + kamioni


if količina >= 50:
    cena = cena - (cena * 0.25)

zarada = cena - (cena * 0.1)
ostatak = zarada - putovanje
falinka = putovanje - zarada

if zarada >= putovanje:
    print(f"Yes! {(ostatak):.2f} USD left.")
else:
    print(f"Not enough money! {(falinka):.2f} USD needed.")