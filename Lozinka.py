"""Write a program that initially reads the username and password of a user profile. Then reads the login password.
⦁	On entering the wrong passwords: prompt the user to enter a new password.
⦁	On entering the correct password: print "Welcome {username}!" and stop execution."""

username = input()
password = input()

while True:
    lozinka = input()
    if lozinka == password:
        break
print(f"Welcome, {username}!")

#čitanje teksta
user = input()
passw = input()
šifra = input()

while šifra != user:
    šifra = input()

print(f"Welcome, {user}!")
