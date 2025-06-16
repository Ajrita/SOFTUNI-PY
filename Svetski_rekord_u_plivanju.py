"""Oliver decides to break the World Record for long-distance swimming. On the console,
we type: the record that Oliver has to break, the distance in meters he has to swim,
and the time in seconds for which he swims a distance of 1 m. To write a program that calculates
whether he has done the record, it must be considered that: the resistance of the water slows him down
every 15 m by 12.5 seconds. After calculating how many seconds Oliver will slow down, the result should be
rounded down to the nearest integer number. Calculate the time in seconds for which he will swim
the distance and the difference from the World Record.
3 lines are read from the console:
⦁	The records in seconds – a floating-point number in the interval [0.00 … 100000.00]
⦁	The distance in meters – a floating-point number in the interval [0.00 … 100000.00]
⦁	The time in seconds for which he swims 1 meter - a floating-point number in the interval [0.00 … 1000.00]
Printing the console depends on the result:
⦁	If Oliver has broken the World Record (his time is less than the record) we print:
⦁	"Yes, he succeeded! The new world record is {time of Oliver} seconds."
⦁	If he has NOT broken the record (his time is greater than or equal to the record) we print:
⦁	"No, he failed! He was {needed seconds} seconds slower."
The result must be formatted to the second decimal symbol."""
import math
bivši_rekord = float(input())
distanca = float(input())
vreme = float(input())

pređeno = distanca * vreme
otežavanje = (math.floor (distanca/15)) * 12.5
rekord = pređeno + otežavanje

sporiji = rekord - bivši_rekord

if rekord < bivši_rekord:
    print(f"Yes, he succeeded! The new world record is {(rekord):.2f} seconds.")
elif rekord >= bivši_rekord:
    print(f"No, he failed! He was {(sporiji):.2f} seconds slower.")