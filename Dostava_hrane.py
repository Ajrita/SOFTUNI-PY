"""The restaurant opens its doors and offers several menus at preferential prices:
⦁	Chicken menu – 10.35 USD.
⦁	Fish menu – 12.40 USD.
⦁	Vegetarian menu – 8.15 USD.
The group will also order a dessert, the price of which is equal to 20% of the total bill (excluding delivery).
The delivery price is 2.50 USD and is finally charged.
Input Data
3 lines are read from the console:
⦁	Number of chicken menus – an integer in the range [0 … 99]
⦁	Number of fish menus – an integer in the range [0 … 99]
⦁	Number of vegetarian menus – an integer in the range [0 … 99]
Output Data
Print one line on the console: "{order price}": """

chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
total_food = chicken_menu * 10.35 + fish_menu * 12.40 + vegetarian_menu * 8.15
dessert = total_food * 0.2
sum = total_food + dessert + 2.50
print (sum)