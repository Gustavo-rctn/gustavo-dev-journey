name = str(input('what is your name?'))
surname = str(input('what is your surname'))
year_birth = int(input('what year were you born?'))
full_name = name + ' ' + surname
calculation = 2026 - year_birth
print(f'your full name is {full_name} and you have {calculation} years old')