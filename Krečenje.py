"""Peter wants to repaint the living room and has hired craftsmen for this purpose.
Write a program that calculates the cost of repairs, given the following prices:
⦁	Protective nylon - 1.50 USD per square meter
⦁	Paint - 14.50 USD for a liter
⦁	Paint thinner - 5.00 USD for a liter
Just in case, to the necessary materials, Peter wants to add another 10% of the amount
of paint and 2 square meters of nylon, of course, 0.40 USD for bags. The amount paid to
the masters for 1 hour of work is equal to 30% of the sum of all costs for materials.
Input Data
The input is readable from the console and contains 4 lines:
⦁	Required amount of nylon (in square meters) – an integer in the range [1... 100]
⦁	Required amount of paint (in liters) – an integer in the range [1…100]
⦁	Quantity of detergent (in liters) – an integer in the range [1…30]
⦁	Hours for which the workers will do the work - an integer in the interval [1…9]
Output Data
On the console print:
⦁	"{total sum of all costs}" """

najlon = int(input())
boja = int(input())
deterdžent = int(input())
sati = int(input())

dodatak_boje = boja * 0.1
dodatak_najlona = 2
kese = 0.40
ruke_na_sat = ((najlon + dodatak_najlona) * 1.50 + (boja + dodatak_boje) * 14.50 + deterdžent * 5 + kese) * 0.3
ruke_ukupno = ruke_na_sat * sati
total = ((najlon + dodatak_najlona) * 1.50 + (boja + dodatak_boje) * 14.50 + deterdžent * 5 + kese) + ruke_ukupno
print(total)


