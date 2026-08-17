import unicodedata


def normalizar_texto(texto):
    # Converte o valor recebido para texto.
    texto = str(texto)

    # Padroniza para minúsculas e remove espaços extras.
    texto = texto.lower().strip()

    # Separa letras e acentos.
    texto = unicodedata.normalize("NFD", texto)

    # Remove os acentos e mantém apenas as letras.
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def pausar():
    # Pausa a execução para o usuário conseguir ler a tela.
    input("\nPressione ENTER para voltar ao menu...")


def exibir_menu():
    # Mostra as opções disponíveis no sistema.
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Sobre a AveDex")
    print("0 - Sair")


def listar_aves(catalogo):
    # Exibe apenas ID e nome popular para facilitar a escolha.
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    # Percorre o catálogo procurando uma ave com o ID informado.
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave

    # Se nenhuma ave for encontrada, retorna None.
    return None


def exibir_detalhes_ave(ave):
    # Exibe informações completas de uma ave.
    print()
    print("=" * 50)
    print("DETALHES DA AVE")
    print("=" * 50)
    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave.get('ordem', 'Não informada')}")
    print(f"Família: {ave.get('familia', 'Não informada')}")
    print(f"Dieta: {ave.get('dieta_tipo', 'Não informada')}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave.get('curiosidade', 'Não informada')}")


def selecionar_ave_por_id(catalogo):
    # Mostra as aves antes de pedir o ID.
    listar_aves(catalogo)

    id_escolhido = input("\nDigite o ID da ave: ").strip()

    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)


def buscar_aves(catalogo, termo_busca):
    # Lista que armazenará as aves encontradas.
    resultados = []

    # Normaliza o termo digitado pelo usuário.
    termo = normalizar_texto(termo_busca)

    # Percorre todas as aves cadastradas.
    for ave in catalogo:

        # Campos em que a busca será realizada.
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        # Junta todos os campos em um único texto.
        texto_busca = " ".join(campos_busca)

        # Normaliza o texto da ave.
        texto_busca = normalizar_texto(texto_busca)

        # Se o termo estiver no texto, a ave entra nos resultados.
        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def exibir_resultados_busca(resultados):
    # Mostra os resultados encontrados pela busca.
    print()
    print("=" * 50)
    print("RESULTADOS DA BUSCA")
    print("=" * 50)

    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )


def tela_busca(catalogo):
    # Solicita o termo de busca.
    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return

    # Busca as aves e exibe os resultados.
    resultados = buscar_aves(catalogo, termo)
    exibir_resultados_busca(resultados)

    # Se houver resultados, permite abrir os detalhes.
    if len(resultados) > 0:
        escolha = input(
            "\nDigite o ID para ver detalhes ou ENTER para voltar: "
        ).strip()

        if escolha != "":
            ave_encontrada = buscar_ave_por_id(resultados, escolha)

            if ave_encontrada is None:
                print("ID não encontrado nos resultados.")
            else:
                exibir_detalhes_ave(ave_encontrada)


catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto parece dizer o próprio nome."
    },
    {
        "id": 2,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e outros invertebrados",
        "curiosidade": "É conhecido por construir ninhos de barro."
    },
    {
        "id": 3,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos e áreas abertas",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    }
]


opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()

    opcao_menu = input("Escolha uma opção: ").strip()

    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        tela_busca(catalogo_aves)

    elif opcao_menu == "3":
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "4":
        print("A AveDex é um catálogo interativo de aves.")
        print(
            "Em breve, teremos comparação, imagens, sons "
            "e dados em arquivo JSON."
        )

    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    else:
        print(
            "Opção inválida. Digite apenas 0, 1, 2, 3 ou 4."
        )

    if opcao_menu != "0":
        pausar()
