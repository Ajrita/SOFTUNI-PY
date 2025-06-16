"""John and Sophie are buying a house not far from Sofia. Sophie loves flowers so much that she
convinces you to write a program that will calculate how much it will cost them, to plant a certain
number of flowers and whether the available budget will be enough. Different flowers have different prices.
             Flowers	Roses	Dahlias	Tulips 	Narcissus	Gladiolus
Price in USD	          5	      3.80	 2.80	   3	      2.50
These are the following discounts:
⦁	If Sophie buys more than 80 Roses - 10% discount from the final price
⦁	If Sophie buys more than 90 Dahlias - 15% discount from the final price
⦁	If Sophie buys more than 80 Tulips - 15% discount from the final price
⦁	If Sophie buys less than 120 Narcissus - the price increases by 15%
⦁	If Sophie Buys less than 80 Gladiolus - the price increases by 20%
3 rows are read from the console:
⦁	Type of flowers - a string with options - "Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"
⦁	Number of flowers - an integer in the range [10…1000]
⦁	Budget – an integer in the range [50…2500]
On the console print:
⦁	If the budget is enough - "Hey, you have a great garden with {number of flowers} {type of flowers} and
{remaining amount} USD left."
⦁	If the budget is not enough - "Not enough money, you need {needed money} USD more."
The amount should be formatted to the second decimal place. """

cveće = input()
količina = int(input())
budžet = int(input())
cena_cveća = 0.00


if cveće == "Roses":
    cena_cveća = količina * 5
    if količina > 80:
          cena_cveća = cena_cveća * 0.9

elif cveće == "Dahlias":
    cena_cveća = količina * 3.80
    if količina > 90:
        cena_cveća = cena_cveća * 0.85

elif cveće == "Tulips":
    cena_cveća = količina * 2.80
    if količina > 80:
        cena_cveća = cena_cveća * 0.85

elif cveće == "Narcissus":
    cena_cveća = količina * 3
    if količina < 120:
        cena_cveća = cena_cveća * 1.15

elif cveće == "Gladiolus":
    cena_cveća = količina * 2.50
    if količina < 80:
        cena_cveća = cena_cveća * 1.20


fali = abs (cena_cveća - budžet)
ostalo = budžet - cena_cveća

if budžet >= cena_cveća:
    print(f"Hey, you have a great garden with {količina} {cveće} and {(ostalo):.2f} USD left.")
elif cena_cveća > budžet:
    print(f"Not enough money, you need {(fali):.2f} USD more.")


