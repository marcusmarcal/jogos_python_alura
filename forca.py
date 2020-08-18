import random

def jogar():
    print("*******************************************")
    print("** Bem-vindo ao jogo de Forca do Dionei! **")
    print("*******************************************")

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    tamanho = len(palavras)
    escolhida = palavras[random.randrange(0, tamanho)]

    arquivo.close()

    palavra_secreta = escolhida.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print("Palavra: ", letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    #print("Encontrou a letra {} na posição {}".format(chute, index))
                index += 1
        else:
            erros += 1
            print("Erros: {}".format(erros))
            if(erros == 6):
                enforcou = True
                print("****************** ENFORCOU!! ******************")
                print("***** A PALAVRA ERA >>> {} <<< *****".format(palavra_secreta))
                print("************************************************\n")
                novo = input("Jogar de novo? [S] ou [N] ").upper()
                if novo == "S":
                    jogar()
                else:
                    print("************* ATÉ A PRÓXIMA! **************")
                    break
        print("Palavra: ", letras_acertadas)
        # print("Jogando...")


        if "_" not in letras_acertadas:
            acertou = True
            print("******************* PARABÉNS *******************")
            print("A PALAVRA ERA >>> {} <<<".format(palavra_secreta))
            print("************************************************")
            novo = input("Jogar de novo? [S] ou [N] ").upper()
            if novo == "S":
                jogar()
            else:
                print("************* ATÉ A PRÓXIMA! **************")
                break

if(__name__ == "__main__"):
    jogar()