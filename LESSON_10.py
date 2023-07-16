#1. Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. To each file append a random number between 1 and 100.
# Create a summary file (summary.txt) that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98
import string, random, os


for letter in string.ascii_uppercase:
    with open('LESSON_10/' + letter + ".txt", "w") as filename:
        line = str(random.randint(1, 100))
        filename.write(line)
directory = 'LESSON_10'
list_of_files = sorted(filter(lambda x: os.path.isfile(os.path.join(directory, x)),
                        os.listdir(directory)))
with open('summary.txt', "w", encoding="utf-8") as file_sum:
    for files in list_of_files:
        file_sum.write(files)
        file_sum.write(": ")
        with open('LESSON_10/' + files, "r") as file_1:
            for line in file_1:
                file_sum.write(line)
        file_sum.write("\n")

# 2.Create a file with some content.Create a second file and copy the content of the first file to the second file in upper case.

import os

fil_2 = open("my_file.txt", "w")
fil_2.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n"
            "sed do eiusmod tempor incididunt ut labore et dolore magna\n"
            "aliqua. Ut enim ad minim veniam, quis nostrud exercitation\n"
            "ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis\n"
            "aute irure dolor in reprehenderit in voluptate velit esse cillum\n"
            "dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat\n"
            "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
fil_2.close()
with open("new_file.txt", "w") as file:
    fil_2 = open("my_file.txt", "r")
    text = fil_2.read()
    file.write(text.upper())
file.close()

#3.Write a program that will simulate user scores in a game.
# Create a list with 5 players’ names after that simulate 100
# rounds for each player. As a result of the game create a list
# with the player's name and score (0-1000 range). And save it to
# a CSV file.The file should look like this:
# Josh, 56
# Luke, 784
# Kate, 90
# Mark, 125
# Mary, 877
# Josh, 345

import csv, random

players = [['Josh'], ['Luke'], ['Kate'], ['Mark'], ['Mary']]
score = 0
for i in players:
    for roun in range(100):
        score += random.randint(0, 1000)
    players[players.index(i)].append(score)

with open('players.csv', "w", encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])
    for play in players:
        writer.writerow(play)

# 4. Write a script that reads the data from the previous CSV file and creates a new file called high_scores.csv where each row contains the player name and their highest score. The final score should be sorted by descending to the highest score.
# The output CSV file should look like this:
# Player name, Highest score
# Kate, 907
# Mary, 897
# Luke, 784
# Mark, 725
# Josh, 345


import csv, operator

reader = csv.reader(open("players.csv"))
sortedlist = sorted(reader, key=lambda row: row[1], reverse=True)
with open('high_scores.csv', "w", encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Highest score'])
    for play in sortedlist[1:]:
        writer.writerow(play)