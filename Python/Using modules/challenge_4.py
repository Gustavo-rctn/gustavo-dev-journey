import random

student_1 = input('Enter the first student\'s name: ')
student_2 = input('Enter the second student\'s name: ')
student_3 = input('Enter the third student\'s name: ')
student_4 = input('Enter the fourth student\'s name: ')

students = [student_1, student_2, student_3, student_4]
selected_student = random.choice(students)

print(f'The selected student is: {selected_student}')

