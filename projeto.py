from usuarios.usuarios import cadastrar_usuario, login_usuario, logout
from caronas.caronas import (
    cadastrar_carona, listar_caronas_disponiveis, buscar_carona_por_origem_destino,
    reservar_vaga, cancelar_reserva, remover_carona, mostrar_detalhes_carona,
    mostrar_caronas_do_usuario, registrar_item_perdido
)
from relatorios.relatorio import relatorio_totalizadores, salvar_relatorio_em_arquivo
from manipular_arquivo import salvar_usuarios_em_arquivo, carregar_usuarios_de_arquivo


usuarios = {}
caronas = []
itens_perdidos = []
usuario_logado = None


def menu():
    print("\n--- MENU ---")
    print("1. Cadastrar Usuário")
    print("2. Login")
    print("3. Cadastrar Carona")
    print("4. Listar Caronas Disponíveis")
    print("5. Buscar Carona por Origem/Destino")
    print("6. Reservar Vaga")
    print("7. Cancelar Reserva")
    print("8. Remover Carona")
    print("9. Mostrar Detalhes da Carona")
    print("10. Mostrar Minhas Caronas")
    print("11. Registrar Item Perdido")
    print("12. Logout")
    print("13. Sair")
    print("14. Relatório Totalizador")
    print("15. Salvar Relatório Totalizador")

usuarios = carregar_usuarios_de_arquivo()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario(usuarios)

    elif opcao == "2":
        email = login_usuario(usuarios)
        if email:
            usuario_logado = {
                "email": email,
                "nome": usuarios[email]["Nome"]
            }

    elif opcao == "3":
        if usuario_logado:
            cadastrar_carona(caronas, usuario_logado)
        else:
            print("Você precisa estar logado!")

    elif opcao == "4":
        if usuario_logado:
            listar_caronas_disponiveis(caronas)
        else:
            print("Você precisa estar logado!")

    elif opcao == "5":
        if usuario_logado:
            buscar_carona_por_origem_destino(caronas)
        else:
            print("Você precisa estar logado!")

    elif opcao == "6":
        if usuario_logado:
            reservar_vaga(caronas, usuario_logado)
        else:
            print("Você precisa estar logado!")

    elif opcao == "7":
        if usuario_logado:
            cancelar_reserva(caronas, usuario_logado)
        else:
            print("Você precisa estar logado!")

    elif opcao == "8":
        if usuario_logado:
            remover_carona(caronas, usuario_logado)
        else:
            print("Você precisa estar logado!")

    elif opcao == "9":
        if usuario_logado:
            mostrar_detalhes_carona(caronas)
        else:
            print("Você precisa estar logado!")

    elif opcao == "10":
        if usuario_logado:
            mostrar_caronas_do_usuario(caronas, usuario_logado)
        else:
            print("Você precisa estar logado!")

    elif opcao == "11":
        registrar_item_perdido(itens_perdidos)

    elif opcao == "12":
        logout()
        usuario_logado = None

    elif opcao == "13":
        salvar_usuarios_em_arquivo(usuarios)
        print("Encerrando sistema...")
        break

    elif opcao == "14":
        if usuario_logado:
            linhas_relatorio = relatorio_totalizadores(caronas, usuario_logado)
        else:
            print("Você precisa estar logado!")

    elif opcao == "15":
        if usuario_logado:
            linhas_relatorio = relatorio_totalizadores(caronas, usuario_logado)
            if linhas_relatorio:
                salvar_relatorio_em_arquivo(linhas_relatorio, usuario_logado)
        else:
            print("Você precisa estar logado!")

    else:
        print("Opção inválida. Tente novamente.")