import math

# h ** 2 = c ** 2 + c ** 2
opposite_side = float(input('Enter the opposite side value: '))
adjacent_side = float(input('Enter the adjacent side value: '))

hypotenuse = math.hypot(opposite_side, adjacent_side)

print(f'The hypotenuse value is: {hypotenuse:.2f}')
