sd = 'hello guys my name is ahmet'
for letter in sd.split():
    print(letter[0])
# there is another way
lol = [letter2[0] for letter2 in sd.split()]
print(lol)
# lets try out some while looops
empty_list = []
for numbers in range(0,100):
    empty_list.append(numbers)
    while numbers > 25:
        print('hell yeah!')

