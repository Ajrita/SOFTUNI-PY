"""Tony and his friends loved to go fishing. They were so passionate about fishing that they decided to go fishing by
boat. The price of renting a boat depends on the season and the number of fishermen.
The price depends on the season:
⦁	The price for renting a boat in the spring is 3000 USD
⦁	The price for renting a boat in summer and autumn is 4200 USD.
⦁	The price for renting a boat in winter is 2600 USD.
Depending on the number of people, the group receives a discount:
⦁	If the group is up to 6 people inclusive – a 10% discount.
⦁	If the group is from 7 to 11 people inclusive - a 15% discount
⦁	If the group is more than 12 people - a 25% discount
The fishermen receive an additional 5% discount if their group is an even number. If it is autumn - then they do not
have an additional discount.
Write a program that calculates whether fisherman will have enough money.
Input Data
3 rows are read from the console:
⦁	Group budget - an integer in the range [1…8000]
⦁	Season - string: "Spring", "Summer", "Autumn", "Winter"
⦁	Number of fishermen - an integer in the range [4…18]
Output Data
Print on the console:
⦁	If the budget is enough:
"Yes! You have {money left} USD left."
⦁	If the budget is not enough:
"Not enough money! You need {needed money} USD."
Amounts must be formatted to two decimal places after the decimal point."""


budžet = int(input())
sezona = input()
broj_ribara = int(input())
renta = 0.00

if sezona == "Spring":
    renta = 3000
elif sezona == "Winter":
    renta = 2600
else:
    renta = 4200

if  broj_ribara <= 6:
    renta = renta * 0.90
elif 7 <= broj_ribara <= 11:
    renta = renta * 0.85
else:
    renta = renta * 0.75

if sezona != "Autumn" and broj_ribara % 2 == 0:
    renta = renta * 0.95

if renta <= budžet:
    print(f"Yes! You have {(budžet - renta):.2f} USD left.")
else:
    print(f"Not enough money! You need {(renta - budžet):.2f} USD.")