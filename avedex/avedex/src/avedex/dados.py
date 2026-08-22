import json
from pathlib import Path


# __file__ representa o caminho deste arquivo dados.py.
# Como dados.py está em src/avedex/dados.py, usamos parents[2]
# para chegar à raiz do projeto.
CAMINHO_PROJETO = Path(__file__).resolve().parents[2]


# Caminho do arquivo JSON usado pela AveDex.
CAMINHO_DATASET = (
    CAMINHO_PROJETO
    / "data"
    / "avedex_dataset_midias.json"
)


def carregar_dataset(caminho=CAMINHO_DATASET):
    # Abre o arquivo JSON em modo leitura.
    # encoding="utf-8" evita problemas com acentos.
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dataset = json.load(arquivo)

    return dataset


def carregar_aves():
    # Carrega o dataset completo.
    dataset = carregar_dataset()

    # Retorna apenas a lista de aves.
    # Se a chave "aves" não existir, retorna lista vazia.
    return dataset.get("aves", [])


def obter_fontes_globais():
    # Carrega o dataset completo.
    dataset = carregar_dataset()

    # Retorna as fontes gerais cadastradas no JSON.
    return dataset.get("fontes_globais", {})
if __name__ == "__main__":
    aves = carregar_aves()

    print(f"Total de aves carregadas: {len(aves)}")

    for ave in aves:
        print(ave["nome_popular"])