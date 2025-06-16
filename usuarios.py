def validar_email(email, usuarios):
    for usuario in usuarios:
        if usuarios[usuario]["Email"] == email:
            print("Esse email já está cadastrado!")
            return False
    if "@gmail.com" not in email or " " in email:
        print("Email inválido! Deve ser um gmail e não pode ter espaços.")
        return False
    return True

    
def validar_senha(senha):
    if len(senha) < 6:
        print("Senha inválida! Deve ter no mínimo 6 caracteres.")
        return False
    return True
    


def cadastrar_usuario(usuarios):
    nome = input('DIGITE O SEU NOME COMPLETO: ')
    email_valido = False
    while not email_valido:
        email = input('DIGITE O SEU EMAIL: ')
        valido = validar_email(email, usuarios)
        if valido:
            email_valido = True
        else:
            print(valido)
            continue
    while True:
        senha = input('DIGITE UMA SENHA: ')
        if validar_senha(senha):
            break
        print('SENHA INVÁLIDA. MÍNIMO 6 CARACTERES.')
    usuarios[email] = {'Email': email, 'Senha': senha, 'Nome': nome}
    print('CADASTRO REALIZADO COM SUCESSO!')


def login_usuario(usuarios):
    email_user = input('DIGITE SEU LOGIN: ')
    senha_user = input('DIGITE SUA SENHA: ')
    if email_user in usuarios and usuarios[email_user]['Senha'] == senha_user:
        print(f'LOGIN BEM-SUCEDIDO! BEM-VINDO, {usuarios[email_user]["Nome"].upper()}')
        return email_user
    else:
        print('USUÁRIO NÃO ENCONTRADO OU SENHA INCORRETA.')
        return None


def logout(usuario_logado):
    if usuario_logado:
        print(f"Usuário {usuario_logado['nome']} desconectado com sucesso.")
    else:
        print("Nenhum usuário está logado.")
    return None
   
    