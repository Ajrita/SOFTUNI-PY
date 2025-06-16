"""Write a program that reads a password (string) entered by the user and checks if
the entered password matches the phrase "s3cr3t!P@ssw0rd". In case of coincidence,
display "Welcome". In case of discrepancy, display "Wrong password!".
"""

unos= input()
lozinka = "s3cr3t!P@ssw0rd"

if unos == lozinka:
    print("Welcome")
else:
   print("Wrong password!")