print('hello, world!') #it shows 'hello, world!'

print(7+4) #adds two numbers

print('7' + '4') #it shows 7 and 4, but together

print('7', '4') #it shows 7 and 4, but with a space between the two

print('hello', 5)

#   ----------------------------------------------------//--------------------------------------------------------------

name = 'Reis'
age = 16
weight = 65
print(name, age, weight)
#                                                 ----//----
name = 'Vasconcelos'
age = 43
weight = 109
print(name, age, weight)
#                                               ----//----
name = 'Gustavo'
age = 16
weight = 65
person = name, age, weight
print(person)
#                                               ----//----


name = input('What is your name?')
age = int(input('How old are you?'))
weight = int(input('What is your weight?'))
person = name, age, weight
print(name, age, weight)
#                                              ----//----
name = input('what is your name?')
age = int(input('How old are you?'))
weight = int(input('What is your weight?'))
person = name, age, weight
print(person)

#=======================================================================================================================
n = input('digite algo:')
print(n.isalpha()) # if it contains only letters / # se contém apenas letras
print(n.isnumeric()) # if it contains only numbers / # se contém apenas números
print(n.isalnum()) # if it contains only letters and/or numbers / # se contém apenas letras e/ou números
print(n.isidentifier()) # if it is a valid name for variables or functions / # se é um nome válido para variáveis ou funções
print(n.isprintable()) # if the text can be displayed on screen (no line breaks) / # se o texto pode ser exibido na tela (sem quebras de linha)
print(n.isspace()) # if it contains only whitespace / # se contém apenas espaços em branco
print(n.isdecimal()) # if it contains only decimal digits (0 to 9) / # se contém apenas dígitos decimais (0 a 9)

#=============================================arithmetic Operations=====================================================
name = str(input('what is your name?'))
print(f'hello {name:=^20}!')
#=======================================================================================================================
n1 = int(input('what is the first number?'))
n2 = int(input('what is the second number ?'))
print(f'the value is {n1+n2}')
#=======================================================================================================================
frase = 'Curso em Video Python'
print(frase.count('o', 0, 14))
#=======================================================================================================================
frase = '   Curso em Video Python   '
print(len(frase))


