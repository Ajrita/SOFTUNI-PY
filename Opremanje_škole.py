"""The school year has already started and the head of the 10B class -
Sophie has to buy a certain number of packets of pens, packets of markers,
and detergent for cleaning the board. She is a regular customer of a bookstore,
so there is a discount for her, which is a percentage of the total.
Write a program that calculates how much money Sophie will have to raise to pay
the bill, keeping in mind the following price list:
⦁	Package of pens- 5.80 USD.
⦁	Package of markers - 7.20 USD.
⦁	Detergent- 1.20 USD (for liter)
Input Data
4 numbers are read from the console:
⦁	Package of pens - an integer in the range [0...100]
⦁	Package of markers – an integer in the range [0...100]
⦁	Liters of detergent – an integer in the range [0…50]
⦁	Percentage reduction – an integer in the range [0...100]
Output Data
Print on the console how much money Sophie will need to pay her bill."""

olovke = int(input())
markeri = int(input())
deterdžent = int(input())
popust = int(input())/100
total = olovke * 5.80 + markeri * 7.20 + deterdžent * 1.20
umanjenje = total * popust
suma = total - umanjenje
print(suma)