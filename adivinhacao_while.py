print("********************************")
print("bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 43
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa {} de {}".format(
        rodada, total_tentativas))
    input_str = input("Digite o seu número: ")
    chute = int(input_str)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou o número secreto")
        break
    else:
        if(maior):
            print("Você errou o seu chute foi maior do que o numero secreto")
        elif(menor):  # bastaria o else porem vimos a sintaxe do elif
            print("Você errou o seu chute foi menor do que o numero secreto")
    rodada = rodada + 1
print("Fim do jogo")
