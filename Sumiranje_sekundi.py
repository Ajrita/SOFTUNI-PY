"""Three athletes finish in a matter of seconds (between 1 and 50).
Write a program that reads the times of the competitors in seconds entered by the user
and calculates their total time in the format "minutes:seconds".
Display the seconds with leading zero (2  "02", 7  "07", 35  "35"). """
import math
prvi = int(input())
drugi = int(input())
treći = int(input())
ukupno = prvi + drugi + treći
minuti = math.floor(ukupno / 60) # ukupno//60
sekunde = ukupno % 60
#dodajemo vodeće nule ako je broj sekundi manji od 10

if sekunde < 10:
    print(f"{minuti}:0{sekunde}")
else:
    print(f"{minuti}:{sekunde}")