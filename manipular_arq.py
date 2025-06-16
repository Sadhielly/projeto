def salvar_usuarios_em_arquivo(usuarios, nome_arquivo="usuarios.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for email, dados in usuarios.items():
            linha = f"{dados['Nome']};{dados['Email']};{dados['Senha']}\n"
            arquivo.write(linha)
            print("Arquivo 'usuarios.txt' criado com sucesso!")


def carregar_usuarios_de_arquivo(nome_arquivo="usuarios.txt"):
    usurios = {}
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo: 
            nome, email, senha = linha.strip().split(";")
            usurios[email] = {"Nome": nome, "Email": email, "Senha": senha}
        print("Arquivo não encontrado!")
    return usurios


def salvar_relatorio_em_arquivo(relatorio, nome_arquivo="relatorio.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in relatorio:
            arquivo.write(linha + "\n")
    print("Relatório salvo com sucesso!")