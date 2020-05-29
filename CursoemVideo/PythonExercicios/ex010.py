# Quanto de dinheiro a pessoa possui na carteira e mostrar na tela quantos dólares ela pode comprar
dinheiro = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = dinheiro / 5.85
print("Com R$ {} você pode comprar US$ {:.2f}".format(dinheiro, dolar))
# ou print("Com R$ {} você pode comprar US$ {:.2f}".format(dinheiro, dinheiro / 3.27))
