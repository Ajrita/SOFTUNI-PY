""""Emma wants to start a healthy lifestyle and has set a goal to walk 10,000 steps every day. However, some days
she is very tired from work and will want to get home before she reaches her goal. Write a program that reads from
the console how many steps she walks each time she goes out during the day, and when she reaches her goal, print
"Goal reached! Good job!" and how many more steps she has walked "{difference between steps} steps over the goal!"
If she wants to go home before then, she will enter the command "Going home" and enter the steps she has walked
while going home. Then, if she has failed to reach her goal, the console should print: "{difference between steps}
more steps to reach the goal." """

action = input() #ili koraci ili komanda "going home"
broj_koraka = 0 #ukupni koraci
dodatni_koraci = 0

while broj_koraka <= 10000:
    if action != "Going home":
        broj_koraka += int(action)
    if action == "Going home":
       dodatni_koraci = int(input())
       broj_koraka += dodatni_koraci

       if broj_koraka < 10000:
            print(f"{10000-broj_koraka} more steps to reach goal.")
            break
       else:
           print(f"Goal reached! Good job!\n{broj_koraka-10000} steps over the goal!")
           break
    if broj_koraka >= 10000:
        print(f"Goal reached! Good job!\n{broj_koraka-10000} steps over the goal!")
        break
    action = input()