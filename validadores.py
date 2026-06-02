########################################
# Importando Bibliotecas Necessárias
########################################
import re

########################################
# Validadores de Usuário
########################################

# Valida formato e tamanho do nome de usuário.
def validar_usuario(usuario):
    usuario = usuario.strip()
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

# Valida tamanho e caracteres de senha.
def validar_senha(senha):
    senha = senha.strip()
    if len(senha) < 4 or len(senha) > 20:
        return False, "Senha deve possuir entre 4 e 20 caracteres."
    if " " in senha:
        return False, "Senha não pode conter espaços."
    return True, ""