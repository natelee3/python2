#Smallest Number
#Create a list of numbers and print the smallest

simple_list = [3, 4, 5, -455, 7, .5]

smallest = 1e9

for num in simple_list:
    if num < smallest:
        smallest = num
print("The smallest number is " + str(smallest))
