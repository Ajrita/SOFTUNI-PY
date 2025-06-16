"""Write a program that checks if the number entered by the user is in the range [-100, 100]
and is different from 0 and print "Yes" if it meets the conditions, or "No" if it is outside the range."""

broj = int(input())

if -100 <= broj <= 100 and broj !=0:
    print("Yes")
else:
    print("No")