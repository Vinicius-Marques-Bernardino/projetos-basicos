'''
Calculadora
'''
while True:

    print('\nCalculadora')
    n1 = input('Digite o primeiro número: ')
    op = input('Escolha a operação \n[+]adição\t [-]subtração\t [*]multiplicação\t [/]divisão\n')
    n2 = input('Digite o segundo número: ')

    num_val = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        num_val = True
    except:
        num_val = None

    if num_val is None:
        print('Número digitado inválido')
        continue

    op_permit = '+-/*'

    if op not in op_permit or len(op) > 1:
        print('Erro ao digitar operadores')
        continue
    
    print('Seu resultado foi: \n')

    if op == '+':
        print(n1_float + n2_float)
    elif op == '-':
        print(n1_float - n2_float)
    elif op == '/':
        print(n1_float / n2_float)
    elif op == '*':
        print(n1_float * n2_float) 
    else:
        print('Ocorreu um erro!')
        

    sair = input('Digite "sair" para sair\n').lower().startswith('s')
    if sair == True : 
        break
