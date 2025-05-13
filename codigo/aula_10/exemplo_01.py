# Importar outras bibliotecas com outras funções para o projetos

# Biblioteca para geração de números aleatórios

import random
import os

# n = random.randint(1, 5)
# m = random.randint(1, 5)

# print(n, m)

os.system('cls') # Uso da biblioteca importada = os
# lst_numeros = [random.randint(1, 60) for i in range(6)]
# print(lst_numeros)


# Exemplo 02 - Função

def gerar_numeros(i, f, q):
    lst_num = [random.sample(range(i, f), q)]
    return lst_num

ini = int(input('Informe o primeiro número: '))
fin = int(input('Informe o último número: '))
qtd = int(input('Quantos números? '))

numeros = gerar_numeros(ini, fin, qtd)
print(numeros)
