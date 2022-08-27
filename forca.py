def jogar():
    print("*********************************")
    print("   Bem vindo ao jogo da Forca!   ")
    print("*********************************")
    
    palavra_secreta = "sabre".upper()
    letras_acertadas = ["_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_acertadas)
    
    while not acertou and not enforcou:
        chute = input("\nQual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                index = index + 1

        else:
            erros += 1

        enforcou = erros == 6
        print(letras_acertadas)

        if letras_acertadas.count('_') >= 1:
            if letras_acertadas.count('_') > 1:
                print(f"Ainda faltam acertar {letras_acertadas.count('_')} letras.")
            elif letras_acertadas.count('_') == 1:
                print(f"Ainda falta acertar {letras_acertadas.count('_')} letra.")
        
        if not letras_acertadas.count('_'):
            acertou = True
            break
        
        print("\nJogando...")

    if acertou:
        print("\nVocê ganhou!")
    else:
        print("\nVocê perdeu!")
    
    print("\nFim do jogo!")

if __name__=="__main__":
    jogar()