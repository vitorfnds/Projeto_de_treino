from usuarios import criar_usuario, verificar_login

########################################
# INTERFACE DE LOGIN
########################################

# Mostra a tela inicial de login/menu.
def mostrar_tela_login():
    print("=== TELA LOGIN ===")
    print("1 - Fazer Login")
    print("2 - Criar Usuario")
    print("3 - Sair")


# Solicita usuário e senha com até três tentativas.
def tela_login():
    tentativas = 0
    while tentativas < 3:
        usuario = input("Usuario: ").strip()
        senha = input("Senha: ").strip()
        sucesso, mensagem = verificar_login(usuario, senha)
        print(mensagem)

        if sucesso:
            return True

        tentativas += 1
        if tentativas < 3:
            print(f"Tentativa {tentativas}/3. Tente novamente.\n")

    print("Numero maximo de tentativas atingido. Retornando a tela inicial.")
    return False


# Registra um novo usuário usando validação do módulo usuarios.
def tela_criar_usuario():
    print("=== CRIAR USUARIO ===")
    usuario = input("Digite o nome do usuario: ").strip()
    senha = input("Digite a senha do usuario: ").strip()
    sucesso, mensagem = criar_usuario(usuario, senha)
    print(mensagem)


# Exibe a tela principal após login bem-sucedido.
def mostrar_menu_principal():
    print("=== MENU PRINCIPAL ===")
    print("Login realizado com sucesso!")
    print("Ainda nao ha opcoes implementadas.")
    input("Pressione Enter para voltar a tela inicial.")


########################################
# EXECUCAO PRINCIPAL
########################################

# Loop principal do programa, controla navegação entre telas.
def main():
    while True:
        mostrar_tela_login()
        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "1":
            if tela_login():
                mostrar_menu_principal()
        elif escolha == "2":
            tela_criar_usuario()
        elif escolha == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opcao nao valida. Por favor, tente novamente.")


########################################
# PONTO DE ENTRADA
########################################

if __name__ == "__main__":
    main()
