"""John decided to spend his vacation in a ski resort. Before he leaves, however, he must book a hotel and
calculate how much his stay will cost. The following types of accommodation are available, with the following
accommodation prices:
⦁	"room for one person" – 18.00 USD per night
⦁	"apartment" – 25.00 USD per night
⦁	"president apartment" – 35.00 USD per night
Depending on the number of days he will stay in the hotel (example: 11 days = 10 nights) and the type of room he
chooses, he can enjoy different discounts.
The discounts are as follows:
room type	      less than 10 days	      between 10 and 15 days	     more than 15 days
room for one	   no discount	             no discount	             no discount
apartment	    30% of the final price	    35% of the final price	     50% of the final price
president ap	10% of the final price	    15% of the final price	     20% of the final price
After the stay, Albert's feedback about the hotel's services can be positive or negative. If his feedback is positive,
Albert adds 25% of the price to the already discounted one. If his feedback is negative, he deducts 10% from the price.
Input Data
3 rows are read from the console:
⦁	First row - days of stay - integer in the range [0...365]
⦁	Second row – room type - "room for one person", "apartment" or "president apartment"
⦁	Third row - grade - "positive" or "negative"
Output Data
On the console print:
⦁	The price for his stay at the hotel is formatted to the second decimal place."""

ostanak = int(input())
smeštaj = input()
ocena = input()
cena = 0.00

if ostanak < 10:
    if smeštaj == "room for one person":
        cena = 18 * (ostanak - 1)
    elif smeštaj == "apartment":
        cena = 25 * (ostanak -1) * 0.7
    elif smeštaj == "president apartment":
        cena = 35 * (ostanak - 1) * 0.9
elif 10<= ostanak <=15:
    if smeštaj == "room for one person":
        cena = 18 * (ostanak - 1)
    elif smeštaj == "apartment":
        cena = 25 * (ostanak -1) * 0.65
    elif smeštaj == "president apartment":
        cena = 35 * (ostanak - 1) * 0.85
elif ostanak >15:
    if smeštaj == "room for one person":
        cena = 18 * (ostanak - 1)
    elif smeštaj == "apartment":
        cena = 25 * (ostanak - 1) * 0.5
    elif smeštaj == "president apartment":
        cena = 35 * (ostanak - 1) * 0.8
if ocena == "positive":
    cena = cena * 1.25
else:
    cena = cena * 0.9
print(f"{cena:.2f}")