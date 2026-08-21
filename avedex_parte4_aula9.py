# ============================================================
# AVEDEX - CATÁLOGO INTERATIVO DE AVES
# ============================================================
# Sistema desenvolvido para consulta, busca, visualização
# de informações e comparação entre diferentes espécies
# de aves cadastradas no catálogo.
# ============================================================


import unicodedata


# ============================================================
# CONSTANTES DO SISTEMA
# ============================================================

# Define a largura padrão utilizada nos títulos e separadores.
LARGURA_TELA = 78

# Opções disponíveis no menu principal da AveDex.
OPCOES_MENU = [
    "1 - Listar aves",
    "2 - Buscar ave",
    "3 - Ver detalhes de uma ave",
    "4 - Comparar duas aves",
    "5 - Sobre a AveDex",
    "0 - Sair"
]

# Campos utilizados nas pesquisas realizadas no catálogo.
CAMPOS_BUSCA = [
    "nome_popular",
    "nome_cientifico",
    "familia",
    "ordem",
    "dieta_tipo"
]

# Campos utilizados na comparação entre duas aves.
# Cada item possui: rótulo, campo do dicionário e unidade.
CAMPOS_COMPARACAO = [
    ("Nome científico", "nome_cientifico", ""),
    ("Ordem", "ordem", ""),
    ("Família", "familia", ""),
    ("Dieta", "dieta_tipo", ""),
    ("Habitat", "habitat", ""),
    ("Comprimento", "comprimento_cm", "cm"),
    ("Peso", "peso_g", "g"),
    ("Conservação", "status_conservacao", ""),
    ("Índice", "indice_conservacao", "")
]


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def linha(caractere="=", largura=LARGURA_TELA):
    # Retorna uma linha formada pela repetição de um caractere.
    return caractere * largura


def titulo(texto):
    # Exibe um título padronizado para as telas da AveDex.
    print()
    print(linha("="))
    print(texto)
    print(linha("="))


def mensagem_aviso(texto):
    # Exibe uma mensagem de aviso para orientar o usuário.
    print(f"[AVISO] {texto}")


def normalizar_texto(texto):
    # Converte o valor recebido para texto.
    texto = str(texto)

    # Padroniza o texto para letras minúsculas e remove espaços extras.
    texto = texto.lower().strip()

    # Separa as letras dos sinais de acentuação.
    texto = unicodedata.normalize("NFD", texto)

    # Remove os sinais de acentuação do texto.
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def pausar():
    # Pausa a execução para que o usuário consiga ler a tela.
    input("\nPressione ENTER para voltar ao menu...")


def valor_ou_indisponivel(valor, unidade=""):
    # Retorna uma mensagem quando não existe informação cadastrada.
    if valor is None or valor == "":
        return "Não informado"

    # Acrescenta a unidade quando ela for necessária.
    if unidade != "":
        return f"{valor} {unidade}"

    return str(valor)


def cortar_texto(texto, tamanho=25):
    # Trata valores de texto que estejam ausentes.
    if texto is None:
        return "Não informado"

    texto = str(texto).strip()

    # Retorna o texto original caso ele esteja dentro do limite.
    if len(texto) <= tamanho:
        return texto

    # Reduz o texto e acrescenta reticências.
    return texto[: tamanho - 3] + "..."


# ============================================================
# MENU E LISTAGEM DE AVES
# ============================================================

def exibir_menu():
    # Exibe o menu principal utilizando as opções cadastradas.
    titulo("AVEDEX - MENU PRINCIPAL")

    # Percorre e apresenta cada opção disponível.
    for opcao in OPCOES_MENU:
        print(opcao)


def listar_aves(catalogo):
    # Exibe todas as aves cadastradas no catálogo.
    titulo("AVES CADASTRADAS")

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    # Procura uma ave no catálogo utilizando seu ID.
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave

    return None


# ============================================================
# DETALHES DA AVE
# ============================================================

def exibir_detalhes_ave(ave):
    # Exibe todas as informações cadastradas de uma ave.
    titulo("DETALHES DA AVE")

    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave.get('ordem', 'Não informada')}")
    print(f"Família: {ave.get('familia', 'Não informada')}")
    print(f"Dieta: {ave.get('dieta_tipo', 'Não informada')}")
    print(f"Habitat: {ave['habitat']}")
    print(
        f"Comprimento: "
        f"{valor_ou_indisponivel(ave.get('comprimento_cm'), 'cm')}"
    )
    print(
        f"Peso: "
        f"{valor_ou_indisponivel(ave.get('peso_g'), 'g')}"
    )
    print(
        f"Conservação: "
        f"{ave.get('status_conservacao', 'Não informada')}"
    )
    print(
        f"Índice de conservação: "
        f"{ave.get('indice_conservacao', 'Não informado')}"
    )
    print(f"Alimentação: {ave['alimentacao']}")
    print(
        f"Curiosidade: "
        f"{ave.get('curiosidade', 'Não informada')}"
    )


def selecionar_ave_por_id(catalogo):
    # Permite ao usuário selecionar uma ave utilizando seu ID.
    listar_aves(catalogo)

    id_escolhido = input("\nDigite o ID da ave: ").strip()

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        mensagem_aviso(
            "Ave não encontrada. Confira o ID informado."
        )
    else:
        exibir_detalhes_ave(ave_encontrada)


# ============================================================
# BUSCA TEXTUAL
# ============================================================

def criar_texto_busca(ave):
    # Monta um texto único com os campos utilizados na busca.
    valores = []

    for campo in CAMPOS_BUSCA:
        valores.append(str(ave.get(campo, "")))

    texto = " ".join(valores)

    # Normaliza o texto para facilitar a pesquisa.
    return normalizar_texto(texto)


def buscar_aves(catalogo, termo_busca):
    # Procura aves que contenham o termo informado pelo usuário.
    resultados = []

    # Normaliza o termo antes de iniciar a busca.
    termo = normalizar_texto(termo_busca)

    # Percorre todas as aves cadastradas.
    for ave in catalogo:
        texto_busca = criar_texto_busca(ave)

        # Adiciona a ave caso o termo seja encontrado.
        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def exibir_resultados_busca(resultados):
    # Exibe as aves encontradas durante a pesquisa.
    titulo("RESULTADOS DA BUSCA")

    if len(resultados) == 0:
        mensagem_aviso("Nenhuma ave encontrada.")

    else:
        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )


def tela_busca(catalogo):
    # Controla todo o processo de pesquisa de aves.
    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        mensagem_aviso(
            "Digite algum texto para realizar a busca."
        )
        return

    resultados = buscar_aves(catalogo, termo)

    exibir_resultados_busca(resultados)

    if len(resultados) > 0:
        escolha = input(
            "\nDigite o ID para ver detalhes ou ENTER para voltar: "
        ).strip()

        if escolha != "":
            ave_encontrada = buscar_ave_por_id(
                resultados,
                escolha
            )

            if ave_encontrada is None:
                mensagem_aviso(
                    "ID não encontrado nos resultados."
                )
            else:
                exibir_detalhes_ave(ave_encontrada)


# ============================================================
# COMPARAÇÃO ENTRE AVES
# ============================================================

def imprimir_linha_comparacao(rotulo, valor_1, valor_2):
    # Exibe uma linha alinhada com os dados das duas aves.
    print(
        f"{rotulo:<18} | "
        f"{str(valor_1):<25} | "
        f"{str(valor_2):<25}"
    )


def preparar_valor_comparacao(ave, campo, unidade):
    # Obtém o valor original armazenado no cadastro da ave.
    valor = ave.get(campo)

    # Reduz textos longos, como o habitat, para manter
    # a organização visual da tabela.
    if campo == "habitat":
        return cortar_texto(valor, 25)

    return valor_ou_indisponivel(valor, unidade)


def exibir_comparacao_aves(ave_1, ave_2):
    # Exibe as informações das duas aves lado a lado.
    print()
    print(linha("=", 78))
    print("COMPARAÇÃO ENTRE AVES")
    print(linha("=", 78))

    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print(linha("-", 78))

    # Percorre os campos definidos para a comparação.
    for rotulo, campo, unidade in CAMPOS_COMPARACAO:
        valor_1 = preparar_valor_comparacao(
            ave_1,
            campo,
            unidade
        )

        valor_2 = preparar_valor_comparacao(
            ave_2,
            campo,
            unidade
        )

        imprimir_linha_comparacao(
            rotulo,
            valor_1,
            valor_2
        )


def escolher_ave(catalogo, mensagem):
    # Lista as aves e solicita ao usuário um ID.
    listar_aves(catalogo)

    id_escolhido = input(
        f"\n{mensagem}: "
    ).strip()

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        mensagem_aviso(
            "Ave não encontrada. Confira o ID informado."
        )
        return None

    return ave_encontrada


def comparar_duas_aves(catalogo):
    # Controla a seleção das duas aves que serão comparadas.
    print()
    print("Escolha a primeira ave")

    ave_1 = escolher_ave(
        catalogo,
        "Digite o ID da primeira ave"
    )

    if ave_1 is None:
        return

    print()
    print("Escolha a segunda ave")

    ave_2 = escolher_ave(
        catalogo,
        "Digite o ID da segunda ave"
    )

    if ave_2 is None:
        return

    # Exibe a comparação entre as aves escolhidas.
    exibir_comparacao_aves(ave_1, ave_2)


# ============================================================
# DADOS DO CATÁLOGO
# ============================================================

catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "comprimento_cm": 23,
        "peso_g": 68,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 20,
        "peso_g": 49,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 13,
        "peso_g": 20,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    }
]


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

opcao_menu = ""

# Mantém o sistema em execução enquanto o usuário
# não escolher a opção de saída.
while opcao_menu != "0":

    # Exibe o menu principal.
    exibir_menu()

    # Recebe a opção escolhida pelo usuário.
    opcao_menu = input(
        "Escolha uma opção: "
    ).strip()

    # Lista todas as aves cadastradas.
    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    # Realiza uma busca textual.
    elif opcao_menu == "2":
        tela_busca(catalogo_aves)

    # Exibe os detalhes de uma ave.
    elif opcao_menu == "3":
        selecionar_ave_por_id(catalogo_aves)

    # Compara duas aves escolhidas pelo usuário.
    elif opcao_menu == "4":
        comparar_duas_aves(catalogo_aves)

    # Exibe informações sobre o projeto AveDex.
    elif opcao_menu == "5":
        print("A AveDex é um catálogo interativo de aves.")
        print(
            "Em breve, teremos batalha, imagens, sons "
            "e dados em arquivo JSON."
        )

    # Encerra o programa.
    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    # Trata opções que não existem no menu.
    else:
        mensagem_aviso(
            "Opção inválida. Digite apenas 0, 1, 2, 3, 4 ou 5."
        )

    # Pausa a tela antes de retornar ao menu.
    if opcao_menu != "0":
        pausar()
