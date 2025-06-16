"""In a cinema, the chairs are arranged in a rectangular shape in r rows and c columns. There are three types of
screenings with tickets at different prices:
⦁	Premiere – premiere screening, at a price of 12.00 USD.
⦁	Normal – standard screening, at a price of 7.50 USD.
⦁	Discount – screening for children, and students at a reduced price of 5.00 USD.
Write a program that reads the type of projection (string), a number of rows, and a number of columns in the hall
(integers) entered by the user and calculates the total ticket revenue for a full hall. Print the result in the format
 as in the examples below, 2 characters after the decimal point. """

projekcija = input()
redovi = int(input())
kolone = int(input())
površina = redovi*kolone

income = 0

if projekcija == "Premiere":
    income = 12 * površina
elif projekcija == "Normal":
    income = 7.5 * površina
elif projekcija == "Discount":
    income = 5 * površina
print(f"{income:.2f} USD")
