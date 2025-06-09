#Jogo da forca

#variáveis
import os


letra = ''
tentativa = 0
correto = 0
acertos = ''
secreto = ''


#Solicite uma plavra
palavra = input("Digite uma palavra: ")
os.system('cls')

#Digite uma letra
while True:
    letra = input("Digite uma letra: ")

#Proibindo mais de uma letra
    if len(letra) > 1:
        print("\nDigite apenas uma letra")
        continue

#Conferindo letra digitada    
    if letra in palavra:
        acertos += letra 

#Digitar letras acertadas
    for secreto in palavra:
        if secreto in acertos:
            print(secreto, end="")
        else: 
            print("_ ", end="")
    tentativa+=1

    if letra in palavra:
        correto += palavra.count(letra)

    tentativa += 1
    
    print("\nacertos: ", correto,)
    print(f"largura: {len(palavra)}")
    
    if correto >= len(palavra):
        os.system('cls')
        print("\n\nVOCÊ GANHOU, SAFADO(A)!")
        print(f"tentativas: {tentativa} \nA palavra era: {palavra}")
        break

    

    





