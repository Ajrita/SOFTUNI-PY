"""Write a program that calculates the student's average grade from all of his/her studies. On the first line,
you will receive the student's name and on each following line his/her annual grades. The student passes to the next
grade if his annual grade is greater than or equal to 4.00. If he/she failed more than once, he/she will be excluded
and the program ends, printing the student's name and the class he/she was excluded from.
At the successful completion of grade 12 to be printed:
"{student's name} graduated. Average grade: {average grade of all studies}"
In the student is excluded from school, to be printed:
"{student's name} has been excluded at {class he/she was excluded from} grade"
The average grade must be formatted to two digits after the decimal point. """

ime = input()
trenutna_ocena = 0.00
brojač_ocena = 0 #sabiramo sve ocene unutar ove promenjive
godina = 1 #brojač za godine školovanja
prosečna_ocena = 0.00
padanje = 0 #brojač, koliko puta je učenik pao razred

while godina <= 12:
    trenutna_ocena = float(input())
    if trenutna_ocena >= 4.00:
        godina += 1
        brojač_ocena +=trenutna_ocena
    else:
        padanje += 1
        if padanje > 1:
            break
prosečna_ocena = brojač_ocena /12
if godina == 13:
    print(f"{ime} graduated. Average grade: {prosečna_ocena:.2f}")
else:
    print(f"{ime} has been excluded at {godina} grade")



