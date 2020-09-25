import time 
import random

score = 0
lives = 5
level_cleared = False
Operations = ["*" , "+" , "-" , "/"]
Player_Name = input("WELCOME to my maths game please enter your name: ")
while True:
    Start_Game = input("Press enter to start")
    try:
        Start_Game = str(Start_Game)
    except:
        pass
    if Start_Game == "":
        break
    print("Thats not enter!")
time.sleep(1)
print("""Here are the rules:
    DO maths thats all just maths please\n""")

##while True:
Num1 = random.randint(0, 2356)
Num2 = random.randint(0, 3457)
ops = random.choice(Operations)
print (Num1)
print(Num2)
print(ops)
answer = eval(str(Num1) + ops + str(Num2))
print (answer)



