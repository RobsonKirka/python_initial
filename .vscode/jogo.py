import forca
import advinhacao_for


def escolhe_jogo():
    print("*******************")
    print("***Escolha o jogo**")
    print("*******************")

    print("(1) forca (2) advinhacao")

    jogo = int(input("Qual o jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    else:
        print("Jogando adivinhação")
        advinhacao_for.jogar()


if(__name__ == "__main__"):
    escolhe_jogo()
