"""A student must go to an exam at a certain time. He arrives at the examination room at a certain time of arrival.
It is considered that the student arrived on time if he arrives at the time of the exam or up to half an hour before.
If he arrives more than 30 minutes earlier, he is early. If he comes after the exam time, he is late. Write a program
that reads exam time and arrival time and records whether the student arrived on time, is early or late, and by how
many hours or minutes is early or late.
Input Data
4 rows are read from the console:
⦁	The first line contains the exam time - an integer from 0 to 23.
⦁	The second line contains the minute of the exam – an integer from 0 to 59.
⦁	The third line contains the time of arrival – an integer from 0 to 23.
⦁	The fourth line contains the minute of arrival – an integer from 0 to 59.
Output Data
On the first line print:
⦁	"Late" - if the student arrives later than the exam time.
⦁	"On time" - if the student arrives exactly at the time of the exam or up to 30 minutes earlier.
⦁	"Early" - if the student arrives more than 30 minutes before the exam time.
If the student arrives at least one minute apart from the exam time, print on the next line:
⦁	"mm minutes before the start" for arriving earlier by less than an hour.
⦁	"hh:mm hours before the start" or 1 hour or earlier. Always print the minutes in 2 digits, for example 1:05.
⦁	 "mm minutes after the start" for an hour delay.
⦁	"hh:mm hours after the start" for a delay of 1 hour or more. Always print the minutes with 2 digits,
for example 1:03."""


vreme_ispita_sati = int(input())
vreme_ispita_minuti = int(input())
vreme_dolaska_sati = int(input())
vreme_dolaska_minuti = int(input())

time_exam = (vreme_ispita_sati * 60) + vreme_ispita_minuti
time_arrival = (vreme_dolaska_sati * 60) + vreme_dolaska_minuti
rezultat = ""
razlika =  time_exam - time_arrival

if razlika < 0:
    rezultat = "Late"
elif 0 <= razlika <= 30:
    rezultat = "On time"
else:
    rezultat = "Early"

print(rezultat)

if rezultat == "Early" or rezultat == "On time":
    if 0 < razlika < 60:
        print(f"{razlika} minutes before the start")
    elif 0 != razlika > 60:
        if razlika % 60 > 9:
            print(f"{razlika // 60}:{razlika % 60} hours before the start")
        elif razlika % 60 <= 9:
            print(f"{razlika // 60}:0{razlika % 60} hours before the start")
    elif razlika == 60:
        print("1:00 hours before the start")
elif rezultat == "Late":
    razlika = abs(razlika)
    if razlika < 60:
        print(f"{razlika} minutes after the start")
    else:
        if razlika % 60 > 9:
            print(f"{razlika // 60}:{razlika % 60} hours after the start")
        elif razlika % 60 <= 9:
            print(f"{razlika // 60}:0{razlika % 60} hours after the start")