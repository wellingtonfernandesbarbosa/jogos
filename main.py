import adivinhacao
import forca

print("*********************************")
print("       Bem vindo ao jogo!        ")
print("*********************************")

print("\nEscolha o jogo que deseja jogar")
print("   (1) Adivinhação   (2) Forca   ")
escolha = int(input("Sua escolha: "))

if escolha == 1:
    print("Jogando adivinhação")
    adivinhacao.jogar()
elif escolha == 2:
    print("Jogando forca")
    forca.jogar()

