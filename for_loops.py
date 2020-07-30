my_list = [1,2,3,4,5,6,7,8,9,10]
for lol in my_list:
    print(lol)
print('')
# lets try only printimg out even numbers in the list
for num in my_list:
    # check for even
    if num % 2 == 0: # this means that if we divide it with two and the remainder is zero(which means it will be an even number)
        print(num)
# so ill make somehing that adds each number
print('')
list_sum = 0
for num in my_list:
    list_sum = list_sum + num
    print(list_sum)

# lets try another one using strings in a list
my_string = ['lol', 'man', 'idk']
for stringss in my_string:
    print(stringss)
# lets do with only a string
letter = 'kawai'
for strings in letter:
    print(strings)
# and now it only prinnts them letter by letter
# such as k a w a i
print('')
# fun fact sometimes we dont even need to assign a variable
for lezgo in 'hello world':
    print(lezgo)
# and now it prints h e l l o w o r l d
# ***very important***
# tuple unpacking
# lets say that we want to creates some tuples in a list
my_lil = [(1,2), (2,3), (4,5), (6,7), (8,9)]
for tup in my_lil:
    print(tup)

# this what it printed
#(1, 2)
#(2, 3)
#(4, 5)
#(6, 7)
#(8, 9)
# IF WE WANT TO AVOID THIS:
for a,b in my_lil:
    print(a)
    print(b)
# this is called tuple unpacking
# it makes tuples normal values
# such as:
# 1 2 3
# and lets say we have 3 unpackings
print('')
# example:
my_lil2 = [(1,2,3), (4,5,6), (7,8,9)]
for a,b,c  in my_lil2:
    print(b) # so as you saw i only got 2 5 8 as a result
    # this is  a way to get specific stuff in a for loop using tuple unpacking
d = {'k1':1,'k2':2,'k3':3}
# we can also use the .values() method to do unpacking
for value,key in d.items(): # .items()  gives us the keys
    print(value)# while .values() gives us the values using unpacking
# the thing with .values() method is that only 1  variable should be assigneds
