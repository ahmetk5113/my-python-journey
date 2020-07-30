def say_hello():
    print("hello")
# when we are using functions and when we are trying to execute them we need to add parenthesis
# like this:
say_hello()
# lets use functions with f strings:
def say_my_name(name):
    print(f'hello {name}')
say_my_name('ahmet')
# it prints out hello ahmet
# lets try default  values when the required value is not provided
def not_provided(name2 = 'default'):
    print(f'hello {name2}')

not_provided()
# it prints out hello default
# because name2 was not defined(provided)
# lets start using return keyword
# the difference between the print function and return keyword is that return helps us save the result in the function to a new variable
def  add_numbers(num1,num2):
    return num1 + num2
result = add_numbers(10,20)
print(result)
#  lets actually see the difference between return and save by doing examples:
def print_result(a,b):
    print(a + b)

def return_result(a,b):
    return a + b

result2 = print_result(10,20)
print(result2)
# it prints out none because none of the value can be either saved it is only printed out and function is closed
# lets see the type of result2
print(type(result2))
# it prints out <class 'NoneType'>
# because it didnt save any value
#lets try return:
result3 = return_result(10,20)
print(result3)
# now it prints out 30 because return allows us to save the value to a new variable
# lets check the type of result3:
print(type(result3))
# it prints out <class 'int'>
# because the value is saved and a specific value is assigned to result3
