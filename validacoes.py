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


def validar_login(email, senha, usuarios):
    if email in usuarios and usuarios[email]["Senha"] == senha:
        return True
    else:
        print("Email ou senha incorretos!")
        return False


def validar_destino(origem, destino):
    if origem == destino:
        print("Destino não pode ser igual à origem.")
        return False
    return True


def validar_horario(horario):
    if ":" not in horario:
        print("Horário inválido! Use o formato HH:MM.")
        return False

    partes = horario.split(":")
    if len(partes) != 2:
        print("Horário inválido! Use o formato HH:MM.")
        return False

    hora = partes[0]
    minuto = partes[1]

    if hora == "" or minuto == "":
        print("Horário inválido! Deve ter hora e minuto.")
        return False

    if not (hora >= "00" and hora <= "23" and minuto >= "00" and minuto <= "59"):
        print("Horário inválido! Hora entre 00 e 23, minutos entre 00 e 59.")
        return False

    return True


def validar_vagas(vagas):
    if vagas == "":
        print("Digite a quantidade de vagas.")
        return False

    if vagas.isnumeric():
        if int(vagas) > 0:
            return True
        else:
            print("As vagas devem ser maiores que zero.")
            return False
    else:
        print("Vagas inválidas! Deve ser um número inteiro.")
        return False


def validar_valor(valor):
    if valor == "":
        print("Digite o valor.")
        return False

    partes = valor.split(".")
    if len(partes) == 1 or len(partes) == 2:
        numeros = "".join(partes)
        if numeros.isnumeric():
            if float(valor) > 0:
                return True
            else:
                print("Valor deve ser maior que zero.")
                return False
        else:
            print("Valor inválido! Use apenas números e ponto.")
            return False
    else:
        print("Valor inválido! Deve ter no máximo um ponto decimal.")
        return False


def validar_pagamento(valor_pago, valor_esperado):
    partes = valor_pago.split(".")

    if len(partes) == 1 or len(partes) == 2:
        numeros = "".join(partes)
        if numeros.isnumeric():
            if float(valor_pago) >= valor_esperado:
                return True
            else:
                print("Valor pago insuficiente.")
                return False
        else:
            print("Valor pago inválido!")
            return False
    else:
        print("Valor pago inválido!")
        return False
    