"""Climbers from all over the world gather in groups and mark the next peaks to climb. Depending on the size of the
group, climbers will climb different peaks.
⦁	Group up to 5 people - climb Makalu
⦁	Group of 6 to 12 people - climb Mont Blanc
⦁	Group of 13 to 25 people - climb Kilimanjaro
⦁	Group of 26 to 40 people - climb K2
⦁	Group of 41 or more people - climb Everest
Write a function that calculates the percentage of climbers climbing each peak.
Input Data
A series of numbers are read from the console, each on a separate line:
⦁	On the first line – the number of groups of climbers – an integer in the range [1...1000]
⦁	For each group on a separate line – the number of people in the group - an integer in the range [1...1000]
Output Data
Print 5 lines on the console, each containing a percentage between 0.00% and 100.00% formatted to two digits after
the decimal point:
⦁	First line - the percentage of people climbing Makalu
⦁	Second line - the percentage of people climbing Mont Blanc
⦁	Third line - the percentage of people climbing Kilimanjaro
⦁	Fourth line - the percentage of people climbing K2
⦁	Fifth line - the percentage of people climbing Everest """

broj_grupa = int(input())
makalu = 0
mont_blanc = 0
kilimandžaro = 0
k2 = 0
everest = 0
total_ljudi = 0

for i in range (1, broj_grupa +1):
    broj_ljudi = int(input())
    total_ljudi += broj_ljudi
    if broj_ljudi <= 5:
        makalu += broj_ljudi
    elif 5 < broj_ljudi <= 12:
        mont_blanc += broj_ljudi
    elif 12 < broj_ljudi <= 25:
        kilimandžaro += broj_ljudi
    elif 25< broj_ljudi <= 40:
        k2 += broj_ljudi
    else:
        everest += broj_ljudi

procenat_makalu = makalu/total_ljudi * 100
procenat_mont_blanc = mont_blanc/total_ljudi * 100
procenat_kilimandžaro = kilimandžaro/total_ljudi * 100
procenat_k2 = k2/total_ljudi * 100
procenat_everest = everest/total_ljudi * 100

print(f"{procenat_makalu:.2f}%")
print(f"{procenat_mont_blanc:.2f}%")
print(f"{procenat_kilimandžaro:.2f}%")
print(f"{procenat_k2:.2f}%")
print(f"{procenat_everest:.2f}%")
