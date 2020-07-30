new_list = ['one','two','three']
new_list.append('eight')
print(new_list)
# pop function
# pop basically removes the item that is at the end of the list
# we can also asign index positions to the pop function to tell it which term to remove
print(new_list.pop())
print(new_list)

# alphabetical order
# we use the sort method to sort lists into alphabetical order
# example:
old_list = ['a', 'e', 'b', 'c', 'x'] # as you can see we sorted this list to alphabetical order
old_list.sort()
print(old_list)

# reverse method
# as we all expect it will reverse all of the stuff in the list

zero_to_hero = [1, 2, 3, 4]
zero_to_hero.reverse()
print(zero_to_hero)
