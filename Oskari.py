"""You have been invited by the academy to write software that calculates the points for an actor/actress.
The academy will give you initial points for the actor. Each assessor will then give their score.
The points an actor gets are formed by: the length of the assessor's name multiplied by the points they give divided
by two. If the score at any point exceeds 1250.5 the program must break and print that the given actor has received a
nomination.
Input Data
⦁	Actor's name - string
⦁	Academy points – a floating-point number in the range [2.0... 450.5]
⦁	Number of assessors n – an integer in the range [1… 20]
On the next n number of lines:
⦁	Assessor's name - string
⦁	Assessor's score – a floating-point number in the range [1.0... 50.0]
Output Data
Print on the console on a single line:
⦁	If the points are above 1250.5:
"Congratulations, {actor's name} got a nominee for leading role with {points}!"
⦁	If the points are not enough:
	"Sorry, {actor's name} you need {needed points} more!"
Format the result to the first digit after the decimal point!"""

ime_glumca = input()
poeni_akademije = float(input())
broj_glasača = int(input())
poeni = poeni_akademije

for i in range (broj_glasača):
    glasači_ime = input()
    glasači_poeni = float(input())
    imenski_poeni = len(glasači_ime)
    ukupni_poeni = (glasači_poeni * imenski_poeni) / 2
    poeni += ukupni_poeni
    if poeni > 1250.5:
        print(f"Congratulations, {ime_glumca} got a nominee for leading role with {poeni:.1f}!")
        break
if poeni < 1250.5:
    razlika = 1250.5 - poeni
    print(f"Sorry, {ime_glumca} you need {razlika:.1f} more!")