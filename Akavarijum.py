"""For his birthday, Steven received an aquarium in the shape of a parallelepiped.
Initially, we read from the console in separate rows its dimensions - length, width,
and height in centimeters. It is necessary to calculate how many liters of water the aquarium
will collect if it is known that a certain percentage of its capacity is occupied by sand, plants, heater, and pump.
One liter of water is equal to one cubic decimeter / 1l = 1 dm3 /.
Write a program that calculates the liters of water needed to fill the aquarium.
Input Data
4 lines are read from the console:
⦁	Length in cm – an integer in the interval [10 … 500]
⦁	Width in cm – an integer in the interval [10 … 300]
⦁	Height in cm – an integer in the interval [10… 200]
⦁	Percentage – a floating-point number in the interval [0.000 … 100.000]
Output Data
Print a number on the console:
⦁	liters of water, that the aquarium contains. """

dužina = int(input())
širina = int(input())
visina = int(input())
postotak_zauzeća = float(input())/100
zapremina = dužina * širina * visina
litraža = zapremina * 0.001
zaokupljeno = litraža - (litraža * postotak_zauzeća )
voda = litraža * (1-postotak_zauzeća)
print(voda)