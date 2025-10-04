#sal =(input("Enter your salary: "))
#sal = int(sal)
#tax=sal*(0.1,0.2)[sal>50000]
#print("Tax to be paid: ",tax)
#print("Tax to be paid: ",tax)
#sysint1 = int(sal)
#sysint1 = sysint1+1
import random
words = ["apple", "key", "mobile", "tiger"]
word1 = random.choice(words)
print(word1)
guess = ""
len1 = len(word1)
disp = ""
choices = 3
for i in range(len1):
    disp = disp + "_"
print(disp)

#print(guess)
corect_letters =[]
game_over = False
lives = 5
while not game_over:
    guess = input("Guess the word: ").lower()
    disp2 = ""
    for c in word1:
        if (c == guess):
            disp2 = disp2 + c
            corect_letters.append(guess)
        elif c in corect_letters:
            disp2 = disp2 + c
        else:
            disp2 = disp2 + "_"
    print(disp2)
    if guess not in word1:
        print("Wrong guess")
        lives = lives - 1
        if lives == 0:
            game_over = True
            print("You have lost the game")
    if "_" not in disp2:
        game_over = True
        print("You have won the game")



    
    
       