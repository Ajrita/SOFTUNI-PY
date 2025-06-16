"""The hotel offers 2 types of rooms: studio and apartment. Write a program that calculates
the price for the entire stay for a studio and apartment. Prices depend on the month of stay.

The following discounts are:
⦁	studio, for more than 7 nights in May and October: 5% discount.
⦁	studio, for more than 14 nights in May and October: 30% discount.
⦁	studio, for more than 14 nights in June and September: 20% discount.
⦁	apartment, for more than 14 nights, regardless of the month: 10% discount.
Input Data
2 rows are read from the console:
⦁	On the first row is the month – May, June, July, August, September, or October
⦁	On the second row is the number of nights – an integer in the range [0 ... 200]
Output Data
On the console print:
⦁	On the first line: "Apartment: {price for the whole stay} USD."
⦁	On the second line: "Studio: {price for the whole stay} USD."
The price for the entire stay must be formatted to two decimal places. """

mesec = input()
noć = int(input())
studio = 0.00
apartman = 0.00

if mesec == "May" or mesec == "October":
    studio = 50 * noć
    apartman = 65 * noć
    if 7 < noć <= 14:
        studio = 50 * noć * 0.95
    elif noć > 14:
        studio = 50 * noć * 0.7
        apartman = 65 * noć * 0.9
elif mesec == "June" or mesec == "September":
    studio = 72.20 * noć
    apartman = 68.70 * noć
    if noć > 14:
        studio = 75.20 * noć * 0.8
        apartman = 68.70 * noć * 0.9
else:
    studio = 76 * noć
    apartman = 77 * noć
    if noć > 14:
       apartman = 77 * noć * 0.9

print(f"Apartment: {(apartman):.2f} USD.")
print(f"Studio: {(studio):.2f} USD.")