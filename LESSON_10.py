# Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. To each file append a random number between 1 and 100.
# Create a summary file (summary.txt) that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)