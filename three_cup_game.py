from random import shuffle
list = [1,2,3,4,5,6]
def shuffler(my_list):
    shuffle(my_list)
    return my_list
result = shuffler(list)
print(result)
my_list = ['','0','']
result2 = shuffler(my_list)
print(result2)

def get_user_input():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("enter a number: 0,1,2")
    return int(guess)
get_user_input()

def check_user(my_list,guess):
    if my_list[guess] == '0':
        print("you're right")
    else:
        print("youre wrong")
        print(my_list)
