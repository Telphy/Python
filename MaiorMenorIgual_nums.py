if __name__ == '__main__':

    num1 = int(input(f'Qual é o primeiro número:\n'))
    num2 = int(input(f'Qual é o segundo número:\n'))

    if num1 == num2:
        print(f'O {num1} é igual a {num2}')
    elif num1 < num2:
        print(f'O {num1} é menor que {num2}')
    else:
        print(f'O {num1} é maior que {num2}')