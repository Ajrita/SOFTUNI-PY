"""Write a program that reads user text (string), finishes reading when it receives "Stop" command"""

text = input()
while text != "Stop":
    print(text)
    text = input()

# drugi način
while True:
    txt = input()
    if text == "Stop":
       break
    print(txt)