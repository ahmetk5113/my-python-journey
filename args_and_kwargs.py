# *args  and **kwargs topic
# lets say that we want to define a function but did you guys know that we are limited by only being able to
# give 5 parameters?
# so heres what we can do while we are defininng and we put the parameters we can put *(astrix) and args which
# lets us put as much parameters as we like
# lets give it a try
# lets take 10% of the sum of all numbers
def myfunc(*args):
    return sum(args) * 0.1

result = myfunc(100,200,200)
print(result) # sum of those numbers are 500 so 10 percentage is 50
# as printed 50.0
# let me show you guys how it would've been if i didnt use *args:
def myfunc2(a,b,c,d,e,f):
    return sum((a,b,c,d,e)) * 0.1
result2 = myfunc2(10,20,30,40,50,60)
print(result2) # it works now because id didnt put the 6 th parameter
#let  me  show you guys  the error message if ive had the 6 th one
# no errror messages but it didnt use the 6 th one
# it just doesnt count it
# cos the default number for parrameters to be used is  5
# lets assign the variables(values) in the parameter part to 0(default)
# lets give it a try that way and see how it works:
def just_tryin_out_boi(a2=0,b2=0,c2=0,d2=0,e2=0,f2=0):
    return sum((a2,b2,c2,d2,e2,f2)) * 0.1
result3 = just_tryin_out_boi(10,20,30,40,50,60)
print(result3)
# as you guys  can see it works buttt this takes  so long to write and takes extra space and memory
# *args method is way easier to understand and do


# **kwargs
# so basically  while args is used for lists kwargs makes dictionaries
# i didnt understand it good as the args but i hope i will get better at them after practicing
def myfunction(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('ı guess i"ll have some tea')
myfunction(fruit='orange',vegetable='carrot')
# soo as far as i understood kwargs do not give us errors even if we give an undefined parameter
# it also lets us use as many parameters as possible
# and it is used for dictionaries
# another example:
def print_out_stuff(**kwargs):
    for key,value in kwargs.items():
        print('hello i go to {} and my name is {}'.format(key,value))
print_out_stuff(
    american_academy='suna',
    turk_maarif_kooleji='Ahmet',
    yakın_dogu='berk')

# HUGEEEE REMINDER!!!!!! while using kwargs after defining function and giving values we must give them in
# key value pairs as shown above
# btw output is:
# hello i go to american_academy and my name is suna
# hello i go to turk_maarif_kooleji and my name is Ahmet
# hello i go to yakın_dogu and my name is berk
# **kwargs return dictionaries
# lets use *args and **kwargs in one example:
def args_and_kwargsss(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i would like {} {}'.format(args[0],kwargs['food']))
args_and_kwargsss(10,20,30,food='eggs',vegetables='lettuce') # idk if you guys realised this but it doesnt give any errors to undefined stuff while using **kwargs
# out: i would like 10 eggs
# out: {'food': 'eggs', 'vegetables': 'lettuce'}
# sooo as far as you guys can see args only took the number in index 1
# and kwargs took the food key which s value was eggs
