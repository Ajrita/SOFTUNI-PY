"""Write a program that reads text (string) entered by the user and calculates and prints the sum of the vowel
values according to the table below. """
text = input()
a = 1
e = 2
i = 3
o = 4
u = 5
zbir = 0

for char in text:
    if char == "a":
        zbir += a
    if char == "e":
        zbir += e
    if char == "i":
        zbir += i
    if char == "o":
        zbir += o
    if char == "u":
        zbir += u
print(zbir)

# drugi način
text = input()
sum = 0
for i in range (0, len(text)):
    if text[i] == "a":
        sum += 1
    if text[i] == "e":
        sum += 2
    if text[i] == "i":
        sum += 3
    if text[i] == "o":
        sum += 4
    if text[i] == "u":
        sum += 5
print(sum)
