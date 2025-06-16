dnevnik   = {
    "Petar Petrović": 4.20,
    "Marko Janković": 4.90,
    "Milica Spasić": 5.00,
    "prosek": 4.60,
    5:10, #broj učenika s određenim prosekom
    4:5,
    3:3,
    "IT": ["Marko", "Milica"]
}
print(dnevnik["Petar Petrović"])
print(dnevnik.get("Milica Janković", "Nema ključa"))