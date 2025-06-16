"""Write a program that reads an hour of the day (integer) and a day of the week (string)
 - entered by the user and checks whether the company's office is open, the office hours are from
 10:00(10 am) to 18:00(6 pm), from Monday to Saturday including."""

hour = int(input())
day = input().lower()

if 10 <= hour <= 18:
    if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday":
        print("open")
    else:
        print("closed")
else:
    print("closed")