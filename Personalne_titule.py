"""Write a console program that reads the age (a floating-point number) and gender ("m" or "f")
 entered by the user and prints an address from the following:
⦁	"Mr." - a man (gender "m") of 16 years or more
⦁	"Master" - a boy (gender "m") under 16 years old
⦁	"Ms." – a woman (gender "f") of 16 years or more
⦁	"Miss" – a girl (gender "f") under 16 years old """

age = float(input())
gender = input()

if age < 16:
    if gender == "m":
        print("Master")
    elif gender == "f":
        print("Miss")
else:
    if gender == "m":
        print("Mr.")
    elif gender == "f":
        print("Ms.")