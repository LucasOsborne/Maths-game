#imports all the modules needed
import time 
import random
from decimal import Decimal
import math
score = 0
score1 = 0
lives = 3
level_cleared = False
level_cleared2 = False
level_cleared3 = False
level_cleared4 = False
Win = False
Dead = False
lvl = 1
Operations = ["*" , "+" , "-" , "/"]#operators in a list for a random script
Player_Name = input("WELCOME to my maths game please enter your name: ")#player name
time.sleep(1)
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
#prints out the rules
print("""Here are the rules:
   1. DO maths thats all just maths please
   2. Any decimals are rounded to 2 d.p
   3. There are negative numbers
   4. You can use a calculator\n""")
Num1 = random.randint(0, 2356)#selects random number 0 - 2356
Num2 = random.randint(0, 3457)#selects random number 0 - 3457
ops = random.choice(Operations)#selects random operator
while True:
    answer = round(eval(str(Num1) + ops + str(Num2)),2)#This evaluates Num1 with a random operatior with Num2 
    if Player_Name == 'debug':
        print (answer) #for debugging
    question = (str(Num1)+ ' ' + ops + ' ' + str(Num2))
    User_Answer = input("Question"+ str(lvl)+': '+str(question)+ ': ')#gets user input
    try:
        User_Answer = float(User_Answer)
        #checks if they are alive
        if lives <= 0:
            Dead = True
            break
        #script that checks what level they are on
        if lvl ==17:
            level_cleared = True
            break
    except:
        pass
    if User_Answer == (round(answer, 2)):
        print("Correct!")
        lvl = lvl + 1
        score = score + 1
        Num1 = random.randint(0, 2356)#selects random number
        Num2 = random.randint(0, 3457)#selects random number
        ops = random.choice(Operations)#selects random operator
    else:
        print("Wrong answer!")
        lvl = lvl + 1
        lives = lives - 1
        score1 = score1 + 1
        Num1 = random.randint(0, 2356)#selects random number
        Num2 = random.randint(0, 3457)#selects random number
        ops = random.choice(Operations)#selects random operator
    
if level_cleared == True:#actives the script 
    Num1 = random.randint(0, 2356)
    Num2 = random.randint(0, 3457)
    while True:
        answer = math.sqrt(Num1)
        answer2 = math.sqrt(Num2)
        question = (str(u"\u221a") + str(Num1) + '+' + str(u"\u221a") + str(Num2))
        final_answer = round((answer + answer2),2)
        if Player_Name == 'debug':
            print (final_answer) ##for debugging
        User_Answer2 = input("Question"+ str(lvl) +': '+ str(question) + ': ')#gets user input
        try:
            User_Answer2 = float(User_Answer2)
            #checks if they are alive
            if lives <= 0:
                Dead = True
                break
            #script that checks what level they are on
            if lvl == 27:
                level_cleared2 = True
                break
        except:
            pass
        if User_Answer2 == final_answer:
            print("Correct!")
            lvl = lvl + 1
            score = score + 1
            Num1 = random.randint(0, 2356)#selects random number
            Num2 = random.randint(0, 3457)#selects random number
        else:
            print("Wrong answer!")
            lvl = lvl + 1
            lives = lives - 1
            score1 = score1 + 1
            Num1 = random.randint(0, 2356)#selects random number
            Num2 = random.randint(0, 3457)#selects random number

if level_cleared2 == True:#actives the script 
    Num1 = random.randint(0, 2356)#selects random number
    Num2 = random.randint(0, 3457)#selects random number
    Num3 = random.randint(0, 60)#selects random number
    Num4 = random.randint(0, 76)#selects random number
    while True:
        final_answer = round((Num3 / Num4*Num2 + Num1),2)
        if Player_Name == 'debug':
            print (final_answer) #for debugging
        question = (str(Num3) + '÷' + str(Num4) + '(' + str(Num2) + '+' + str(Num1) + ')')
        User_Answer3 = input("Question"+ str(lvl) +': '+ str(question) + ': ')#gets user input
        try:
            User_Answer3 = float(User_Answer3)
            #checks if they are alive
            if lives <= 0:
                Dead = True
                break
            #script that checks what level they are on
            if lvl == 37:
                level_cleared3 = True
                break
        except:
            pass
        if User_Answer3 == final_answer:
            print("Correct!")
            lvl = lvl + 1
            score = score + 1
            Num1 = random.randint(0, 2356)#selects random number
            Num2 = random.randint(0, 3457)#selects random number
            Num3 = random.randint(0, 60)#selects random number
            Num4 = random.randint(0, 76)#selects random number
        else:
            print("Wrong answer!")
            lvl = lvl + 1
            lives = lives - 1
            score1 = score1 + 1
            Num1 = random.randint(0, 2356)#selects random number
            Num2 = random.randint(0, 3457)#selects random number
            Num3 = random.randint(0, 60)#selects random number
            Num4 = random.randint(0, 76)#selects random number

if level_cleared3 == True:#actives the script 
    a = random.randint(0, 2356)#selects random number
    b = random.randint(0, 3457)#selects random number
    ops = random.choice(Operations)#selects random operator
    while True:
        LA1 = a * a
        LA2 = b * b
        final_answer = round(math.sqrt(eval(str(LA1) + ops + str(LA2))),2)#evaluate square roots then rounds 
        question = (str(a) + str(u'\u00b2') + str(ops) + str(b) + str(u'\u00b2'))
        if Player_Name == 'debug':
            print(final_answer) #for debugging
        User_Answer4 = input("Question"+ str(lvl)+': '+str(question)+ ': ')#gets user input
        try:
            User_Answer4 = float(User_Answer4)
            #checks if they are alive
            if lives <= 0:
                Dead = True
                break
            #script that checks what level they are on
            if lvl >= 50:
                level_cleared4 = True
                break
            #script that checks if they have completed all the levels then calculates their final score
            if level_cleared and level_cleared2 and level_cleared3 and level_cleared4 == True:
                score = score - score1
                Win = True
                break
        except:
            pass
        if User_Answer4 == final_answer:
            print("Correct!")
            lvl = lvl + 1
            score = score + 1
            a = random.randint(0, 2356)#selects random number
            b = random.randint(0, 3457)#selects random number
            ops = random.choice(Operations)#selects random operator
        else:
            print("Wrong answer!")
            lvl = lvl + 1
            lives = lives - 1
            score1 = score1 + 1
            a = random.randint(0, 2356)#selects random number
            b = random.randint(0, 3457)#selects random number
            ops = random.choice(Operations)#selects random operator

if Dead == True:
    #script that writes to a leaderboard.txt then prints it out
    score = score - score1
    f = open("leaderboard.txt", "a")
    f.write("Name: "+ str(Player_Name) + "score: " + str(score) + "\n")
    f.close()

    #open and read the file after the appending:
    f = open("leaderboard.txt", "r")
    print(f.read())
    f.close()
    print(str("welldone") + str(Player_Name) + ("you got ")+ str(score) + str("\50"))
if Win == True:
    #script that writes to a leaderboard.txt then prints it out
    score = score - score1
    f = open("leaderboard.txt", "a")
    f.write("Name: "+ str(Player_Name) + "score: " + str(score) + "\n")
    f.close()

    #open and read the file after the appending:
    f = open("leaderboard.txt", "r")
    print(f.read())
    f.close()
    print(str("welldone") + str(Player_Name) + ("you got ")+ str(score) + str("\50"))