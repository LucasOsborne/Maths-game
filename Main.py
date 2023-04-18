import time
import random
import math

score = 0
score1 = 0
lives = 3
lvl = 1
Operations = ["*", "+", "-", "/"]
Player_Name = input("WELCOME to my maths game, please enter your name: ")
leaderboard = []

while True:
    start_game = input("Press Enter to start")
    if start_game == "":
        break
    print("That's not Enter!")
    time.sleep(1)

# Level clearance flags
level_cleared = [False] * 4
Win = False
Dead = False

print("""Here are the rules: 
   1. Any decimals are rounded to 2 d.p.
   2. There are negative numbers.
   3. You can use a calculator.\n""")


def generate_question():
    num1 = random.randint(0, 2356)
    num2 = random.randint(0, 3457)
    op = random.choice(Operations)
    answer = round(eval(str(num1) + op + str(num2)), 2)
    return num1, num2, op, answer


def level_1():
    global lvl, score, score1, lives, Dead, level_cleared
    num1, num2, op, answer = generate_question()
    while True:
        question = f"Question {lvl}: {num1} {op} {num2}"
        user_answer = input(question + ": ")
        try:
            user_answer = float(user_answer)
        except ValueError:
            continue
        if user_answer == answer:
            print("Correct!")
            lvl += 1
            score += 1
            num1, num2, op, answer = generate_question()
            if lvl == 17:
                level_cleared[0] = True
                break
        else:
            print("Wrong answer!")
            lvl += 1
            lives -= 1
            score1 += 1
            num1, num2, op, answer = generate_question()
            if lives <= 0:
                Dead = True
                break


def level_2():

    global lvl, score, score1, lives, Dead, level_cleared
    num1, num2 = random.randint(0, 2356), random.randint(0, 3457)
    while True:
        answer = round((math.sqrt(num1) + math.sqrt(num2)), 2)
        question = f"Question {lvl}: √{num1} + √{num2}"
        user_answer = input(question + ": ")
        try:
            user_answer = float(user_answer)
        except ValueError:
            continue
        if user_answer == answer:
            print("Correct!")
            lvl += 1
            score += 1
            num1, num2 = random.randint(0, 2356), random.randint(0, 3457)
            if lvl == 34:
                level_cleared[1] = True
                break
        else:
            print("Wrong answer!")
            lvl += 1
            lives -= 1
            score1 += 1
            num1, num2 = random.randint(0, 2356), random.randint(0, 3457)
            if lives <= 0:
                Dead = True
                break


def level_3():

    global lvl, score, score1, lives, Dead, level_cleared
    num1, num2, op, answer = generate_question()
    while True:
        question = f"Question {lvl}: {num1} {op} {num2}"
        user_answer = input(question + ": ")
        try:
            user_answer = float(user_answer)
        except ValueError:
            continue
        if user_answer == answer:
            print("Correct!")
            lvl += 1
            score += 1
            num1, num2, op, answer = generate_question()
            if lvl == 51:
                level_cleared[2] = True
                break
        else:
            print("Wrong answer!")
            lvl += 1
            lives -= 1
            score1 += 1
            num1, num2, op, answer = generate_question()
            if lives <= 0:
                Dead = True
                break


def level_4():

    global lvl, score, score1, lives, Dead, level_cleared
    num1, num2, op, answer = generate_question()
    while True:
        question = f"Question {lvl}: {num1} {op} {num2}"
        user_answer = input(question + ": ")
        try:
            user_answer = float(user_answer)
        except ValueError:
            continue
        if user_answer == answer:
            print("Correct!")
            lvl += 1
            score += 1
            num1, num2, op, answer = generate_question()
            if lvl == 68:
                level_cleared[3] = True
                break
        else:
            print("Wrong answer!")
            lvl += 1
            lives -= 1
            score1 += 1
            num1, num2, op, answer = generate_question()
            if lives <= 0:
                Dead = True
                break
# Game loop


while not Win and not Dead:
    if not level_cleared[0]:
        level_1()
    if not level_cleared[1]:
        level_2()
    if not level_cleared[2]:
        level_3()
    if not level_cleared[3]:
        level_4()
    # Game over

    if Win:
        print(f"Congratulations, {Player_Name}! You have completed the game!")
    else:
        print(f"Sorry, {Player_Name}, you lost! Better luck next time!")
        # Add score to leaderboard

    leaderboard.append((Player_Name, score))
    # Sort leaderboard by score

    leaderboard.sort(key=lambda x: x[1], reverse=True)
    # Print leaderboard

    print("\n--- Leaderboard ---")
    for i, entry in enumerate(leaderboard):
        print(f"{i+1}. {entry[0]}: {entry[1]} points")
        # Save leaderboard to file

    with open("leaderboard.txt", "w") as file:
        for entry in leaderboard:
            file.write(f"{entry[0]},{entry[1]}\n")
