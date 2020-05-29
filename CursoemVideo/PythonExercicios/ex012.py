# Ler o preco de um produto e mostrar o novo preco com 5 % de desconto
preco = float(input("Qual é o preço do produto? R$ "))
desc = preco - (preco * 5 / 100)
# preco - o desconto
print("O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}".format(preco, desc))
