"""Write a program that reads a product name entered by the user and checks if it is a fruit or vegetable.
⦁	The fruits are banana, apple, kiwi, cherry, lemon, and grapes
⦁	The vegetables are tomato, cucumber, pepper, and carrot
⦁	Everything else is "unknown"
Print "fruit", "vegetable" or "unknown" depending on the introduced product. """

unos = input()
if unos == "banana" or unos == "apple" or unos == "kiwi" or unos == "cherry" or unos == "lemon" or unos == "grapes":
    print("fruit")
elif unos == "tomato" or unos == "cucumber" or unos == "pepper" or unos == "carrot":
    print("vegetable")
else:
    print("unknown")
