#Multiply a List
#Create a list of numbers and a single factor
#Create and print a new list multiplying them together


simple_list = [2, 3, 4]
factor = 2
new_list = []

for num in simple_list:
    new_list.append(num * factor)

print(new_list)