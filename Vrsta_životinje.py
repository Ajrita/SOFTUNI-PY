"""Write a program that prints the species of the animal according to its name entered by the user.
⦁	dog -> mammal
⦁	crocodile, tortoise, snake -> reptile
⦁	others -> unknown """
animal = input().lower()
animals = {
    "dog": "mammal",
    "crocodile": "reptile",
    "tortoise" : "reptile",
    "snake" : "reptile"
}
print (animals.get(animal, "unknown"))

#S IF-ELIF
životinja = input().lower()
if životinja == "dog":
     print("mammal")
elif životinja == "crocodile" or životinja == "tortoise" or životinja == "snake":
     print("reptile")
else:
     print("unknown")


