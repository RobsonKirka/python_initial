from ast import comprehension
import random


def jogar():

    imprimir_mensagem_abertura()
    palavra_secreta = carerga_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = arrisca_letra()

        if(chute in palavra_secreta):
            adiciona_letra_correta(palavra_secreta, chute, letras_acertadas)
            acertou = verifica_ganhador(palavra_secreta, letras_acertadas)
        else:
            erros += 1
            enforcou = verifica_perderdor(erros, palavra_secreta)
    print(letras_acertadas)
    print("fim de jogo")


def imprimir_mensagem_abertura():
    print("*******************")
    print("***Jogo de forca***")
    print("*******************")


# parametro opcional caso não seja passado nada ele assume um valor default
def carerga_palavra_secreta(nome_arquivo="palavras.txt"):
    palavras = []
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]  # list comprehension


def arrisca_letra():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def adiciona_letra_correta(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def verifica_ganhador(palavra_secreta, letras_acertadas):
    letras_faltando = letras_acertadas.count('_')
    if(letras_faltando == 0):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        acertou = True
    else:
        print(letras_acertadas)
        print("Ainda falta acertar {} letras".format(letras_faltando))
        acertou = False
    return acertou


def verifica_perderdor(erros, palavra_secreta):
    enforcou = erros == 6
    if(not enforcou):
        print("Ops, você errou mas ainda possui {} tentativas".format(6-erros))
        desenha_forca(erros)
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    return enforcou


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar()
