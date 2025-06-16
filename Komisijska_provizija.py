"""The company gives the following commissions to its merchants according to the city in which they operate
and the volume of sales:
City	0 ≤ s ≤ 500	500 < s ≤ 1 000	1 000 < s ≤ 10 000	s > 10 000
London	5%	7%	8%	12%
Paris	4.5%	7.5%	10%	13%
Rome	5.5%	8%	12%	14.5%
Write a console program that reads the city name (string) and sales volume (a floating-point number) entered by the user
and calculates the percentage of the trade commission according to the table above. Display the result formatted to 2
digits after the decimal point. In case of invalid city or sales volume (negative number) print "error"."""

grad = input().lower()
obim_prodaje = float(input())
provizija = -1

if grad == "london":
    if 0 <= obim_prodaje <= 500:
        provizija = 0.05 # 5/100 tj. 5%
    elif 500 < obim_prodaje <= 1000:
        provizija = 0.07 # 7/100 tj. 7%
    elif 1000 < obim_prodaje <= 10000:
        provizija = 0.08  # 8/100 tj. 8%
    elif obim_prodaje > 10000:
        provizija = 0.12  # 12/100 tj. 12%
elif grad == "paris":
    if 0 <= obim_prodaje <= 500:
        provizija = 0.045 # 4.5/100 tj. 4.5%
    elif 500 < obim_prodaje <= 1000:
        provizija = 0.075 # 7.5/100 tj. 7.5%
    elif 1000 < obim_prodaje <= 10000:
        provizija = 0.1  # 10/100 tj. 10%
    elif obim_prodaje > 10000:
        provizija = 0.13  # 13/100 tj. 13%
elif grad == "rome":
    if 0 <= obim_prodaje <= 500:
        provizija = 0.055 # 5.5/100 tj. 5.5%
    elif 500 < obim_prodaje <= 1000:
        provizija = 0.08 # 8/100 tj. 8%
    elif 1000 < obim_prodaje <= 10000:
        provizija = 0.12  # 12/100 tj. 12%
    elif obim_prodaje > 10000:
        provizija = 0.145  # 14.5/100 tj. 14.5%


if provizija > 0:
    print(f"{(obim_prodaje * provizija):.2f}")
else:
    print("error")
