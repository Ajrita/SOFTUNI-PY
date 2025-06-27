"""On Jose's eighteenth birthday, he decided that he was going to move out to live in an apartment. He packed his
stuff in boxes and found an ad for a suitable apartment to rent. He began moving his stuff in pieces because he
couldn't carry it all at once. He has limited free space in his new apartment where he can place his stuff so that
the place is suitable for living.
Write a program that calculates the free volume of Jose's apartment that remains after he moves his stuff.
Each box is of exact size:  1m. x 1m. x 1m.

Input Data
The user enters the following data on separate lines:
⦁	Free space width - an integer
⦁	Free space length - an integer
⦁	Free space height - an integer
⦁	On the next lines (until the "Done" command is received) – the number of boxes to be moved to the apartment - integers
The program should finish by receiving the "Done" command or if the free space runs out.
Output Data
Print one of the following lines on the console:
⦁	If you receive the "Done" command and there is still space available:
"{number of free cubic meters} Cubic meters left."
⦁	If the free space runs out before the "Done" command is received:
"No more free space! You need {number of not enough cubic meters} Cubic meters more." """

width = int(input())
lenght = int(input())
height = int(input())
prostor = width * height * lenght
kutije = 0

unos = input() #čitamo prvi unos; može biti ili "Done" ili broj kutija

while unos !="Done":
    unos = int(unos)
    kutije += unos #dodajemo broj kutija u ukupan zauzet prostor
    if kutije > prostor: #Ako je broj kutija veći od ukupnog slobodnog prostora, prekini petlju
        break
    unos = input()

diff = abs (prostor-kutije)

if kutije >= prostor:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")
