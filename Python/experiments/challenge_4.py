def add_grade(grade_list, new_grade):
    grade_list.append(new_grade)
    return grade_list

grades = [8.5, 9.8, 4, 7]

new_grade = float(input('Enter the student\'s new grade: '))

updated_grades = add_grade(grades, new_grade)
formatted_grades = ", ".join(f'{grade}' for grade in updated_grades)
average = sum(updated_grades) / len(updated_grades)

print(f'Grade added: {new_grade}\n'
      f'Grades: {formatted_grades}\n'
      f'Average: {average:.1f}')
