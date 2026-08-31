width = float(input('Enter the wall width (in meters): '))
height = float(input('Enter the wall height (in meters): '))
area = width * height
exact_paint = area / 2
paint_with_margin = exact_paint + (exact_paint * 0.10)
print(f'\nTotal wall area: {area:.2f} m²')
print(f'Exact paint needed: {exact_paint:.2f} liters')
print(f'Paint needed (with a 10% safety margin): {paint_with_margin:.2f} liters')