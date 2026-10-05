def verificar_situacao(saldo):

    if saldo < 0:
        return "Saldo negativo"
    elif saldo == 0:
        return "Saldo zerado"
    else:
        return "Saldo positivo"

pessoas = []
opcao = 0

while opcao != 3:
    print("=====SISTEMA DE CADASTRO DE BANCOS=====")
    print("1- Cadastrar banco")
    print("2- Listar bancos cadastrados")
    print("3- Sair")

    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:

        nome = input ("Digite o nome do banco:")
        nome1 = input ("Digite o nome do cliente:")

        saldo = float(input("Digite o saldo da conta:"))

        situacao = verificar_situacao(saldo)

        print("Nome do banco:" , nome)
        print("---------------------------------")
        print("Nome do cliente:" , nome1)
        print("---------------------------------")
        print("Saldo da conta:" , saldo)
        print("---------------------------------")
        print("Situação do saldo:" , situacao)
        print("---------------------------------")

        pessoas.append(nome)

        print("Banco cadastrado com sucesso!")

    elif opcao == 2:

        print("Lista de bancos cadastrados:")

        for pessoa in pessoas:
            print(pessoa)
        print("---------------------------------")

    elif opcao == 3:

        print("Sistema encerrado.")   

    else: 
        print("Opção inválida. Tente novamente.")


