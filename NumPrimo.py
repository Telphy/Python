""" EX1 Mostra Num Primo
Pede ao utilizador 2 numeros. O 2º numero deve ser <= 1º.
Mostra todos os numeros primos que ha entre o 1º e o 2º
Depois de mostrar os numeros quantos numeros primos havia
"""


def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1  # zeros = zeros + 1
    return zeros


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        ini = int(input("Seleciona o número inicial: "))
        fim = int(input("Seleciona o número final: "))
        primos = 0
# Outra maneria defazer o ex e retirar a funçao divisores e usar tudo aqui
        for n in range(ini, fim + 1):  # Alterar o for por um while TPC
            if divisores(n) == 2:
                primos += 1
        print(f'Entre {ini} e {fim} há {primos} de primos')

        continuar = input("Queres repetir, S ou N?: ")
    print(f'Até breve')

