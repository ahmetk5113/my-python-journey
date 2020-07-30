# first question
st = 'Print only the words that start with s in this sentence'
for letter in st.split():
    if letter[0] == 's':
        print(letter)

# second
new_list = []
for numbers in range(0,11):
    new_list.append(numbers)
print(new_list)

# third
new_list2 = [number for number in range(0,51) if number%3==0]
print(new_list2)

# fourth
st2 = 'Print every word in this sentence that has an even number of letters'
for letters in st2.split():
    if len(letters)%2 == 0:
        print(letters)

# fifth
for num in range(0,101):
    if num%3==0:
        print('Fizz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0 and num%5==0:
        print('FizzBuzz')
    else:
        num

# last
st3 = 'Create a list of the first letters of every word in this string'
for letterss in st3.split():
    print(letterss[0])
# just kidding this was the for loop version
lol = [word[0] for word in st3.split()]
print(lol)
# yupp there you go
