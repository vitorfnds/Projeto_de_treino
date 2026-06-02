########################################
# MENU DE NAVEGAÇÃO
########################################

# Esta função exibe o menu principal do sistema e aguarda a escolha do usuário
def mostrar_menu():

    # Exibe as opções básicas do sistema
    print("=== Menu Principal ===")
    print("1. Fazer Login")
    print("2. Criar Usuário")
    print("3. Sair")

#Função que exibe a tela de cadastro de usuário, solicitando as informações necessárias para criar um novo usuário
def tela_criar_usuario():

    print("=== Criar Usuário ===")
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")

    # Aqui você pode adicionar a lógica para salvar o usuário no banco de dados ou em um arquivo
    print(f"Usuário '{nome}' criado com sucesso!")


########################################
# EXECUÇÃO PRINCIPAL
########################################

# Função principal que controla o fluxo do aplicativo e processa as opções escolhidas pelo usuário
def main():

    # Controla o laço principal do aplicativo
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

# Executa o aplicativo quando o arquivo é executado diretamente
if __name__ == "__main__":

    main()