

if __name__ == '__main__':
    """
    primeira maneira
    fatorial = int(input(f'Qual é o número que será o fatorial?: '))
    for x in range(1, fatorial):
        fatorial = fatorial * x # 10 = 10*1 / 10=10*2 / 20 = 20*3 / etc
    print(fatorial)
    """

    # Segunda maneira
    def fatorial(num):
        for x in range(1, num):
            num = num * x
        return num

    numero = int(input(f'Qual é o número que será o fatorial?: '))
    print(fatorial(numero))