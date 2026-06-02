########################################
# MENU DE NAVEGAÇÃO
########################################

def mostrar_menu():
    print("=== Menu Principal ===")
    print("1. Fazer Login")
    print("2. Criar Usuário")
    print("3. Sair")

def tela_criar_usuario():
    print("=== Criar Usuário ===")
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")

    print(f"Usuário '{nome}' criado com sucesso!")


########################################
# EXECUÇÃO PRINCIPAL
########################################

def main():
    while True:

        mostrar_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            print("Você escolheu Fazer Login.")
        elif escolha == '2':
            tela_criar_usuario()
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção não válida. Por favor, tente novamente.")


########################################
# PONTO DE ENTRADA
########################################

if __name__ == "__main__":
    main()