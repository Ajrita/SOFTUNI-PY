"""A company boss notices that more and more employees are spending time on sites that distract them.
To prevent this, he introduces surprise checks on his employees' opened browser tabs.
According to the opened tab site, the following fines are applied:
⦁	"Facebook" -> 150 USD
⦁	"Instagram" -> 100 USD
⦁	"Reddit" -> 50 USD
Two lines are read from the console:
⦁	The number of tabs opened in the browser n – an integer in the range [1...10]
⦁	Salary – an integer in the range [500...1500]
⦁   Then n - number of times the website name is read – string.
Input Data
If during the check the salary becomes less than or equal to 0 USD, the console displays "You have lost your
salary." and the program ends. Otherwise, after the check, the console displays the remainder of the salary (to be
displayed as an integer)."""

broj_tabova = int(input())
plata = float(input())

for i in range (broj_tabova):
    imena_stranica = input()
    if imena_stranica == "Facebook":
        plata -= 150
    if imena_stranica == "Instagram":
        plata -= 100
    if imena_stranica == "Reddit":
        plata -= 50
    if plata <= 0:
        print("You have lost your salary.")
        break
if plata > 0:
    print(f"{plata:.0f}")
