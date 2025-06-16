"""There are n integers in the range [1...1000]. Of these, some percent p1 are below 200, another percent p2
are from 200 to 399, another percent p3 are from 400 to 599, another percent p4 are from 600 to 799 and the remaining
p5 percent are from 800 upwards. Write a program that calculates and prints the percentages p1, p2, p3, p4, and p5."""

n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(1, n + 1):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2+=1
    elif 400 <= num <= 599:
        p3+=1
    elif 600 <= num <= 799:
        p4 += 1
    else:
        p5 +=1

procenta_p1 = p1/n * 100
procenta_p2 = p2/n * 100
procenta_p3 = p3/n * 100
procenta_p4 = p4/n * 100
procenta_p5 = p5/n * 100

print(f"{procenta_p1:.2f}%")
print(f"{procenta_p2:.2f}%")
print(f"{procenta_p3:.2f}%")
print(f"{procenta_p4:.2f}%")
print(f"{procenta_p5:.2f}%")
