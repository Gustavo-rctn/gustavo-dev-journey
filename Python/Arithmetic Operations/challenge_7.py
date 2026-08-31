width = float(input('Enter the wall width (in meters): '))
height = float(input('Enter the wall height (in meters): '))
area = width * height
paint_needed = area / 2
print(f'Your wall area is {area:.2f} m².')
print(f'You will need {paint_needed:.2f} liters of paint to paint it.')
