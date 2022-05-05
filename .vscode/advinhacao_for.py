import random


def jogar():
    print("*******************")
    print("Jogo de adivinhação")
    print("*******************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define um Nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    print(numero_secreto)
    for rodada in range(1, total_tentativas + 1):
        print("Rodada {} de {}".format(rodada, total_tentativas))
        input_str = input("Digite um número entre 1 e 100: ")
        chute = int(input_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        if(acertou):
            print("Você acertou o numero secreto e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("O número chutado é maior que o número secreto")
            else:
                print("O número chutado é menor que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
