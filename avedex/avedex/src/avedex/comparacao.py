from src.avedex.catalogo import escolher_ave
from src.avedex.utils import (
    linha,
    titulo,
    valor_ou_indisponivel,
    cortar_texto,
)


CAMPOS_COMPARACAO = [
    ("Nome científico", "nome_cientifico", ""),
    ("Ordem", "ordem", ""),
    ("Família", "familia", ""),
    ("Dieta", "dieta_tipo", ""),
    ("Habitat", "habitat", ""),
    ("Comprimento", "comprimento_cm", "cm"),
    ("Peso", "peso_g", "g"),
    ("Conservação", "status_conservacao", ""),
    ("Índice", "indice_conservacao", ""),
]


def imprimir_linha(rotulo, valor_1, valor_2):
    # Imprime uma linha alinhada da tabela de comparação.
    print(
        f"{rotulo:<18} | "
        f"{str(valor_1):<25} | "
        f"{str(valor_2):<25}"
    )


def preparar_valor(ave, campo, unidade):
    # Busca o valor original no dicionário da ave.
    valor = ave.get(campo)

    # Habitat pode ser longo, então cortamos para manter a tabela legível.
    if campo == "habitat":
        return cortar_texto(valor, 25)

    return valor_ou_indisponivel(valor, unidade)


def comparar_aves(aves):
    # Coordena a escolha e comparação de duas aves.
    titulo("COMPARAÇÃO DE AVES")

    ave_1 = escolher_ave(
        aves,
        "Digite o ID da primeira ave"
    )

    if ave_1 is None:
        return

    ave_2 = escolher_ave(
        aves,
        "Digite o ID da segunda ave"
    )

    if ave_2 is None:
        return

    titulo("COMPARAÇÃO LADO A LADO")

    imprimir_linha(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print(linha("-", 78))

    for rotulo, campo, unidade in CAMPOS_COMPARACAO:
        valor_1 = preparar_valor(
            ave_1,
            campo,
            unidade
        )

        valor_2 = preparar_valor(
            ave_2,
            campo,
            unidade
        )

        imprimir_linha(
            rotulo,
            valor_1,
            valor_2
        )