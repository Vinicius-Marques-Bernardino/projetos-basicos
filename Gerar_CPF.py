#gerar CPF

#bibliotecas
import re
import random
import os

while True:
    os.system('cls')  # Limpa a tela do terminal
    print('Gerador de CPF\nEscolha uma opção:')
    escolha = input('[1] para gerar um CPF\n[2] para validar um CPF\n[3] para sair\n')

    if escolha not in ['1', '2', '3']:
        print('Opção inválida! Por favor, escolha 1, 2 ou 3.')

    # Gerarando CPF
    elif escolha == '1':
        cpf = '' #inicializando a variavel CPF
        cpfcalculado = 0 #inicializando a variavel CPF calculado

        #gerando os 9 primeiros digitos do CPF
        for i in range(9):
            cpf += str(random.randint(0, 9))
            
        #somando os 9 primeiros digitos e multiplicando por 10, 9, 8...
        for i,c in enumerate(cpf[8::-1], start=2):
            cpfcalculado += int(c)*i

        #multiplicando por 10 e pegando o resto da divisao por 11
        cpfcalculado = (cpfcalculado*10)%11

        cpf += str(cpfcalculado) if cpfcalculado < 10 else '0'

        cpfcalculado = 0 #zerando a variavel para o segundo digito

        #Calculando o segundo digito do CPF
        for i,c in enumerate(cpf[9::-1], start=2):
            cpfcalculado += int(c)*i

        #multiplicando por 10 e pegando o resto da divisao por 11
        cpfcalculado = (cpfcalculado*10)%11

        cpf += str(cpfcalculado) if cpfcalculado < 10 else '0'

        os.system('cls') #limpando a tela      
        print(f'CPF gerado: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}') #formatando o CPF gerado
        os.system('pause') 

    #Validando CPF
    elif escolha == '2':

    # Validar CPF de entrada
        while True:
            cpf = input('Digite seu CPF:\n')
            if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
                break
            else:
                print('CPF inválido! Formato correto: XXX.XXX.XXX-XX')
                
        
        cpf = re.sub(r'[^0-9]', '', cpf) #remove os valores não uméricos do CPF
                
        cpfcalculado=0

    #somando os 9 primeiros digitos e multiplicando por 10, 9, 8...
        for i,c in enumerate(cpf[8::-1], start=2):
                cpfcalculado += int(c)*i

    #multiplicando por 10 e pegando o resto da divisao por 11
        cpfcalculado = (cpfcalculado*10)%11

    # Verificando se o primeiro digito do CPF é válido
        print(f'Primeiro digito do CPF: {cpfcalculado}' if cpfcalculado < 10 else 0)
        if cpfcalculado != int(cpf[9]):
            print('CPF inválido!')
            os.system('cls') 
                
        cpfcalculado= 0 #zerando a variavel para o segundo digito

    #Calculando o segundo digito do CPF
        for i,c in enumerate(cpf[9::-1], start=2):
                cpfcalculado += int(c)*i

    #multiplicando por 10 e pegando o resto da divisao por 11
        cpfcalculado = (cpfcalculado*10)%11

        print(f'Segundo digito do CPF: {cpfcalculado} ' if cpfcalculado < 10 else 0)

    # Verificando se o segundo digito do CPF é válido
        os.system('cls')
        if cpfcalculado != int(cpf[10]):
            print('CPF inválido!')
        else:
            print('CPF válido!')
            os.system('pause')

#Saindo do programa
    elif escolha == '3':
        print('Saindo do programa...')
        break