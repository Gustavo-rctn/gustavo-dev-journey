import random

student_1 = input('Enter the first student\'s name: ')
student_2 = input('Enter the second student\'s name: ')
student_3 = input('Enter the third student\'s name: ')
student_4 = input('Enter the fourth student\'s name: ')

students = [student_1, student_2, student_3, student_4]

# Shuffling and unpacking the presentation order
first, second, third, fourth = random.sample(students, k=4)


print(f'The first student selected is: {first}')
print(f'The second student selected is: {second}')
print(f'The third student selected is: {third}')
print(f'The fourth student selected is: {fourth}')
