from src.avedex.utils import titulo, linha


OPCOES_MENU = [
    "1 - Listar aves",
    "2 - Buscar ave",
    "3 - Ver detalhes de uma ave",
    "4 - Comparar duas aves",
    "5 - Créditos e fontes",
    "0 - Sair",
]


def abertura(aves):
    # Mostra uma abertura simples do sistema.
    titulo("BEM-VINDO AO AVEDEX")

    print("Catálogo interativo de aves.")
    print(f"Total de aves carregadas: {len(aves)}")
    print(linha("-"))


def exibir_menu_principal():
    # Mostra o menu principal a partir da lista OPCOES_MENU.
    titulo("AVEDEX - MENU PRINCIPAL")

    for opcao in OPCOES_MENU:
        print(opcao)