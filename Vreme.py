"""Write a program that reads the hour and minutes of the 24-hour day entered by
the user and calculates what time it will be in 15 minutes. Print the result in hours:minutes.
The hours are always between 0 and 23, and the minutes are always between 0 and 59.
The hours are written in one or two digits.
Minutes are always displayed in two digits, with a leading zero when necessary. """

sati = int(input())
minuti = int(input())

dodela_minuta = minuti + 15
ostatak_minuta = dodela_minuta - 60

if dodela_minuta >= 60 and ostatak_minuta < 10 and sati < 23:
    print(f"{sati+1}:0{ostatak_minuta}")
elif dodela_minuta >= 60 and ostatak_minuta < 10 and sati == 23:
    print(f"{0}:0{ostatak_minuta}")
elif dodela_minuta >= 60 and ostatak_minuta >= 10 and sati < 23:
    print(f"{sati+1}:{ostatak_minuta}")
elif dodela_minuta >= 60 and ostatak_minuta >= 10 and sati == 23:
    print(f"{0}:{ostatak_minuta}")
else:
    print(f"{sati}:{dodela_minuta}")

"""
hour= int(input())
minute = int(input())
hours_in_minutes = hours * 60
total_minutes = minutes + hours_in_minutes + 15
final_hour = total_minutes // 60
final_minutes = total_minutes % 60
if final_hour == 24:
final_hour = 0
if final_minutes < 10:
print(f"{final_hour}:0{final_minutes}")
else:
print(f"{final_hour}:{final_minutes}")

"""