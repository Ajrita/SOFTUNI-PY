"""Write a program that reads text from the console (person's name)
and prints "Hello, <name>! " where <name> name is entered from the console."""

name = input()
print("Hello, " + name + "!")

#drugi način, uz pomoć funkcije 'end' koja služi da se naredni print ispisuje u istoj liniji
name = input()
print("Hello, ", end="")
print(name)