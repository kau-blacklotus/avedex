import unicodedata


def normalizar_texto(texto):
    # Converte o valor recebido para texto.
    texto = str(texto)

    # Padroniza para minúsculas e remove espaços extras.
    texto = texto.lower().strip()

    # Separa letras e acentos.
    texto = unicodedata.normalize("NFD", texto)

    # Remove os acentos.
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def pausar():
    # Pausa a execução para o usuário conseguir ler a tela.
    input("\nPressione ENTER para voltar ao menu...")


def exibir_menu():
    # Exibe as opções principais do sistema.
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Comparar duas aves")
    print("5 - Sobre a AveDex")
    print("0 - Sair")


def listar_aves(catalogo):
    # Mostra uma lista simples com ID e nome popular.
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    # Percorre o catálogo procurando o ID informado.
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave

    # Retorna None quando não encontra.
    return None


def valor_ou_indisponivel(valor, unidade=""):
    # Trata valor ausente.
    if valor is None or valor == "":
        return "Não informado"

    # Acrescenta unidade quando necessário.
    if unidade != "":
        return f"{valor} {unidade}"

    return str(valor)


def exibir_detalhes_ave(ave):
    # Exibe detalhes de uma única ave.
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
    # Mostra as aves e permite escolher uma pelo ID.
    listar_aves(catalogo)

    id_escolhido = input("\nDigite o ID da ave: ").strip()

    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)


def buscar_aves(catalogo, termo_busca):
    # Lista que receberá as aves encontradas.
    resultados = []

    # Normaliza o termo digitado.
    termo = normalizar_texto(termo_busca)

    for ave in catalogo:
        # Campos usados na busca.
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        texto_busca = " ".join(campos_busca)
        texto_busca = normalizar_texto(texto_busca)

        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def exibir_resultados_busca(resultados):
    # Exibe as aves encontradas pela busca.
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
    # Solicita um termo ao usuário.
    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return

    resultados = buscar_aves(catalogo, termo)
    exibir_resultados_busca(resultados)

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


def imprimir_linha_comparacao(rotulo, valor_1, valor_2):
    # Imprime uma linha alinhada da comparação.
    print(
        f"{rotulo:<18} | "
        f"{str(valor_1):<25} | "
        f"{str(valor_2):<25}"
    )


def exibir_comparacao_aves(ave_1, ave_2):
    # Exibe os dados das duas aves lado a lado.
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)

    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print("-" * 78)

    imprimir_linha_comparacao(
        "Nome científico",
        ave_1.get("nome_cientifico"),
        ave_2.get("nome_cientifico")
    )

    imprimir_linha_comparacao(
        "Ordem",
        ave_1.get("ordem"),
        ave_2.get("ordem")
    )

    imprimir_linha_comparacao(
        "Família",
        ave_1.get("familia"),
        ave_2.get("familia")
    )

    imprimir_linha_comparacao(
        "Dieta",
        ave_1.get("dieta_tipo"),
        ave_2.get("dieta_tipo")
    )

    imprimir_linha_comparacao(
        "Habitat",
        ave_1.get("habitat"),
        ave_2.get("habitat")
    )

    imprimir_linha_comparacao(
        "Comprimento",
        valor_ou_indisponivel(
            ave_1.get("comprimento_cm"),
            "cm"
        ),
        valor_ou_indisponivel(
            ave_2.get("comprimento_cm"),
            "cm"
        )
    )

    imprimir_linha_comparacao(
        "Peso",
        valor_ou_indisponivel(
            ave_1.get("peso_g"),
            "g"
        ),
        valor_ou_indisponivel(
            ave_2.get("peso_g"),
            "g"
        )
    )

    imprimir_linha_comparacao(
        "Conservação",
        ave_1.get(
            "status_conservacao",
            "Não informado"
        ),
        ave_2.get(
            "status_conservacao",
            "Não informado"
        )
    )

    imprimir_linha_comparacao(
        "Índice",
        ave_1.get(
            "indice_conservacao",
            "Não informado"
        ),
        ave_2.get(
            "indice_conservacao",
            "Não informado"
        )
    )


def escolher_ave(catalogo, mensagem):
    # Lista as aves e pede ao usuário o ID desejado.
    listar_aves(catalogo)

    id_escolhido = input(f"\n{mensagem}: ").strip()

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
        return None

    return ave_encontrada


def comparar_duas_aves(catalogo):
    # Escolhe a primeira ave.
    print()
    print("Escolha a primeira ave")

    ave_1 = escolher_ave(
        catalogo,
        "Digite o ID da primeira ave"
    )

    if ave_1 is None:
        return

    # Escolhe a segunda ave.
    print()
    print("Escolha a segunda ave")

    ave_2 = escolher_ave(
        catalogo,
        "Digite o ID da segunda ave"
    )

    if ave_2 is None:
        return

    # Exibe a comparação.
    exibir_comparacao_aves(ave_1, ave_2)


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
        comparar_duas_aves(catalogo_aves)

    elif opcao_menu == "5":
        print("A AveDex é um catálogo interativo de aves.")
        print(
            "Em breve, teremos batalha, imagens, sons "
            "e dados em arquivo JSON."
        )

    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    else:
        print(
            "Opção inválida. Digite apenas 0, 1, 2, 3, 4 ou 5."
        )

    if opcao_menu != "0":
        pausar()
# ============================================================
# CONFIGURAÇÕES GERAIS DA AVEDEX
# ============================================================
# Esta seção reúne constantes utilizadas em diferentes partes
# do sistema para facilitar manutenção e futuras expansões.
# ============================================================

# Define a largura padrão utilizada nos títulos, menus
# e linhas de separação exibidas no terminal.
LARGURA_TELA = 78

# Opções disponíveis no menu principal da AveDex.
# Cada item será exibido ao usuário para navegação
# pelas funcionalidades do sistema.
OPCOES_MENU = [
    "1 - Listar aves",
    "2 - Buscar ave",
    "3 - Ver detalhes de uma ave",
    "4 - Comparar duas aves",
    "5 - Sobre a AveDex",
    "0 - Sair"
]

# Campos considerados durante as pesquisas realizadas
# pelo usuário. A busca verifica se o termo digitado
# está presente em algum destes atributos da ave.
CAMPOS_BUSCA = [
    "nome_popular",
    "nome_cientifico",
    "familia",
    "ordem",
    "dieta_tipo"
]

# Campos exibidos na tela de comparação entre duas aves.
# Cada tupla contém:
# (Nome exibido ao usuário, chave do dicionário, unidade)
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
# FUNÇÕES DE INTERFACE DA AVEDEX
# ============================================================
# Funções responsáveis pela padronização da apresentação
# das informações e mensagens no terminal.
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
# ============================================================
# MENU PRINCIPAL DA AVEDEX
# ============================================================
# Função responsável por apresentar ao usuário as opções
# disponíveis no sistema.
# ============================================================

def exibir_menu():
    # Exibe o título do menu principal da AveDex.
    titulo("AVEDEX - MENU PRINCIPAL")

    # Percorre a lista de opções e exibe cada uma no terminal.
    for opcao in OPCOES_MENU:
        print(opcao)
# ============================================================
# PREPARAÇÃO DE DADOS PARA BUSCA
# ============================================================
# Função responsável por reunir e normalizar os dados de uma
# ave que poderão ser utilizados nas pesquisas da AveDex.
# ============================================================

def criar_texto_busca(ave):
    # Lista temporária que armazenará os valores dos campos
    # utilizados na pesquisa.
    valores = []

    # Percorre cada campo definido nas configurações de busca.
    for campo in CAMPOS_BUSCA:
        # Obtém o valor do campo no cadastro da ave.
        # Caso o campo não exista, utiliza um texto vazio.
        valores.append(str(ave.get(campo, "")))

    # Junta todos os valores em um único texto para pesquisa.
    texto = " ".join(valores)

    # Normaliza o texto para facilitar a localização dos dados,
    # ignorando diferenças entre maiúsculas, minúsculas e acentos.
    return normalizar_texto(texto)
