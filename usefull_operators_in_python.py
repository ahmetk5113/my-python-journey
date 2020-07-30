# ** usefull operatrors**
# range() function
my_list = [1,2,3]
for items in range(10): # we can add a start point a step size and an end
    print(items)

# lets try that out
print('')
print('')
my_lol = [2,4,9]
for num in range(0,100,10): #step size is at the end and the end is in the middle
    print(num)


# enumarate method
# basically enumerate method gives us the index position and the result in the for loop
# example:
word = 'abcde'
for item in enumerate(word):
    print(item)

# we can also do tuple unpacking if we want to get indexes and letters seperately
# example:
word2 = 'abcdef'
for index,letter in enumerate(word2):
    print(index)
# which will only print out 0,1,2,3,4,5
# lets only get the letter
word2 = 'abcdef'
for index,letter in enumerate(word2):
    print(letter)
# this only prints out a\n,b\n,c\n,d\n,e\n,f\n
# or simply a,b,c,d,e,f
# zip function
# its zips two lists together
list_num = [1,2,3]
list_letters = ['a', 'b', 'c']
for items in zip(list_num,list_letters):
    print(items)
# in this way it prints out:
# (1, 'a')
# (2, 'b')
# (3, 'c')
# but we can use tuple unpacking to solve this problem we can print them out seperately
my_jeez1 = [1,2,3]
my_jeez2 = ['a','b','c']
for index,items2 in zip(my_jeez1,my_jeez2):
    print(index) # now i can print out 1 2 3 seperately
    print(items2) # and a b c
# **in operator**
# it helps us see whether the object specified is in the list or dictionary or a string
print('x' in [1,2,3])
# it prints out False because there are no 'x''s in the [1,2,3]
# lets try an example with dictionary
d = {'lol':245}
print(245 in d.values()) # it prints out true because the value in d is 245
# min max functions that gives us the minimum and maximum values in a list:
my_list2 = [10,20,30,100]
print(min(my_list2)) # it prints out 10 because 10 is the smallest value
# lets try max:
print(max(my_list2)) # it prints out 100 because 100 is  the greatest value
# **random library**
from random import shuffle
listss = [1,2,3,4,5,6,7,8,9,10]
shuffle(listss)
print(listss) # it randomises the placement of the numbers
# we can also use randint to get random integers
from random import randint
print(randint(1,100)) # wee basically give two parameters first one is the starting point and the last one is the end point
# because it returns something we can set a variable to it
random_numbers = randint(0,100)

# **input function**
# example:
input('enter a word: ')
# we can set this to variable
result = input('whats your name?: ')
