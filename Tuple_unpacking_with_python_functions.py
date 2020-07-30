# lets do some tuple unpacking in functions
# i will make an example that decides the employee of the month depending on their working hours
employee_working_hours = [('ahmet',100), ('zehra',200), ('ozan',600)]
def working_hour_checker(employee_working_hours):
    begginning_value = 0
    employee_of_the_month = ''
    for employee,hours in employee_working_hours:
        if hours > begginning_value:
            begginning_value = hours
            employee_of_the_month = employee
        else:
            pass
     # return
    return (employee_of_the_month,begginning_value)
print(working_hour_checker(employee_working_hours))
# it  print out  ('ozan', 600)
# because ozan has the most workinng hours
# what we can also do is  that we can do tuple unpacking while calling a function
# like this:
employee2,hours2 = working_hour_checker(employee_working_hours)
print(employee2)
# as far as you can see it printed out ozan because ozan is  the employee of the month
# lets  see his working hour:
print(hours2) # it  prints out 600 because he worked for 600  hours
