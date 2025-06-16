"""Write a program that reads the day of the week (string)
- entered by the user and prints on the console the price of a movie ticket according to the day of the week:"""

day = input().lower()

if day == "monday" or day == "tuesday" or day == "friday":
    print(12)
elif day == "wednesday" or day == "thursday":
    print(14)
elif day == "saturday" or day == "sunday":
    print(16)