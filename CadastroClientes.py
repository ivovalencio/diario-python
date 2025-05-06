#Primeiro formulário de cadastro de clientes.
# Opção 1: Cadastrar novo cliente
#Opção 2: Listar todos os clientes
#Opção 3: Sair
#O sistema deve pedir: "Escolha uma opção: "
#"Digite o nome do cliente: "
# "Digite o telefone do cliente: "
#"Digite o e-mail do cliente: "
#"Digite o telefone do cliente: "
#Cliente cadastrado com sucesso!


class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
#aqui as ações
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")

#clientes = [] → Aqui está uma lista vazia, antes do laço, para armazenamento temporário dos objetos criados da classe Cliente.
#Sempre que o usuário cadastrar um novo cliente, um novo objeto será adicionado a esta lista com clientes.append(novo_cliente)

clientes = []

while True:
    print("\nMenu: ")
    print("1 - Cadastrar Novo Cliente")
    print("2 - Listar clientes")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input(" Digite seu nome: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite o e-mail: ")
        novo_cliente = Cliente(nome, telefone, email)
        clientes.append(novo_cliente)
        print("Cliente cadastrado com sucesso. ")

    elif opcao == "2":
        if not clientes:
            print("Nenhum cliente cadastrado. ")
        else:
            for cliente in clientes:
                cliente.mostrar_dados()
    elif opcao =="3":
        print ("Encerrando o programa. ")
        break

    else:
        print("Opção inválida. Tente novamente ")

