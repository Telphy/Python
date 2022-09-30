import random


def get_random(ini, fim):
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':

    nums = [0, 0, 0, 0, 0]
    estrelas = [0, 0]

    for y in range(1, 6):
        for x in range(len(nums)):
            while True:
                onumero = get_random(1, 50)
                if onumero not in nums:
                    nums[x] = onumero
                    break
        """
        fazer a lista nums e estrelas do maior para o menor 
        """

        print(f'Aposta Numero {y}')
        print(f'Os numeros que te sairam foram: {sorted(nums)}')

        for x in range(len(estrelas)):
            while True:
                aestrela = get_random(1, 12)
                if aestrela not in nums:
                    estrelas[x] = aestrela
                    break

        print(f'E as estrelas foram: {sorted(estrelas)}')
        print(f'------------------------')