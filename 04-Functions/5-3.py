###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard # your own defined module

# Reads employee's data from keyboard
first_name = input('Enter name: ')
last_name = input('Enter last name: ')
age = int(input('Enter your age: '))
salary = int(input('Enter your salary: '))
is_salary_hidden = input('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name}')
print(f'Last name: {last_name}')
print(f'Age: {age}')
if is_salary_hidden == 'y':
    print('Salary is hidden')
elif is_salary_hidden == 'n':
    print(f'Salary: {salary}')

