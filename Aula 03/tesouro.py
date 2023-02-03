from random import randint

tesouroMin = 0
tesouroMax = 15
tesouro = randint(tesouroMin, tesouroMax)
chute = 0
chances = 3

while chute != tesouro:
    chute = input(f'Chute um número de {tesouroMin} a {tesouroMax}: ')
    if chute.isnumeric():
        chute = int(chute)
        chances -=1
        if chute == tesouro:
            print(f'Muito bem, número {tesouro} descoberto\nAinda haviam {chances} chances')
            break
        else:
            if chute > tesouro:
                print(f'Número errado, o valor secreto é menor, chances restantes: {chances}')
            else:
                print(f'Número errado, tente um número maior, chances restantes: {chances}')
    else:
        print(f'Número inválido! Digite um número de {tesouroMin} a {tesouroMax}')

    if chances == 0:
        print(f'Número de tentativas esgotadas, o número secreto era: {tesouro}')
        break
