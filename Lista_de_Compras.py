import os


lista_compras = []
action = ""
func = ""
i=0

print("LISTA DE COMPRAS\n\n")

while True:
    print("Selcione uma opção")
    action = input("[a]adicionar item\t [d]deletar item\t [s]mostrar blista\n")

    if action == 'a':
        os.system('cls')
        func = input("Digite o valor: ")
        if func in lista_compras:
            print("Item já existente")
        else:
            lista_compras.append(func)

    elif action == 'd':
        os.system('cls')
        func = input("Qual item deseja remover: ")
        try:
            i = int(func)
            del lista_compras[i]
        except ValueError:
            print("Este não é um valor válido")
        except IndexError:
            print("Não há este item")
        except Exception:
            print("Erro desconhecido")

    elif action == 's':
        os.system('cls')

        if len(lista_compras) == 0:
            print("Lista vázia")
        else:
            for i, item in enumerate(lista_compras):
                print(i, item)
    else:
        print("Ação não reconhecida, escolha uma das opções 'a', 'd', 's'")
