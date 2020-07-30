my_file = open('test.txt')
print(my_file.read())
print(my_file.read())
# when we read the file the cursor goes all the way to the last word
# and we need to reset that
my_file.seek(0)
# to be able to read it again
print(my_file.read())
# if we want to get each line as seperate elements we need to use readlines method
my_file.seek(0)
print(my_file.readlines())
# and it prints out: ['Hello this is a text file\n', 'this is the first line\n', 'this is the second line\n', 'this is the third line\n']
# well that was the old schoolof openning files
# let me show you guys the new way:
# everything we write after that indentation done by colons can use the test.txt file
with open('test.txt') as my_new_file:
    content = my_new_file.read()
print(content)
# the goodthing about using the new way is that we dont have to close the file everytime we are done with them
# when we are done with using files we need to close them to avoid any errors
my_file.close()
# up to now we only read the files but we can also write and overwrite them :)
with open('test.txt', mode='r') as my_new_file: # we can choose the mode of the file wether it is to be read only
    content = my_new_file.read()
# or write and read and write only
# here are the list of commands to change the  mode of the file
# btw w mode overwrites
# here is the list:
# mode='r' is read only
# mode='w' is write only(it overwrites)
# mode='a' is append only(will add on to files)
# mode='r+' is reading and writing
# mode='w+' is writing and reading( overwrites existing files or creates a new file!)
# lets say that we want to make a the mode of a file write only
with open('test.txt', mode='w') as my_new_file:
    content = my_new_file.write('') # the stuff i would write in those quotes would be overwrited on to the test..txt file
# lets say we want to append
with open('test.txt', mode='a') as f:
    f.write('\nLOL')
# soo lets create a not existing file using write mode
with open('test3.txt', mode='w') as f:
    f.write('I HAVE CREATED THIS FILEE')
# python created an another file for me called test3.txt because there was no existing file like that
# lets try something else
# lets try using w+ to make the mode writing and reading
with open('write_and_read.txt', mode='w+') as p:
    p.write('hey watsup')
    p.read()
print(p)
# it was not necessary to print p but i wanted to see what would happen
