personel_fee = [('berk',2000),('arda',600000),('ahmet',500000000)]
def employee_fee_function(personel_fee):
    starting_value = 0
    winner = ''
    for worker,fee in personel_fee:
        if fee > starting_value:
            starting_value = fee
            winner = worker
        else:
            pass
    return (winner,starting_value)
result = employee_fee_function(personel_fee)
print(result)

# lets try a different one
student_grades = [('john',53), ('jack',80), ('ahmet',94), ('elon',100), ('nikola',97)]
def grade_changer(student_grades):
    for student,grades in student_grades:
        if grades[1] == 5 or grades[1] >= 5:
            grades = grades[0] + 1  and grades = grades[1] == 0
        else:
            grades[1] == 0

    return (student, grades)
result2 = grade_changer(student_grades)
print(result2)

