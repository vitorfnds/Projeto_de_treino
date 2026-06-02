########################################
# Importando Bibliotecas Necessárias
########################################
import re

########################################
# Validadores de Usuário
########################################

# Este módulo é responsável por gerenciar os usuários do sistema, incluindo a validação dos dados de entrada.
def validar_usuario(usuario):

    # Remove espaços em branco no início e no final do nome de usuário
    usuario = usuario.strip()

    # Esta função valida o nome de usuário e a senha
    if len(usuario) < 2 or len(usuario) > 20:
        return False, "Usuário deve possuir entre 2 e 20 caracteres."
    if " " in usuario:
        return False, "Usuário não pode conter espaços."
    if not re.match(r"^[A-Za-z0-9]{2,20}$", usuario):
        return False, "Usuário deve conter apenas letras e números."
    
    return True, ""

########################################
# Validadores de Senha
########################################

# Esta função valida a senha do usuário, garantindo que ela atenda aos critérios de segurança
def validar_senha(senha):

    # Remove espaços em branco no início e no final da senha
    senha = senha.strip()

    # Verifica se a senha tem pelo menos 4 caracteres
    if len(senha) < 4 or len(senha) > 20:
        return False, 'Senha deve possuir entre 4 e 20 caracteres.'
    if '' in senha:
        return False, 'Senha não pode conter espaços em brancos.'
    
    return True, 'Senha válida.'