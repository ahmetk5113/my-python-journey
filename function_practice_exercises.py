# 1:
# warmup questions
def lesser_of_two_evens(a,b):
    if a%2==0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
# 2:
print('')
def animal_crackers(text1,text2):
    if text1[0] == text2[0]:
        return True
    else:
        return False
print(animal_crackers('lool','lil'))

# 3:
print('')
def makes_twenty(num1,num2):
    if sum((num1,num2)) == 20:
        return True
    elif num1 == 20 or num2 == 20:
        return True
    else:
        return False
print(makes_twenty(20,13))
print(makes_twenty(12,8))
print(makes_twenty(3,4))

# i did all of them right up to here
# yaayyyy

# level 1 problems:
print('')
def old_macdonald(string):
    if len(string) > 3:
        return string[:3].capitalize() + string[3:].capitalize()
    else:
        pass

print(old_macdonald('macdonald'))
# MASTER YODA:
def master_yoda(text3):
    return ''.join(text3.split()[::-1])
# soo that basically splits text 3 reorders them from back and sticks them together in an empty string
print(master_yoda('hi guys bro'))

