"""An enterprising person opens neighbourhood shops in several cities and sells at different prices;
Write a program that reads product (string), city (string), and quantity (a floating-point number)
entered by the user and calculates and prints how much the corresponding quantity of the selected product
costs in the specified city."""

product = input().lower()
city = input().lower()
quantity = float(input())

if city == "london":
    if product == "coffee":
       print(0.50 * quantity)
    elif product == "water":
       print(0.80 * quantity)
    elif product == "beer":
       print(1.20 * quantity)
    elif product == "sweets":
       print(1.45 * quantity)
    elif product == "peanuts":
       print(1.60 * quantity)
elif city == "rome":
    if product == "coffee":
       print(0.40 * quantity)
    elif product == "water":
       print(0.70 * quantity)
    elif product == "beer":
       print(1.15 * quantity)
    elif product == "sweets":
       print(1.30 * quantity)
    elif product == "peanuts":
       print(1.50 * quantity)
elif city == "paris":
    if product == "coffee":
       print(0.45 * quantity)
    elif product == "water":
       print(0.70 * quantity)
    elif product == "beer":
       print(1.10 * quantity)
    elif product == "sweets":
       print(1.35 * quantity)
    elif product == "peanuts":
       print(1.55 * quantity)
