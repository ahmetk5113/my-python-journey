# Functions with Logic
# soo now i will make a function that checks wheter the number is even or not
def even_check(number1):
    return number1 % 2 == 0
print(even_check(20))
# it prints out True because 20 is an even number
# lets try this with a list:
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
print(check_even_list([1,3,5,7])) # it prints out none here because it is an odd number and it will pass
print(check_even_list([2,4,6])) # it prints out true here because they are even numbers

# now lets make a function that gives false when there is no even number:
def check_even_and_odd(numss):
    for number23 in numss:
        if number23 % 2 == 0:
            return True
        else:
            pass
    return False

# if we have putted the return false to the same indentation as the return true it would only read one line cos the whole for loop wouldnt be runned
# but now it runs the whole loop and and doesnt stop looking for an even number
print(check_even_and_odd([3,1,4]))
# it prints out True
# lets make a function that returns all the even numbers in a list
# first we need to make an empty list to be able to append all the even numbers
empty_list = []
def check_even_list(numba):
    for every_number in numba:
        if every_number % 2 == 0:
            empty_list.append(every_number)
        else:
            pass
    return empty_list
check_even_list([1,2,5,8])
print(empty_list)
