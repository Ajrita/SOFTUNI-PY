""""During the summer, the weather is often changing, and Steven needs your help.
Write a program that, depending on the time of day and the degrees, can recommend to Steven what
clothes to wear. Your friend has different plans for each stage of the day, which require a different look,
you can see them on the table.
2 rows are read from the console:
⦁	Degrees - an integer in the range [10…42]
⦁	Time of the day - "Morning", "Afternoon", "Evening" (string)
Print on the console: ""It's {degrees} degrees, get your {outfit} and {shoes}." """

temperatura = int(input())
doba_dana = input()
Outfit = ""
Shoes = ""


if doba_dana == "Morning":
    if 10 <= temperatura <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif temperatura <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif temperatura >= 25:
        Outfit = "T-Shirt"
        Shoes = "Sandals"

elif doba_dana == "Afternoon":
    if 10 <= temperatura <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif temperatura <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif temperatura >= 25:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"

elif doba_dana == "Evening":
    Outfit = "Shirt"
    Shoes = "Moccasins"
print(f"It's {temperatura} degrees, get your {Outfit} and {Shoes}.")
