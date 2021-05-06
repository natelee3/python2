#Largest Number
#Create a list of numbers and print the largest number.

simple_list = [3, 4, 5, 455, 7, .5]

largest = 0

for num in simple_list:
    if num > largest:
        largest = num
print("The largest number is " + str(largest))

