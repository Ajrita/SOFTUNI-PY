"""A number is valid if it is in the range [100… 200] or is 0.
Write a program that reads an integer entered by the user and prints "invalid" if the number entered is not valid."""
unos = int(input())
is_valid = (100 <= unos <= 200) or unos == 0
if not is_valid:
        print("invalid")
