"""Write a program with which Michael solves problems from his exams until he receives the "Enough" command
from his lecturer. For each problem he solves, he receives a grade. The program should finish when receiving the
"Enough" command or if Michael receives the specified number of poor grades.
A poor grade is any grade that is less than or equal to 4.
Input Data
⦁	On the first line - number of poor grades – an integer;
⦁	Then multiple readings of two lines:
⦁	Problem name – string
⦁	Grade – an integer in the range [2…6]
Output Data
⦁	If Michael receives the "Enough" command, print on 3 lines:
⦁	"Average score: {average score}"
⦁	"Number of problems: {number of all problems}"
⦁	"Last problem: {last problem name}"
⦁	If he receives the specified number of poor grades:
⦁	"You need a break, {number of poor grades} poor grades."
The average score must be formatted to two digits after the decimal point. """

allowed_poor_grades = int(input())
problem_name = "" #dodelićemo vrednost kasnije kroz input
grade = 0 #dodelićemo vrednost kasnije kroz input
gotten_poor_grade = 0
score = 0.00
number_of_problems = 0
last_problem = ""

while problem_name != "Enough" or gotten_poor_grade < allowed_poor_grades:
    problem_name = input()

    if problem_name == "Enough":
        print(f"Average score: {score/number_of_problems:.2f}\nNumber of problems: {number_of_problems}\nLast problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        gotten_poor_grade += 1

    if gotten_poor_grade == allowed_poor_grades:
        print(f"You need a break, {gotten_poor_grade} poor grades.")
        break
    last_problem = problem_name
    score += grade
    number_of_problems += 1


