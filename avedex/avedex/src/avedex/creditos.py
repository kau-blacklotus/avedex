from src.avedex.dados import obter_fontes_globais
from src.avedex.utils import titulo


def mostrar_creditos():
    # Mostra informações gerais do projeto e suas fontes.
    titulo("CRÉDITOS E FONTES")

    print("A AveDex é um catálogo interativo de aves.")
    print(
        "Projeto desenvolvido na disciplina de "
        "Boas Práticas de Programação."
    )

    print()
    print("Professor: João Paulo F. C. César")
    print("Curso: Análise e Desenvolvimento de Sistemas")
    print("Instituição: IFMG Campus Ouro Preto")

    print()
    print("Fontes globais")

    fontes = obter_fontes_globais()

    if not fontes:
        print("Nenhuma fonte global informada no dataset.")
    else:
        for nome, url in fontes.items():
            print(f"- {nome}: {url}")