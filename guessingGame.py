
import random
print("Number geussing game")
number = random.randint(1,9)
chances = 0
print("Guess a number (between 1 and 9):")

while chances < 5:

    userAnswer = int(input("Enter your guess:-"))


    if userAnswer == number:
        print("Congratulation YOU WON!!!")
        break
        
    elif userAnswer > number:
        print("Your guess was too high: Guess a number lower than", userAnswer)

    else:
        print("Your guess was too low: Guess a number higher than", userAnswer)

    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)