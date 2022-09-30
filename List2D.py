if __name__ == '__main__':
    ilhas = ["Pico", "Terceira", "Faial", "Graciosa", "S.Jorge"]
    tipos = ["Gasolina", "Gasoleo"]
    vendas = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    totais = [0, 0, 0, 0, 0]

    # Obter input
    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            while True:
                try:
                    vendas[x][y] = int(input(f'Insira vendas de {tipos[x]} para a ilha {ilhas[y]}: '))  # mal o
                    # utilizador digita o valor, ja esta a incerir nas casas
                    break
                except ValueError:  # se o utilizador incerir um valor que nao seja int, iria dar erro, e ira executar
                    # o codigo do except
                    print(f'Insira um valor válido para vendas de {tipos[x]} na ilha {ilhas[y]}')
    for venda in vendas:
        print(venda)

    # Imprimir vendas por tipo
    for x in range(len(vendas)):
        total = 0
        for y in range(len(vendas[x])):
            total += vendas[x][y]
        print(f'Total de vendas para {tipos[x]} = {total}')

    # Imprimir vendas por ilha
    z = 0
    for y in range(len(vendas[z])):
        z += 1
        total = 0
        for x in range(len(vendas)):
            total += vendas[x][y]
        print(f'Total de vendas para {ilhas[y]} = {total}')
        totais[y] = total
        """
        o total de vendas de combustivel
        qual e a ilha que vendeu mais e a menos
        """

    # Imprimir o total de vendas
    total = 0
    for x in range(2):
        for y in range(5):
            total += vendas[x][y]
    print(f'Total de vendas = {total}')

    print(totais)

    # Maior e menor vendas de cada ilha

    maior = totais[0]
    menor = totais[0]
    for x in range(1, len(totais)):
        if totais[x] > maior:
            maior = totais[x]
        if totais[x] < menor:
            menor = totais[x]

    ilhas_maior = []
    ilhas_menor = []

    for x in range(len(totais)):
        if totais[x] == maior:
            ilhas_maior.append(ilhas[x])
        if totais[x] == menor:
            ilhas_menor.append(ilhas[x])
    print(totais)
    print(f'Ilhas com maior valor total de vendas = {ilhas_maior} - {maior}')
    print(f'Ilhas com menor valor total de vendas = {ilhas_menor} - {menor}')

    """
    ilha que consumui mais gasolina
    ilha que consumiu mais gasoleo
    imprimir por ordem de grandesa (sort)
    """