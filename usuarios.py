########################################
# Importando Funções de Validação
########################################

# Importando a validação de usuário e senha do arquivo validadores.py
from validadores import (
    validar_usuario,
    validar_senha
)

########################################
# Usuários
########################################

# Dicionário responsável por armazenar os usuários em memória.
usuarios = {}

# Este módulo é responsável por gerenciar os usuários do sistema, incluindo a validação dos dados de entrada.

def normalizar_usuario(usuario):
    """
    Normaliza o nome de usuário removendo espaços nas bordas
    e convertendo todo o texto para minúsculas.
    """
    return usuario.strip().lower()

# Esta função verifica se um usuário já existe no sistema, comparando o nome de usuário normalizado com os usuários existentes.
def usuario_existe(usuario):

    # Normaliza o nome de usuário para garantir uma comparação consistente
    usuario_normalizado = normalizar_usuario(usuario)
    return usuario_normalizado in usuarios

# Esta função cria um novo usuário, validando o nome de usuário e a senha antes de adicioná-lo ao sistema
def criar_usuario(usuario, senha):

    # Normaliza o nome de usuário para garantir uma comparação consistente
    usuario_valido, erro_usuario = validar_usuario(usuario)
    if not usuario_valido:
        return False, erro_usuario
    
    # Normaliza a senha para garantir uma comparação consistente
    senha_valida, erro_senha = validar_senha(senha)
    if not senha_valida:
        return False, erro_senha
    
    if usuario_existe(usuario):
        return False, "Usuário já existe."
    
    # Normaliza o nome de usuário para garantir uma comparação consistente e adiciona o novo usuário ao sistema
    usuario_normalizado = normalizar_usuario(usuario)
    usuarios[usuario_normalizado] = {
        'usuario': usuario.strip(),
        'senha': senha.strip(),
        'moedas': 10
    }

    return True, "Usuário criado com sucesso!"

# Esta função verifica se as credenciais de login do usuário são válidas, comparando o nome de usuário e a senha fornecidos com os dados armazenados
def verificar_login(usuario, senha):

    # Normaliza o nome de usuário para garantir uma comparação consistente
    usuario_normalizado = normalizar_usuario(usuario)
    if usuario_normalizado not in usuarios:
        return False, "Usuário ou senha incorretos."

    # Normaliza a senha para garantir uma comparação consistente e verifica se a senha fornecida corresponde à senha armazenada para o usuário
    senha_normalizada = senha.strip()
    if usuarios[usuario_normalizado]["senha"] != senha_normalizada:
        return False, "Usuário ou senha incorretos."

    return True, "Login realizado com sucesso!"