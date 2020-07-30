# list comphrensions area unique way of quicklycreating a list with Python
# if you find yourself using a for loop with .append() to create a list,list comphrensions might be a good alternative
# example:
my_string = 'hello'
my_list = []
for x in my_string:
    my_list.append(x)
print(my_list) # now it prints out ['h', 'e', 'l', 'l', 'o']

# butt that wasnt actually an list comphrension
# in a list comphrension we break down a for loop and make it more simple
# here is an example:
my_string2 = 'lolllll'
my_list2 = [letter for letter in my_string2] # both of those keywords have to match(letter)
print(my_list2)
# soo we basically broke down the for loop
# as far as i understood when we had the for loop we only appended ellements from the string yo the list
# but now we got element from element instead of appending we are getting elements from the string s
# we can also use range function in list comphrension s here's how:
these_lists = [num for num in range(0,10)]
print(these_lists) # now it prints 0 to 10
# we can use if statements in list comphrensions:
look_at_those = [num2 for num2 in range(0,11) if num2%2==0] # this means that print out even numbers that are in range 0  to 11
print(look_at_those) # it prints out [0,2,4,6,8,10] because they are in range 0-11 and they are even
# last examples:
# lets try a celcius to fahrenheit converter expression:
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)* temp + 32)for temp in celcius]
print(fahrenheit)
# lets try nested loops:
mylist = []
for x in [3,5,7]:
    for y in [200,400,600]:
        mylist.append(x*y)
print(mylist)
# it prints out [600, 1200, 1800, 1000, 2000, 3000, 1400, 2800, 4200]
