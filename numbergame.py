import random

print("Number guessing game")

number = random.randint(1, 100)

print("Guess a number (between 1 and 100):")

chances = 0

while chances < 15:

    
    guess = int(input("Enter your guess:- "))


    if guess == number:

        print("Congratulation YOU WON!!!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances += 1
    
if not chances > 15:
    print("YOU LOSE!!! The number is", number)