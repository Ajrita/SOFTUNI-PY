"""Write a program that calculates the necessary costs for the purchase
of food for dogs and cats. Food is shopped at a pet store,
with a pack of dog food priced at 2.50 USD and a pack of cat food costing 4 USD.
Input
2 lines are read from the console:
⦁	The number of packages of food for dogs – integer in the interval [0… 100]
⦁	The number of packages of food for cats – integer in the interval [0… 100]
Output
Print on the console:
"{end sum} USD."
"""
dog_food = int(input())
cat_food = int(input())

print(f"{dog_food * 2.50 + cat_food * 4} USD.")
