import math

width = float(input('Enter the wall width (in meters): '))
height = float(input('Enter the wall height (in meters): '))

area = width * height
paint_needed = area / 2

# Using 'math.ceil' to always round the number of cans up
# Example: 1.2 cans automatically becomes 2 cans, completely avoiding IF/ELSE
cans_needed = math.ceil(paint_needed / 18)

# Fluent and professional display of the final results
print(f'\nWall area: {area:.2f} m²')
print(f'Paint required: {paint_needed:.2f} liters')
print(f'You will need to buy {cans_needed} can(s) of paint (18L each).')
