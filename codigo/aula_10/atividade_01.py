# Exercício 01
# Criar uma calculadora que receba dois números e seja capaz de somar, subtrair, multiplicar e dividir

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


num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

soma = calc_soma(num1, num2)
print(f'Soma de {num1} + {num2} = {soma}') # Teste de impressão com todas as variáveis na saída.

subtracao = calc_subt(num1, num2)
print(f'Subtração: {subtracao}')

multiplicacao = calc_mult(num1, num2)
print(f'Multiplicação: {multiplicacao}')

divisao = calc_div(num1, num2)
print(f'Divisão: {divisao}')
# print(type(divisao))  # Utilizei para informar o tipo da variável divisao, pois não esperava que o python fosse retornar um número que não fosse também int
