import random

def jogar():    
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000
    
    print("\nSelecione o nivel de dificuldade")
    print("(1) Facil  (2) Medio  (3) Dificil")
    nivel = int(input("Escolha o nivel: "))
    
    if nivel == 1:
        total_de_tentativas = 12
    elif nivel == 2:
        total_de_tentativas = 7
    elif nivel == 3:
        total_de_tentativas = 3
    
    
    for rodada in range(1, total_de_tentativas + 1):
        print(f"\nTentativa {rodada} de {total_de_tentativas}")
    
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)
        
        if (chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100!")
            continue
    
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
    
        if (acertou):
            print("Parabéns! Você acertou!")
            print("Voce fez {} pontos.".format (pontos))
            break
        else:
            if (maior):
                print("O seu chute foi maior do que o número secreto!")
            elif (menor):
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    
    print(f"\nO número sorteado foi {numero_secreto}")
    print("Fim do jogo")

if (__name__=="__main__"):
    jogar()