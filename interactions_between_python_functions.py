# **interaction between python functions**
# typically a python script or notebook contains several functions interracting with eachother
# lets create a few functions to mimic  the carnival guessing game (the three cup game)
# lets first learn how to  use the shuffle method using the random odule that is  already built in python
from random import shuffle
example = [1,2,3,4,5,6,7]
shuffle(example)
# print(example)
# everytime it gives them in a different order
# lets start creating our game
# did you realise that the suffle method doesnt return anything
# so we need to make a function that return the values
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

result = shuffle_list(example)
print(result)
my_list = ['','0','']
print(shuffle_list(my_list)) # everytime we run it it puts 0 in a  different position

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('pick a number 0,1,2: ')
    return int(guess)

player_guess()
