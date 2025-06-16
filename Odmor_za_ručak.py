"""During the lunch break, you want to watch an episode of your favorite series. Your task is to write a program that
will find out if you have enough time to watch the episode. Your lunch break consists of: time for lunch - 1/4 of the
total lunch break, and time for uninterrupted rest - 1/8 of the total lunch break. The rest is the time for watching
the series.
3 lines are read from the console:
⦁	Name of the series - a string
⦁	Episode duration - an integer in the range [10… 90]
⦁	Duration of the break - an integer in the range [10… 120]
On the console print:
⦁	If you have enough time to watch the episode:
"You have enough time to watch {name of series} and left with {time left} minutes free time."
⦁	If you don’t have enough time:
"You don't have enough time to watch {name of series}, you need {needed time} more minutes."
The time must be rounded to the nearest greater integer."""

import math
ime_serije = input()
trajanje_epizode = int(input())
trajanje_odmora = int(input())

vreme_ručka = trajanje_odmora/4
odmor= trajanje_odmora/8
ukupno = trajanje_epizode + vreme_ručka + odmor

ostatak = abs(trajanje_odmora - ukupno)

if trajanje_odmora >= ukupno:
    print(f"You have enough time to watch {ime_serije} and left with {math.ceil(ostatak)} minutes free time.")
else:
    print(f"You don't have enough time to watch {ime_serije}, you need {math.ceil(ostatak)} more minutes.")