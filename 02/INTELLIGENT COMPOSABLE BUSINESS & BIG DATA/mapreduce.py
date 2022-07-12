# Para manter a compatibilidade com Python 3
# e necessaria a importacao de __future__.print_function
# para o uso de print().
from __future__ import print_function
import sys
from map import map
from reduce import reduce

# Lendo arquivo de STDIN.
entrada = sys.stdin

# Esse trecho de codigo nao precisaria existir
# substituir resultados.append() por print() seria
# mais eficiente, pois nao seria necessario a criacao
# de outra lista e o envio de linhas para STDOUT
# ele so existe para possivel reciclagem de codigo
# na funcao reduce().
for linha in reduce(map(entrada)):
    print(linha.replace("\n", ""))
    # print() enviara as linhas para STDOUT.

    # O metodo replace('\n', '') e necessario
    # para reverter a formatacao de reduce().
