if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        nome = input('Qual teu nome completo:\n')
        nl = nome.split(' ')  # nl e uma lista com 5 cas
        print(f'O nome tem {len(nl)} palavras.')
        print(nl[0])
        for a in nl:
            print(a)
            """
            Se executar esta linha so, a de cima, vou repetir o primeiro nome 2 vezes
            """
        x = 0
        while x < len(nl):
            print(nl[x])
            x += 1
        continuar = input("Queres repetir, S ou N?: ")
    print(f'Até breve')
