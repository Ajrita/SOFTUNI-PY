"""Jessie has decided to raise money for a vacation and wants you to help her find out if she will be able to collect
the required amount. She saves or spends some of her money every day. If she wants to spend more than her available
money, she will spend everything she has and will be left with 0 USD.
Input Data
From the console read:
⦁	Money needed for the vacation – a floating-point number.
⦁	Available money – a floating-point number.
Then 2 lines are read multiple times:
⦁	Action type – text with "spend" and "save" options.
⦁	Amount to save/spend – a floating-point number.
Output Data
The program must end in the following cases:
⦁	If in 5 consecutive days Jessie only spends, the console displays:
⦁	"You can't save the money."
⦁	"{Total days passed}"
⦁	If Jessie collects the money for the vacation, the console displays:
⦁	"You saved the money for {Total days passed} days." """

potreban_novac = float(input())
dostupan_novac = float(input())
dani = 0
trošenje_po_danima = 0

while dostupan_novac < potreban_novac and trošenje_po_danima < 5:
    dani += 1
    akcija = input()
    iznos = float(input()) #iznos potrošenog/sačuvanog novca
    if akcija == "spend":
        dostupan_novac -= iznos
        trošenje_po_danima += 1
        if dostupan_novac < 0:
            dostupan_novac = 0 #vrednost dostupnog novca ne može biti manja od nule
    elif akcija == "save":
        dostupan_novac += iznos
        trošenje_po_danima = 0
    if dostupan_novac >= potreban_novac:
        print(f"You saved the money for {dani} days.")
        break
    if trošenje_po_danima == 5:
        print(f"You can't save the money.\n {dani}")
        break



