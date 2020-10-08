Player_Name = "barry"
score = 60

f = open("C:\\Users\lucas\Desktop\Maths-game\leaderboard.txt", "a")
f.write("player: " + str(Player_Name) + " score: " + str(score) + "\n")
f.close()

#open and read the file after the appending:
f = open("C:\\Users\lucas\Desktop\Maths-game\leaderboard.txt", "r")
print(f.read())
f.close()