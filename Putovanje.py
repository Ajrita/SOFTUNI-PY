"""Strangely, most people plan their vacation early. A young programmer has an exact budget and free time for each
season. Write a program that will accept the budget and the season, and print, where the programmer will rest and how
much he will spend. The budget determines the destination, and the season determines how much of the budget he will
spend. If it is summer, he will rest at the campsite and in the winter at a hotel. If he is in Europe, he will stay in
a hotel, regardless of the season. Each campsite or hotel, according to the destination, has its price that corresponds
to a certain percentage of the budget:
⦁	At 100 USD or less – somewhere in Serbia
⦁	Summer – 30% of the budget
⦁	Winter – 70% of the budget
⦁	At 1000 USD or less – somewhere in Balkans
⦁	Summer – 40% of the budget
⦁	Winter – 80% of the budget
⦁	For more than 1000 USD. – somewhere in Europe
⦁	When travelling in Europe, regardless of the season he will spend 90% of the budget.
Input Data
2 rows are read from the console:
⦁	The budget – a floating-point number in the range [10.00...5000.00].
⦁	The season – a string "summer" or "winter"
Output Data
On the console print.
⦁	Somewhere in {destination}
⦁	{Type of holiday} – {Money spent}
⦁	The Holiday can be a "Camp", or "Hotel"
⦁	The amount must be rounded to the second decimal place """

budžet = float(input())
sezona = input().lower()
cena = 0.00
zemlja = ""
smeštaj = ""

if budžet <= 100:
    zemlja = "Serbia"
    if sezona == "summer":
       cena = budžet * 0.3
    elif sezona == "winter":
       cena = budžet * 0.7
elif budžet <= 1000:
    zemlja= "Balkans"
    if sezona == "summer":
        cena = budžet * 0.4
    elif sezona == "winter":
        cena = budžet * 0.8

elif budžet > 1000:
    zemlja= "Europe"
    cena = budžet * 0.9

print(f"Somewhere in {zemlja}")
if sezona == "summer" and zemlja!= "Europe":
    print(f"Camp - {(cena):.2f}")
else:
    print(f"Hotel - {(cena):.2f}")



