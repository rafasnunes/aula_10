# Exercício 01 Versão 2
# Criar uma calculadora que receba dois números e seja capaz de somar, subtrair, multiplicar e dividir
# Alterar a entrada dos números sendo aleatórios e não com entrada do usuário

import random

#Funções do Programa

def calc_soma(n1, n2):
    resultado = n1 + n2
    return resultado


def calc_subt(n1, n2):
    resultado = n1 - n2
    return resultado


def calc_mult(n1, n2):
    resultado = n1 * n2
    return resultado


def calc_div(n1, n2):
    resultado = n1 / n2
    return resultado


# Início do código


num1 = random.randint(1,50)
num2 = random.randint(1,50)

soma = calc_soma(num1, num2)
print(f'Soma de {num1} + {num2} = {soma}') # Teste de impressão com todas as variáveis na saída.

subtracao = calc_subt(num1, num2)
print(f'Subtração: {subtracao}')

multiplicacao = calc_mult(num1, num2)
print(f'Multiplicação: {multiplicacao}')

divisao = calc_div(num1, num2)
print(f'Divisão: {divisao}')
# print(type(divisao))  # Utilizei para informar o tipo da variável divisao, pois não esperava que o python fosse retornar um número que não fosse também int
