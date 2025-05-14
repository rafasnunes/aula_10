# Exercício 01 Versão 3
# Criar uma calculadora que receba dois números e seja capaz de somar, subtrair, multiplicar e dividir
# Entrada aleatória de 2 números e o usuário selecionar via teclado qual operação executar com eles.

import random


# Funções do Programa


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


num1 = random.randint(1, 50)
num2 = random.randint(1, 50)

print('Digite a operação: ( + ) Soma ( - ) Subtração ( * ) Multiplicação ( / ) Divisão')

calculadora = input('Digite a operação: ')

print(f'Números gerados {num1} e {num2}')

match calculadora:
    case '+':
        soma = calc_soma(num1, num2)
        print(f'Soma de {num1} + {num2} = {soma}')
    case '-':
        subtracao = calc_subt(num1, num2)
        print(f'Subtração: {subtracao}')
    case '*':
        multiplicacao = calc_mult(num1, num2)
        print(f'Multiplicação: {multiplicacao}')
    case '/':
        divisao = calc_div(num1, num2)
        print(f'Divisão: {divisao}')
