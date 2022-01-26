# Tien Nguyen
# Section #
# 01/26/2022
# tienn@email.sc.edu
# lab 6 guessing game
import random
a = random.randint(1, 80)
correct = False
guess = 0
for i in range(3):
    key = int(input("Guess a number between 1 and 80: "))
    if key > a:
        print('too high')
        guess += 1
    elif key < a:
        print('too low')
        guess += 1
    else:
        guess += 1
        correct = True
        break
if correct:
    print("Yay you guessed it in {} guesses".format(guess))
else:
    print("Sorry, you only have 3 guesses")
