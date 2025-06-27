"""You're invited to a 30th birthday party, where the birthday boy serves a huge cake. However, he doesn't know how
many pieces the guests can take from it. Your task is to write a program that calculates the number of pieces the
guests have taken before it is eaten. You will receive the dimensions of the cake (width and length – integers) and
then on each line until you receive the "STOP" command or until the cake is finished, the number of pieces the guests
take from it. Each piece of cake is 1x1 cm.
Print one of the following lines on the console:
⦁	"{number of pieces} pieces are left." - if you receive STOP and have not finished the cake pieces
⦁	"No more cake left! You need {number of not enough pieces} pieces more." """

width = int(input())
length = int(input())
p = width * length
gosti = 0
less = p > gosti #True

while less:  #Petlja se izvršava dokle god je vrednost promenljive less = True
    taken = input() #Vrednost može biti ili STOP ili br.gostijju
    if taken == "STOP":
        break
    gosti += int(taken)
    if p < gosti:
        less = False
if less:
    print(f"{p-gosti} pieces are left.")
else:
    print(f"No more cake left! You need {gosti-p} pieces more.")