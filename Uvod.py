#int
a = 5
while a <= 10:
    print("a = " + str (a))
    a += 1

#string
line = input()
while line != "Stop":
    print("Loop")
    line = input()

#beskonačna petlja, int
b = 5
while True:
    if b > 10:
        break
    print("b = " + str(b))
    b += 1

#beskonačna petlja, string
while True:
    line = input()
    if line == "Stop":
        break
    print ("Loop")