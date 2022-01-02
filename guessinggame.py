import random
print("Number guessing game")
number = random.randint(0,10)
chances = 0
print("Guess a number from 0-10")
while chances<4:
    guess = int(input("Enter your guess"))
    if guess == number:
        print("Congrats you win!")
        break
    elif guess<number:
        print("Guess higher than ",guess)
    else:
        print("Guess lower than ",guess)
    chances = chances+1
if not chances<4:
    print("YOU LOSE :( The number was ",number)