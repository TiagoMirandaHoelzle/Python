from connection import *
import functions as f
import time

while True:

    print("\n\n==== Menu ====")
    print("Que ação deseja realizar?")
    print("1 - Cadastrar um produto")
    print("2 - Listar produtos cadastrados")
    print("3 - Atualizar as informações de um produto")
    print("4 - Excluir um produto")
    print("5 - Sair do menu")

    try:
        opc = int(input(": "))
        print("\n")
    except ValueError:
        print("\n")
        print("Digite um número válido!")
        continue

    match opc:
        case 1:
            f.create()
            time.sleep(1) # Pausa a execução do código por 1 segundo
        case 2:
            f.read()
            time.sleep(1)

        case 3:
            f.update()
            time.sleep(1)

        case 4:
            f.delete()
            time.sleep(1)

        case 5:
            print("Saindo ...")
            time.sleep(2)
            print("Sessão encerrada")
            break
        case _:
            print("Opção inválida!")
            time.sleep(1)

# Fechando a conexão com o banco
cursor.close()
conn.close()