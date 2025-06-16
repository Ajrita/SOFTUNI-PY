"""Write a program that reads the day of the week (string) - entered by the user.
If the day is a working day, it prints on the console - "Working day", if it is a day off - "Weekend".
If any text other than the day of the week is entered, print "Error" """

day = input()
days = {
    "Monday": "Working day",
    "Tuesday":"Working day",
    "Wednesday":"Working day",
    "Thursday":"Working day",
    "Friday":"Working day",
    "Saturday": "Weekend",
    "Sunday": "Weekend"
}

print(days.get(day, "Error"))

#s IF_ELIF

dan =input().lower()

if dan == "monday" or dan == "tuesday" or dan == "wednesday" or dan ==  "thursday" or dan == "friday":
    print("Working day")
elif dan == "saturday" or dan == "sunday":
    print("Weekend")
else:
    print("Error")