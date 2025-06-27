"""Write a program that calculates how much total money is in a bank account after making a certain number of deposits.
On each line, you will receive the amount you need to deposit into the account until you receive a "NoMoreMoney"
command. For each amount received, the console should output "Increase: " + the amount and that amount should be added
to the account. If a number less than 0 is received, the console should output "Invalid operation!" and the program
should end. When the program ends, it should print "Total: " + the total amount in the account, formatted to two digits
after the decimal point."""

n = input() #obzirom da input može biti i string "no more money", biramo ovaj tip za unos a posle kastrujemo
suma = 0.0

while n != "NoMoreMoney":
    deposit = float(n)
    if deposit < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {deposit:.2f}")
        suma +=deposit
    n = input()
print(f"Total: {suma:.2f}")