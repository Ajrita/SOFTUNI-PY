"""Check if the number is greater than 10 and is even"""
unos = int(input())
valid = unos > 10 and unos % 2 == 0
print(type(valid))
print(valid)
if not valid:
    print("Invalid")
else:
    print("Valid")