import random
import time

working = True
while working == True:
    lowestNum = int(input("What's the lowest number you want? [in numbers] "))
    highestNum = int(input("What's the highest number you want? [in numbers] "))
    number = random.randint(lowestNum, highestNum)
    guess = int(input("Guess a number between " + str(lowestNum) + " and " + str(highestNum) + " "))

    while guess != number:
        if guess > number:
            print("Wrong. You need to guess lower. Try again.")
            guess = int(input("\nGuess a number between " + str(lowestNum) + " and " + str(highestNum) + " "))
        else:
            print("You need to guess higher. Try again.")
            guess = int(input("\nGuess a number between " + str(lowestNum) + " and " + str(highestNum) + " "))

    print("You guessed! Nice job")

    restart = input("Do you want to play again? [yes/no] ")
    if restart.lower() == "yes":
        working = True
    else:
        print("Goodbye!")
        time.sleep(1)
        working = False
