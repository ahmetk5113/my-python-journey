x = 0
while x < 5:
    print(f'the current value of x is {x}')
    x = x + 1
else:
    print("x is not less than 5")
# pass example
x = [1,2,3]
for items in x:
    #lol
    pass # does nothing at all
# continue example
my_string = 'sammy'
for items in my_string:
    if items == 'a': # it ignores a
        continue # this makes it not to print letter a
    print(items)
# break example
for item1 in my_string:
    if item1 == 'a': # when it comes to letter a it breks out and doesnt print out rest
        break
    print(item1)

# lets try break method in while loop
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
