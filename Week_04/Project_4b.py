#Project 4b
#Zachary Boelter

#1 Create empty tuple
grocery_list = ()

#2 for loop, 5x, input item, if not in tuple, add to tuple
for i in range(5):
    item = input('Enter item:')
    if item not in grocery_list:
        grocery_list = grocery_list + (item,)

#3 print whole tuple
print(grocery_list)

#4 print items in the tuple one at a time
for item in grocery_list:
    print(item)

#5 Print the first value in the tuple
print(grocery_list[0])

#6 Print the last value in the tuple
print(grocery_list[-1])

#7 print the 2nd and 4th values in the tuple using indexing
print(grocery_list[1])
print(grocery_list[3])

#8 print the 2nd through 4th values in the tuple using slicing
print(grocery_list[1:4])

