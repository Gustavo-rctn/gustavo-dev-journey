import math

number = int(input('Enter a number?'))
double = number * 2
triple = number * 3
with_exponent = number ** (1/2)
square_root = math.sqrt(number)
print(f'Using exponents, the square root is {with_exponent}')
print(f'The double is {double}')
print(f'The triple is {triple}')
print(f'The square root is {square_root: .2f}')