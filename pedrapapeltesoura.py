#encoding:UTF-8
import random

while True: 
    aleatorio = random.randrange(0, 3)
    escolhaPc = ""
    print("1)Pedra")
    print("2)Papel")
    print("3)Tesoura")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Sair do Programa")
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
        print ("Nos vemos!")
        break
    else:
        print ("Valor Invalido")
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
    
    if escolhaPc == "pedra" and escolhaUsuario == "papel":
        print("Ganhou, papel cobre pedra")
    elif escolhaPc == "papel" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura corta papel")
    elif escolhaPc == "tesoura" and escolhaUsuario == "pedra":
        print("Ganhou, pedra amassa tesoura")
    elif escolhaPc == "spock" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto envenena o Spock")
    elif escolhaPc == "papel" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto come o papel")
    elif escolhaUsuario == "tesoura" and escolhaPc == "lagarto":
        print("Ganhou, a tesoura decapitou o lagarto")
    elif escolhaUsuario == "pedra" and escolhaPc == "spock":
        print("Ganhou, o Spock vaporizou a pedra")
    elif escolhaUsuario == "tesoura" and escolhaPc == "spock":
        print("Ganhou, o Spock quebrou a tesoura")
    elif escolhaUsuario == "papel" and escolhaPc == "spock":
        print("Ganhou, o papel refuta o spock")
        
    if escolhaUsuario == "pedra" and escolhaPc == "papel":
        print("Perdeu, papel cobre pedra")
    elif escolhaUsuario == "papel" and escolhaPc == "tesoura":
        print("Perdeu, tesoura corta papel")
    elif escolhaUsuario == "tesoura" and escolhaPc == "pedra":
        print("Perdeu, pedra amassa tesoura")
    elif escolhaUsuario == "spock" and escolhaPc == "lagarto":
        print("Perdeu, o lagarto envenenou o Spock")
    elif escolhaUsuario == "papel" and escolhaPc == "lagarto":
        print("Perdeu, o lagarto comeu o papel")
    elif escolhaUsuario == "lagarto" and escolhaPc == "tesoura":
        print("Perdeu, o lagarto foi decapitado pela tesoura")
    elif escolhaUsuario == "pedra" and escolhaPc == "spock":
        print("Perdeu, o spock vaporizou a pedra")
    elif escolhaUsuario == "tesoura" and escolhaPc == "spock":
        print("Perdeu, o spock quebrou a tesoura")
    elif escolhaUsuario == "spock" and escolhaPc == "papel":
        print("Perdeu, o papel refuta o spock")


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