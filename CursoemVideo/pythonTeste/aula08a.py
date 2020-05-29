# floor (arredondar pra baixo), ceil (arredondar pra cima)
import math   # Usando essa importação devo escrever math."o que desejo"
from math import sqrt, ceil  # Assim eu posso usar direto
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print(emoji.emojize("Olá mundo :earth_americas:", use_aliases=True))