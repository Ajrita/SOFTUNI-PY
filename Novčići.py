"""Vending machine manufacturers wanted to make their machines return as few change coins as possible.
Write a program that receives an amount - the change that needs to be returned and calculates with how few coins
this can be done. The coins can be 2.00 EUR, 1.00 EUR, 0.50 EUR, 0.20 EUR, 0.10 EUR, 0.05 EUR, 0.02 EUR, 0.01 EUR."""

ulog = float(input()) #4.30
ulog = int(ulog * 100) #430
novčići_2 = 0 #2e
novčići_1 = 0 #1e
novčići_050 = 0 #0.50centi
novčići_020 = 0 #0.20 centi
novčići_010 = 0 #0.10 centi
novčići_005 = 0 #0.05 centi
novčići_002 = 0 #0.02 centi
novčići_001 = 0 #0.01 centi

while not ulog == 0:
    if ulog >= 200: #430 >= 200 T
        novčići_2 += ulog // 200 #430 // 200 = 2
        ulog -= novčići_2 * 200 # 430 - 2 * 200 = 30
    if 100 <= ulog < 200:
        novčići_1 += ulog // 100
        ulog -= novčići_1 * 100
    if 50 <= ulog < 100:
        novčići_050 += ulog // 50
        ulog -= novčići_050 * 50
    if 20 <= ulog < 50:
        novčići_020 += ulog // 20
        ulog -= novčići_020 * 20
    if 10 <= ulog < 20:
        novčići_010 += ulog // 10
        ulog -= novčići_010 * 10
    if 5 <= ulog < 10:
        novčići_005 += ulog // 5
        ulog -= novčići_005 * 5
    if 2 <= ulog < 5:
        novčići_002 += ulog // 2
        ulog -= novčići_002 * 2
    if 1 <= ulog < 2:
        novčići_001 += ulog // 1
        ulog -= novčići_001 * 1
print(novčići_2 + novčići_1 + novčići_050 + novčići_020 + novčići_010 + novčići_005 + novčići_002 + novčići_001)