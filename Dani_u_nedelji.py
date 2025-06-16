"""Write a program that reads an integer entered by the user and prints a day of the week within [1 ... 7]
 or prints "Error" if the number entered is invalid."""

day = int(input())

days= {
    1 :"Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
print(days.get(day, "Error"))

#s IF-ELIF

dan = int(input())

if dan == 1:
    print("Monday")
elif dan == 2:
    print("Tuesday")
elif dan == 3:
    print("Wednesday")
elif dan == 4:
    print("Thursday")
elif dan == 5:
    print("Friday")
elif dan == 6:
    print("Saturday")
elif dan == 7:
    print("Sunday")
else:
    print("Error")