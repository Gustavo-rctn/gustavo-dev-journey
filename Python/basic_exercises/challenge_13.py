current_salary = float(input('What is your current salary?'))
percentage_increase = float(input('what is percentage increase?'))
calculation = current_salary * (percentage_increase / 100)
new_salary = current_salary + calculation
print(f'your salary increase in {calculation} and your new salary is {new_salary}')
