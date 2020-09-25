import time 
import random
from decimal import Decimal
import math
score = 0
lives = 5
level_cleared = False
level2_cleared = False
Dead = False
lvl = 1
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
Num1 = random.randint(0, 2356)
Num2 = random.randint(0, 3457)
ops = random.choice(Operations)
    
  
while True:
    answer = round(eval(str(Num1) + ops + str(Num2)),2)
    ##print (answer) for debugging
    question = (str(Num1)+ ' ' + ops + ' ' + str(Num2))
    User_Answer = input("Question"+ str(lvl)+': '+str(question)+ ': ')
    try:
        User_Answer = float(User_Answer)
        if lives <= 0:
            Dead = True
            break
        if score == 1:
            level_cleared = True
            break
    except:
        pass
    if User_Answer == (round(answer, 2)):
        print("Correct!")
        lvl = lvl + 1
        score = score + 1
        Num1 = random.randint(0, 2356)
        Num2 = random.randint(0, 3457)
        ops = random.choice(Operations)
        pass
    else:
        print("Wrong answer!")
        lives = lives - 1
        Num1 = random.randint(0, 2356)
        Num2 = random.randint(0, 3457)
        ops = random.choice(Operations)
    
if level_cleared == True:
    Num1 = random.randint(0, 2356)
    Num2 = random.randint(0, 3457)
    while True:
        answer = math.sqrt(Num1)
        answer2 = math.sqrt(Num2)
        question = (str(u"\u221a") + str(Num1)+ '+' + str(u"\u221a")+ str(Num2))
        final_answer = round((answer + answer2),2)
        ##print (final_answer) for debugging
        User_Answer2 = input("Question"+ str(lvl)+': '+str(question)+ ': ')
        try:
            User_Answer2 = float(User_Answer2)
            if lives <= 0:
                Dead = True
                break
            if score == 5:
                level_cleared2 = True
                break
        except:
            pass
        if User_Answer2 == final_answer:
            print("Correct!")
            lvl = lvl + 1
            score = score + 1
            Num1 = random.randint(0, 2356)
            Num2 = random.randint(0, 3457)
        else:
            print("Wrong answer!")
            lives = lives - 1
            Num1 = random.randint(0, 2356)
            Num2 = random.randint(0, 3457)


if Dead == True:
    f = open("Leaderboard.txt", "a+")
    f.write(' Name:'+ str(Player_Name)+ ' score:'+ str(score)+ ' lives:'+ str(lives)+ '\n')
    f.close()
    f = open('Leaderboard.txt', 'r')
    leaderboard = [line.replace('\n','') for line in f.readlines()]


    for i in leaderboard:
        print(i)


