# **tuples subject**
# tuples are very similar to lists.however they have one significant difference: IMMUTABILITY
# once an element is inside a tuple it can not be assigned again
# tuples use parenthesis: (1,2,3)
t = (1, 2, 3)
my_list = [1,2,3]
print(type(t))
# .count() method helps us count how many times that element has been used
# example:
b = ("a","a","c")
print(b.count("a")) # it gives a result of 2 because we used a 2 times
# index() method gives us the very first time the sellected ellement occurs in the tuple
# example:
print(b.index("c")) # it gives us the index position of two bbecause it is the first place that ellemnt c was found in

