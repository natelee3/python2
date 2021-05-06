#Positive Numbers II
#Create a list of numbers, 
# Create a new list of each number in the list that is greater than 0

simple_list = [3, 4, 5, -455, -7, .5]
new_list = []

for num in simple_list:
    if num > 0:
        new_list.append(num)

print(new_list)