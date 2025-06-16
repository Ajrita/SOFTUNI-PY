"""Write a program that reads two integers (N1 and N2) and an operator with which to perform a mathematical operation
with them. Possible operations are: Addition (+), Subtraction (-), Multiplication (*), Division (/) and Division with
remainder (%). When adding, subtracting, and multiplying the console, the result must be printed and whether it is even
or odd. In ordinary division - the result. In modular division - the remainder. It should be borne in mind that the
divisor can be equal to 0 (zero) and not divisible by zero. In this case, a specific message must be printed.
Input Data
3 rows are read from the console:
⦁	N1 – an integer in the range [0...40 000]
⦁	N2 – an integer in the range [0...40 000]
⦁	Operator – symbol of: "+", "-", "*", "/", "%"
Output Data
On the console print:
⦁	If the operation is addition, subtraction, or multiplication:
⦁	 "{N1} {operator} {N2} = {result} – {even/odd}"
⦁	If the operation is a division:
⦁	"{N1} / {N2} = {result}" – the result is formatted to the second decimal place
⦁	If the operation is division by a remainder:
⦁	"{N1} % {N2} = {remainder}"
⦁	In case of division by 0 (zero):
⦁	"Cannot divide {N1} by zero" """

n1 = int(input())
n2 = int(input())
znak = input()
rezultat = 0.00

if znak == "+":
    rezultat = n1 + n2
    if rezultat % 2 == 0:
        print(f"{n1} {znak} {n2} = {rezultat} - even")
    else:
        print(f"{n1} {znak} {n2} = {rezultat} - odd")
elif znak == "-":
    rezultat = n1 - n2
    if rezultat % 2 == 0:
        print(f"{n1} {znak} {n2} = {rezultat} - even")
    else:
        print(f"{n1} {znak} {n2} = {rezultat} - odd")
elif znak == "*":
    rezultat = n1 * n2
    if rezultat % 2 == 0:
        print(f"{n1} {znak} {n2} = {rezultat} - even")
    else:
        print(f"{n1} {znak} {n2} = {rezultat} - odd")
elif znak == "/" and n2 !=0:
      rezultat =n1/n2
      print(f"{n1} / {n2} = {(rezultat):.2f}")
elif znak == "%" and n2 !=0:
    rezultat = n1 % n2
    print(f"{n1} % {n2} = {rezultat}")
else:
    print(f"Cannot divide {n1} by zero")
