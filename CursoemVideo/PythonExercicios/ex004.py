a = input('Digite algo: ')
print('O tipo primitivo é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('Ele é um número? ', a.isnumeric())
print('Ele é alfabético?', a.isalpha())
print('Ele é alfanumerico?', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle()) # Quando a palavra está maiuscula e minuscula. Ex: 'Python'