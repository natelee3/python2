#Takes a string and prints it vertically

print("I can print movie titles vertically.")
title = input("What's your favorite movie? ")
counter = 0

while counter < len(title):
    print(title[counter])
    counter += 1