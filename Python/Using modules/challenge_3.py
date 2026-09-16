import math

angle = float(input('Enter the angle value: '))

# Converting the angle to radians before calculating trigonometry
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print(f'The sine of angle {angle} is: {sine:.2f}')
print(f'The cosine of angle {angle} is: {cosine:.2f}')
print(f'The tangent of angle {angle} is: {tangent:.2f}')
