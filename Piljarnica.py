"""Fruit shop on weekdays works at the following prices:
fruit	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
price	2.50	1.20	0.85	1.45	2.70	5.50	3.85
On Saturdays and Sundays, the store is works at higher prices:
fruit	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
price	2.70	1.25	0.90	1.60	3.00	5.60	4.20
Write a program that reads from the console fruit (banana / apple / orange / grapefruit / kiwi / pineapple / grapes),
day of the week (Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday),
and quantity (a floating-point number), entered from the customer, and calculates the sum according to the prices
in the tables above. In case of an invalid day of the week or invalid fruit name, print "error". """

fruit = input().lower()
day = input().lower()
quantity = float(input())
price = 0.0
total_cost = 0.0

if day == "monday" or day == "tuesday" or day == "friday" or day == "wednesday" or day == "thursday":
    if fruit == "banana":
        price = 2.50
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "apple":
        price = 1.20
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "orange":
        price = 0.85
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "grapefruit":
        price = 1.46
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "kiwi":
        price = 2.70
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "pineapple":
        price = 5.50
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "grapes":
        price = 3.85
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    else:
        print("error")
elif day == "saturday" or day == "sunday":
    if fruit == "banana":
        price = 2.70
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "apple":
        price = 1.25
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "orange":
        price = 0.90
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "grapefruit":
        price = 1.60
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "kiwi":
        price = 3.00
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "pineapple":
        price = 5.60
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    elif fruit == "grapes":
        price = 4.20
        total_cost = price * quantity
        print(f"{total_cost:.2f}")
    else:
        print("error")
else:
    print("error")