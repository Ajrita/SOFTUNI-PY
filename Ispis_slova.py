"""Write a program that receives text (string) and prints each character of the string on a separate line."""

text = input()
#Izvlačimo dužinu teksta koja ispisuje koliko slova ima i ona nam je drugi argument do kojeg će brojač ići
#Prvi argument će biti 0 jer indexiranje stringa kreće od nule
dužina = len(text)
for i in range ( 0, dužina): # for i in range ( 0, len(text))
    print(text[i])
