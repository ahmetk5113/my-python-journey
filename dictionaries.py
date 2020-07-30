# **dictionaries topic**
# dictionaries are unordered mappings for storing objects
# previously we saw how lists store objects in an ordered sequence
# dictionaries use a key-value pairing instead
# dictionaries use curly braces and colons to signify their keys and associated values
# syntax:
# {'key1':'value1':'key2':'value2'}
# so when to choose a list and when to choose a dictionary?

my_dictionary = {'key1':'value1','key2':'value2'}
print(my_dictionary['key1'])
# an example to this could be the market prices of specific items
# such as apples and oranges
# dictionaries use key value pairs so if we give the key it will print us the value
# it is simple as that :)
prices_lookup = {'apple':2.99,'oranges':1.35}
print(prices_lookup['apple'])
# so lets try setting an list or a dictionary in a dictionary
prices_dictionary = {'key1':22,'lol':{'cod':32}}
# this was an example of an dictionary inside a dictionary
print(prices_dictionary['lol']['cod'])
# now i wil show an example of a list in a dictionary
prices_list = {'list1':'i suck','list2':[1, 2, 3]}
print(prices_list['list2'])
# there you go ;)
# a different try
test = {'key13':['hi', ' hello', 'wassup']}
print(test['key13'][0].upper())
# while printing this it didnt let me put a string in the index position so i had to write 0 there representing the first string
test2 = {'key42':[1, 2, 3, 4]}
test2['key42'][1] = 6
print(test2)
# this is also an example to show that we can change  stuff in selected index
# .keys() method gives us  the keys in an dictionary
# .values() method gives us the values in a dictionary
# examples:
print(my_dictionary.keys())
print(prices_lookup.keys())
# as  a reult it gives us:
# dict_keys(['key1', 'key2'])
# dict_keys(['apple', 'oranges'])
# example for values:
print(my_dictionary.values())
print(prices_lookup.values())
# as result it gives us:
# dict_values(['value1', 'value2'])
# dict_values([2.99, 1.35])
# items() gives us the pairings in a  dictionary
# examples:
print(my_dictionary.items())
# which prints out:
# dict_items([('key1', 'value1'), ('key2', 'value2')])
