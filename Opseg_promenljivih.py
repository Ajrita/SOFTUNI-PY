#Izvršiće se jer je plata inicijalizovana u bloku koda koji se izvršava

current_day = "Monday"
if current_day == "Monday":
    salary= 1000
print(salary)  #1000

#Izvršiće se jer je plata inicijalizovana izvan bloka koda koji se ne izvršava

današnji_dan = "Friday"
isplata =0
if današnji_dan == "Monday":
   isplata = 1000
print(isplata)  #0


#Neće se izvšiti jer je plata inicijalizovana u bloku koda koji se ne izvršava

danas = "Tuesday"
if danas == "Monday":
    plata = 1000
print(plata)  #Error
