"""There are several books on John’s list of required literature for the summer vacation.
 Since John prefers to play with friends outside, your task is to help him calculate how
 many hours a day he has to spend reading the required literature.
Input Data
3 lines are read from the console:
⦁	Number of pages in the current book – an integer in the interval [1…1000]
⦁	Pages read in 1 hour - an integer in the interval [1…1000]
⦁	The number of days for which you must read the book - an integer in the range [1…1000]
Output Data
To print on the console the number of hours that John has to spend reading each day."""
stranice_knjige = int(input())
progres_za_sat = int(input())
rok = int(input())
ukupno_sati= stranice_knjige // progres_za_sat
sum= ukupno_sati//rok
print(sum)