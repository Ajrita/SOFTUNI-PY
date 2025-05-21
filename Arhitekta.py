"""Write a program that calculates how many hours it will take an architect
 to prepare the projects on several construction sites. The preparation of
 a project takes three hours.
 2 lines are read from the console:	Name of the architect - text,
 Number of projects to be prepared- integer in the interval [0 … 100]
 Print on the console: "The architect {architect name} will need {needed hours} hours
 to complete {projects count} project/s."
"""

name = input()
projects = int(input())

print(f"The architect {name} will need {projects * 3} hours to complete {projects} project/s.")