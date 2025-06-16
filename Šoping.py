""" Peter wants to buy N video cards, M CPUs, and P number of RAM. If the number of video cards is greater
than that of the processors, he receives a 15% discount on the final bill. The following prices apply:
⦁	Video card - 250 USD for one.
⦁	CPU - 35% from the total price of purchased video cards.
⦁	RAM - 10% from the total price of purchased video cards.
Calculate the amount needed to purchase the materials and calculate whether the budget will be enough.
4 lines are read from the console:
⦁	Peter’s budget – a floating-point number in the interval [0.0…100000.0]
⦁	Number of video cards – an integer in the interval [0…100]
⦁	Number of CPUs – an integer in the interval [0…100]
⦁	Number of RAM – an integer in the interval [0…100]
On the console, print one row with the following text:
⦁	If the budget is enough:
"You have {budget left} USD left!"
⦁	If the budget is not enough:
"Not enough money! You need {needed sum} USD more!"
Format the result to the second decimal symbol."""

budžet = float(input())
video_igrice = int(input())
grafička = int(input())
memorija = int(input())

total_igrice = video_igrice * 250

total = total_igrice + grafička * (total_igrice * 0.35) + memorija * (total_igrice * 0.1)

if video_igrice > grafička:
    total = total - (total * 0.15)
ostalo = budžet - total
nedostaje = total - budžet

if budžet >= total:
    print(f"You have {(ostalo):.2f} USD left!")
else:
    print(f"Not enough money! You need {(nedostaje):.2f} USD more!")