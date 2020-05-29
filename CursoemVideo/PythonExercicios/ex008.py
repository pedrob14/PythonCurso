# Um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# km hm dam m dm cm mm
m = float(input("Uma distância em metros: "))
print("A distância de {}m em centimetros é {}cm e em milímetros é de {}mm.".format(m, m * 100, m * 1000))