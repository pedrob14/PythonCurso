# Ler o salário de um funcionário e mostrar seu novo salário com 15 % de aumento
sal = float(input("Qual é o salário do funcionário? R$ "))
aumento = sal + (sal * 15 / 100)
# salari + o reajuste
print("Um funcionário que ganhava R$ {:.2f}, com 15 % de aumento, passa a receber R$ {:.2f}".format(sal, aumento))