# encoding:UTF-8
import random

userScore = 0
pcScore = 0
totalScore = 0


while True:
    def percent():
        if totalScore > 0:
            x = ((totalScore - pcScore) / totalScore) * 100
            return x
        elif totalScore == 0:
            x = 0
            return x

    aleatorio = random.randrange(0, 3)
    escolhaPc = ""
    print("1)Pedra")
    print("2)Papel")
    print("3)Tesoura")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Show Scores")
    opcao = int(input("O que você escolhe: "))

    if opcao == 1:
        escolhaUsuario = "pedra"
    elif opcao == 2:
        escolhaUsuario = "papel"
    elif opcao == 3:
        escolhaUsuario = "tesoura"
    elif opcao == 4:
        escolhaUsuario = "lagarto"
    elif opcao == 5:
        escolhaUsuario = "spock"
    elif opcao == 6:
        userScore = userScore + userWin
        pcScore = pcScore + pcWin
        totalScore = userScore + pcScore
        print("Pontuações: ")
        print("Usuário: ", userScore)
        print("Pc: ", pcScore)
        print("Porcentagem de vitórias: ", percent(), "% ")
        break
    else:
        print("Valor Invalido")
        continue

    print("Tua escolha: ", escolhaUsuario)
    if aleatorio == 0:
        escolhaPc = "pedra"
    elif aleatorio == 1:
        escolhaPc = "papel"
    elif aleatorio == 2:
        escolhaPc = "tesoura"
    elif aleatorio == 3:
        escolhaPc = "lagarto"
    elif aleatorio == 4:
        escolhaPc = "spock"
    print("PC escolheu: ", escolhaPc)
    print("...")

    userWin = 0
    pcWin = 0

    if escolhaPc == "pedra" and escolhaUsuario == "papel":
        print("Ganhou, papel cobre pedra")
        userWin += 1
    elif escolhaPc == "papel" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura corta papel")
        userWin += 1
    elif escolhaPc == "tesoura" and escolhaUsuario == "pedra":
        print("Ganhou, pedra amassa tesoura")
        userWin += 1
    elif escolhaPc == "lagarto" and escolhaUsuario == "pedra":
        print("Ganhou, a pedra esmagou o lagarto")
        userWin += 1
    elif escolhaPc == "spock" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto envenena o Spock")
        userWin += 1
    elif escolhaPc == "papel" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto come o papel")
        userWin += 1
    elif escolhaUsuario == "tesoura" and escolhaPc == "lagarto":
        print("Ganhou, a tesoura decapitou o lagarto")
        userWin += 1
    elif escolhaUsuario == "spock" and escolhaPc == "pedra":
        print("Ganhou, o Spock vaporizou a pedra")
        userWin += 1
    elif escolhaUsuario == "spock" and escolhaPc == "tesoura":
        print("Ganhou, o Spock quebrou a tesoura")
        userWin += 1
    elif escolhaUsuario == "papel" and escolhaPc == "spock":
        print("Ganhou, o papel refuta o spock")
        userWin += 1

    if escolhaUsuario == "pedra" and escolhaPc == "papel":
        print("Perdeu, papel cobre pedra")
        pcWin += 1
    elif escolhaUsuario == "papel" and escolhaPc == "tesoura":
        print("Perdeu, tesoura corta papel")
        pcWin += 1
    elif escolhaUsuario == "tesoura" and escolhaPc == "pedra":
        print("Perdeu, pedra amassa tesoura")
        pcWin += 1
    elif escolhaUsuario == "lagarto" and escolhaPc == "pedra":
        print("Perdeu, pedra esmaga o lagarto")
        pcWin += 1
    elif escolhaUsuario == "spock" and escolhaPc == "lagarto":
        print("Perdeu, o lagarto envenenou o Spock")
        pcWin += 1
    elif escolhaUsuario == "papel" and escolhaPc == "lagarto":
        print("Perdeu, o lagarto comeu o papel")
        pcWin += 1
    elif escolhaUsuario == "lagarto" and escolhaPc == "tesoura":
        print("Perdeu, o lagarto foi decapitado pela tesoura")
        pcWin += 1
    elif escolhaUsuario == "pedra" and escolhaPc == "spock":
        print("Perdeu, o spock vaporizou a pedra")
        pcWin += 1
    elif escolhaUsuario == "tesoura" and escolhaPc == "spock":
        print("Perdeu, o spock quebrou a tesoura")
        pcWin += 1
    elif escolhaUsuario == "spock" and escolhaPc == "papel":
        print("Perdeu, o papel refuta o spock")
        pcWin += 1

    elif escolhaPc == escolhaUsuario:
        print("Empate")
    again = input("Jogar novamente? s/n: ")
    if 's' in again:
        continue
    elif 'n' in again:
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")
