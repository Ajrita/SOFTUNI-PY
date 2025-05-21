"""Jesse decides he wants to play basketball, but he needs equipment to train.
Write a program that calculates what costs Jesse will have if he starts training,
knowing how much the basketball training fee is for 1 year. Required equipment:
⦁	Basketball sneakers – their price is 40% less than the fee for one year
⦁	Basketball outfit – its price is 20% cheaper than the sneakers
⦁	Ball – its price is 1 / 4 of the price of the outfit
⦁	Basketball Accessories –its price is 1 / 5 of the price of the ball
Input Data
1 line is read from the console:
⦁	The annual fee for basketball training - an integer in the interval [0… 9999]
Output Data
Print on the console how much Jesse will spend if he starts playing basketball. """

članarina = int (input())
patike = članarina - (članarina * 0.4)
dres = patike - (patike *0.2)
lopta = dres/4
dodaci = lopta/5
suma = članarina + patike + dres + lopta + dodaci
print(suma)