"""Rafael Nadal is a tennis player whose next goal is to climb the world rankings in men's tennis.
During the year, Nadal participates in a certain number of tournaments, and for each tournament, he receives points
that depend on the position he finished in the tournament. There are three options for finishing a tournament:
⦁	W - if he is the winner, he receives 2000 points
⦁	F - if he is a finalist, he receives 1200 points
⦁	SF - if he is a semi-finalist, he receives 720 points
Write a program that calculates how many points Rafael Nadal will have after playing all the tournaments, knowing how
many points he started the season with. Also, calculate how many points he earns on average from all tournaments played
and what percentage of tournaments he has won.
Input Data
Two lines are first read from the console:
⦁	Number of tournaments he has participated in – an integer in the range [1…20]
⦁	Initial number of points in the ranking – an integer in the range [1...4000]
A separate line is read for each tournament:
⦁	Tournament stage reached – string – "W", "F" or "SF"
Output Data
Print three lines in the following format:
⦁	"Final points: {number of points after the tournaments are played}"
⦁	"Average points: {average points earned per tournament}"
⦁	"{percentage of won tournaments}%"
Average points should be rounded down to the nearest integer number and percentages to be formatted to the second
digit after the decimal point."""

broj_mečeva = int(input())
broj_na_listi = int(input())

poeni = 0 # na turnirima
ukupne_pobede = 0

for i in range (1, broj_mečeva + 1):
    kotiranje = input()
    if kotiranje == "W":
        poeni += 2000
        ukupne_pobede += 1
    if kotiranje == "F":
        poeni += 1200
    if kotiranje == "SF":
        poeni += 720

ukupni_poeni = poeni + broj_na_listi
print(f"Final points: {ukupni_poeni}")

prosek = int(poeni/broj_mečeva)
print(f"Average points: {prosek}")

procenta_pobede = ukupne_pobede / broj_mečeva * 100
print(f"{procenta_pobede:.2f}%")