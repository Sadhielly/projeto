caronas = []

def cadastrar_carona(usuario_logado):
    print("\n--- Cadastro de Carona ---")
    origem = input("Origem: ")
    destino = input("Destino: ")
    data = input("Data da carona (DD/MM/AAAA): ")
    hora = input("Horário da carona (HH:MM): ")
    vagas = int(input("Quantidade de vagas: "))
    valor = float(input("Valor por vaga: "))

    carona = {
        "motorista": usuario_logado["email"],
        "nome_motorista": usuario_logado["nome"],
        "origem": origem,
        "destino": destino,
        "data": data,
        "hora": hora,
        "vagas": vagas,
        "valor": valor,
        "reservas": []
    }

    caronas.append(carona)
    print("Carona cadastrada com sucesso!")


def listar_caronas_disponiveis():
    print("\n--- Caronas Disponíveis ---")
    encontrou = False
    for c in caronas:
        if c["vagas"] > 0:
            print(f"Motorista: {c['nome_motorista']} | Origem: {c['origem']} | Destino: {c['destino']}")
            print(f"Data: {c['data']} | Hora: {c['hora']} | Vagas: {c['vagas']} | Valor: R${c['valor']:.2f}\n")
            encontrou = True
    if not encontrou:
        print("Não há caronas disponíveis no momento.")


def buscar_carona_por_origem_destino():
    print("\n--- Buscar Carona ---")
    origem = input("Origem: ")
    destino = input("Destino: ")
    encontrou = False

    for c in caronas:
        if c["origem"].lower() == origem.lower() and c["destino"].lower() == destino.lower() and c["vagas"] > 0:
            print(f"Motorista: {c['nome_motorista']} | Data: {c['data']} | Hora: {c['hora']} | Vagas: {c['vagas']}")
            print(f"Valor por vaga: R${c['valor']:.2f}\n")
            encontrou = True

    if not encontrou:
        print("Nenhuma carona encontrada com os critérios informados.")


def reservar_vaga(usuario_logado):
    print("\n--- Reservar Vaga ---")
    email_motorista = input("Email do motorista: ")
    data = input("Data da carona (DD/MM/AAAA): ")

    for c in caronas:
        if c["motorista"] == email_motorista and c["data"] == data:
            if usuario_logado["email"] in c["reservas"]:
                print("Erro: você já reservou essa carona.")
                return
            if c["vagas"] > 0:
                c["reservas"].append(usuario_logado["email"])
                c["vagas"] -= 1
                print("Reserva realizada com sucesso!")
                return
            else:
                print("Erro: não há vagas disponíveis.")
                return

    print("Erro: carona não encontrada.")


def cancelar_reserva(usuario_logado):
    print("\n--- Cancelar Reserva ---")
    email_motorista = input("Email do motorista: ")
    data = input("Data da carona (DD/MM/AAAA): ")

    for c in caronas:
        if c["motorista"] == email_motorista and c["data"] == data:
            if usuario_logado["email"] in c["reservas"]:
                c["reservas"].remove(usuario_logado["email"])
                c["vagas"] += 1
                print("Reserva cancelada com sucesso.")
                return
            else:
                print("Você não possui reserva nessa carona.")
                return

    print("Erro: carona não encontrada.")


def remover_carona(usuario_logado):
    print("\n--- Remover Carona ---")
    data = input("Data da carona a remover (DD/MM/AAAA): ")
    for c in caronas:
        if c["motorista"] == usuario_logado["email"] and c["data"] == data:
            caronas.remove(c)
            print("Carona removida com sucesso.")
            return

    print("Erro: você não possui carona cadastrada nessa data.")


def mostrar_detalhes_carona():
    print("\n--- Detalhes da Carona ---")
    email_motorista = input("Email do motorista: ")
    data = input("Data da carona (DD/MM/AAAA): ")

    for c in caronas:
        if c["motorista"] == email_motorista and c["data"] == data:
            print(f"Origem: {c['origem']}")
            print(f"Destino: {c['destino']}")
            print(f"Horário: {c['hora']}")
            print(f"Valor por vaga: R${c['valor']:.2f}")
            print(f"Vagas restantes: {c['vagas']}")
            print("Passageiros:")
            if c["reservas"]:
                for r in c["reservas"]:
                    print(f"- {r}")
            else:
                print("Nenhum passageiro ainda.")
            return

    print("Carona não encontrada.")


def mostrar_caronas_do_usuario(usuario_logado):
    print("\n--- Minhas Caronas ---")
    encontrou = False
    for c in caronas:
        if c["motorista"] == usuario_logado["email"]:
            print(f"{c['origem']} -> {c['destino']} | {c['data']} {c['hora']} | R${c['valor']:.2f}")
            print(f"Vagas restantes: {c['vagas']}")
            print(f"Passageiros: {', '.join(c['reservas']) if c['reservas'] else 'Nenhum'}\n")
            encontrou = True
    if not encontrou:
        print("Você não tem caronas cadastradas.")


def registrar_item_perdido(itens_perdidos):
    print('=== ITENS PERDIDOS ===')
    for item in itens_perdidos:
        print(f'- {item}')
    acao = input('DESEJA REGISTRAR UM ITEM PERDIDO? [S/N]: ').upper()
    if acao == 'S':
        item = input('DESCREVA O ITEM: ')
        if item not in itens_perdidos:
            itens_perdidos.append(item)
            print(f'ITEM "{item}" REGISTRADO.')