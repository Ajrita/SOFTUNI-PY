"""Write a program that read from the console name, family, age and town
 and prints the following message:
 "You are <firstName> <lastName>, a <age>-years old person from < town>."
"""
name = input()
surname = input()
age = int(input())
town = input()
print(f"You are {name} {surname}, a {age}-years old person from {town}.")
