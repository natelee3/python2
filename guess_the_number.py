#Chooses a random number between 1 and 10 and gives the user 5 guesses.

import random
#magic_number = random.randint(1,10)
magic_number = 5
print("I am thinking of a number between 1 and 10")
user_input = int(input("What's the number? "))

count = 4

while count > 0:

        count -= 1
        if user_input == magic_number:
            print("Yes! You win!")
            count = 0 #End game
        elif count == 0:
            print("Nope. You are out of guesses!")
        elif user_input < magic_number:
            print(str(user_input) + " is too low.")
            print("You have " + str(count) + " guesses left.")
            user_input = int(input("What's the magic number? "))
        elif user_input > magic_number:
            print(str(user_input) + " is too high.")
            print("You have " + str(count) + " guesses left.")
            user_input = int(input("What's the magic number? "))
        else:
            print("That's not an input I recognize. Try again")
            user_input = int(input("What's the magic number? "))



