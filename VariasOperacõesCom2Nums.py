def comfor(n1, n2):
    soma = 0
    for i in range(n1, n2 + 1):
        soma = soma + i
    return soma


def comwhile(n1, n2):
    soma = 0
    while soma == 0:
        soma = n1 + n2
        return soma


if __name__ == '__main__':

    while True:
        try:
            num1 = int(input(f'Qual é o primeiro número: '))
            break
        except ValueError:
            print('Insere valores válidos!')

    while True:
        try:
            num2 = int(input(f'Qual é o segundo número: '))
            break
        except ValueError:
            print('Insere valores válidos!')

    fororwhile = (input(f'Deseja a soma ser com "for" ou "while": '))

    if fororwhile == "for":
        print(f'O valor da soma é: {comfor(num1, num2)}')
    elif fororwhile == "while":
        print(f'O valor da some é: {comwhile(num1, num2)}')
    else:
        print(f'"{fororwhile} Não e uma resposta valida, tenta if or while')

    if num1 == num2:
        print(f'O {num1} é igual a {num2}')
    elif num1 < num2:
        print(f'O {num1} é menor que {num2}')
    else:
        print(f'O {num1} é maior que {num2}')