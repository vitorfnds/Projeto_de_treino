########################################
# Importando Funções de Validação
########################################

from validadores import validar_usuario, validar_senha

########################################
# Usuários
########################################

# Usuários armazenados em memória.
usuarios = {}

# Normaliza o usuário para pesquisa sem case sensitive.
def normalizar_usuario(usuario):
    return usuario.strip().lower()

# Verifica se um usuário já existe.
def usuario_existe(usuario):
    usuario_normalizado = normalizar_usuario(usuario)
    return usuario_normalizado in usuarios

# Cria um novo usuário se as validações passarem.
def criar_usuario(usuario, senha):
    usuario_valido, erro_usuario = validar_usuario(usuario)
    if not usuario_valido:
        return False, erro_usuario

    senha_valida, erro_senha = validar_senha(senha)
    if not senha_valida:
        return False, erro_senha

    if usuario_existe(usuario):
        return False, "Usuário já existe."

    usuario_normalizado = normalizar_usuario(usuario)
    usuarios[usuario_normalizado] = {
        'usuario': usuario.strip(),
        'senha': senha.strip(),
        'moedas': 10
    }

    return True, "Usuário criado com sucesso!"

########################################
# Verificação de Login
########################################

# Verifica credenciais de login.
def verificar_login(usuario, senha):

    usuario_normalizado = normalizar_usuario(usuario)
    if usuario_normalizado not in usuarios:
        return False, "Usuário ou senha incorretos."

    senha_normalizada = senha.strip()
    if usuarios[usuario_normalizado]["senha"] != senha_normalizada:
        return False, "Usuário ou senha incorretos."

    return True, "Login realizado com sucesso!"