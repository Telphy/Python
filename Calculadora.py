"""Este programa imprementa funções ariteméticas"""

valor1 = 100  # Variavel global
valor2 = 200

"""
Ver em casa
"""


# Variaveis locais
def aritemetica(num1, num2, op):  # Estou a chamar uma funçao para que eu possa chamar depois, e nao antes
    """
    Esta função implementa as operações de somar, subtrair, multiplicar e dividir
    :param num1: primeiro fator da operacão
    :param num2: segundo fator da operação
    :param op: valores validos sao: +,-,:,*
    :return: resiltado da operação
    """

    total = 'Codigo de operação inválido'
    if op == '+':
        total = num1 + num2
    if op == '*':
        total = num1 * num2
    if op == ':':
        total = num1 / num2
    if op == '-':
        total = num1 - num2
    return total


if __name__ == '__main__':
    nome = input("Como de Chamas? ")
    continuar = 's'
    while continuar == 's':
        valor1 = float(input("Seleciona o valor 1: "))
        valor2 = float(input("Seleciona o valor 2: "))
        operacao = input("Seleciona uma das operações validas sao: +,-,:,* ")
        # Valor1 global deixa de fazer efeito
        print(f'Ola {nome}, {valor1} {operacao} {valor2} = {aritemetica(valor1, valor2, operacao )}')
        continuar = 'Opçao errada'
        continuar = input("Queres repetir, S ou N?: ")
    print(f'Até breve {nome}')