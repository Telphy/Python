def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1  # zeros = zeros + 1
    return zeros


"""
    for n in range(1,num):
        print(n)
    return 1

    se eu fizer assim, so vai contar ate ao numero antes do escolhido por exemplo 5, iria dar 1 2 3 4

"""

if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        numero = int(input("Seleciona o número 1: "))
        print(f'O número {numero} tem {divisores(numero)} divisores')
        continuar = input("Queres repetir, S ou N?: ")
    print(f'Até breve')