from ast import comprehension
import random


def jogar():
    print("*******************")
    print("***Jogo de forca***")
    print("*******************")

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]  # list comprehension

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
            letras_faltando = letras_acertadas.count('_')
            if(letras_faltando == 0):
                print("Parabens você formou a palavra '{}'".format(palavra_secreta))
                acertou = True
            else:
                print(letras_acertadas)
                print("Ainda falta acertar {} letras".format(letras_faltando))
        else:
            erros += 1
            enforcou = erros == 6
            if(not enforcou):
                print("Ops, você errou mas ainda possui {} tentativas".format(6-erros))
    print(letras_acertadas)
    print("fim de jogo")


if(__name__ == "__main__"):
    jogar()
