"""An integer is given - the starting number of points. Bonus points are added to it according
 to the rules described below. Write a program that calculates the bonus points received by the
 number and the total number of points (number + bonus).
⦁	If the number is up to 100 inclusive, the bonus points are 5.
⦁	If the number is greater than 100, the bonus points are 20% of the number.
⦁	If the number is greater than 1000, the bonus points are 10% of the number.

⦁	Additional bonus points (added separately from the previous ones):
⦁	For an even number  + 1 point.
⦁	For a number ending in 5  + 2 points."""

broj = int(input())
bonus = 0
if broj <= 100:
    bonus = 5
elif 100 < broj < 1000:
    bonus = broj * 0.2
elif broj > 1000:
    bonus = broj * 0.1
if broj % 2 == 0:
    bonus += 1
if broj % 5 == 0 and broj % 10 !=0:
    bonus += 2
print(bonus)
print(broj+bonus)