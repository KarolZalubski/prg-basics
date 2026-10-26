###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard1 # your own defined module

# Reads employee's data from keyboard
first_name = keyboard1.input_string('Enter name: ')
last_name = input('Enter last name: ')
age = keyboard1.input_integer('Enter your age: ')
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

