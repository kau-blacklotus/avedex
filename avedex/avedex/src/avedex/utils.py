import unicodedata

# Largura padrão usada nos títulos e linhas de separação.
LARGURA_TELA = 78


def linha(caractere="=", largura=LARGURA_TELA):
    # Retorna uma linha formada pela repetição de um caractere.
    # Exemplo: linha("=") retorna "====..."
    return caractere * largura


def titulo(texto):
    # Exibe um título padronizado no terminal.
    print()
    print(linha("="))
    print(texto)
    print(linha("="))


def mensagem_sucesso(texto):
    # Mostra uma mensagem positiva para o usuário.
    print(f"[OK] {texto}")


def mensagem_aviso(texto):
    # Mostra uma mensagem de atenção.
    print(f"[AVISO] {texto}")


def mensagem_erro(texto):
    # Mostra uma mensagem de erro.
    print(f"[ERRO] {texto}")


def pausar():
    # Pausa o programa para o usuário conseguir ler a tela.
    input("\nPressione ENTER para voltar ao menu...")


def normalizar_texto(texto):
    # Converte o valor recebido para texto.
    texto = str(texto)

    # Padroniza minúsculas e remove espaços extras.
    texto = texto.lower().strip()

    # Separa letras e acentos.
    texto = unicodedata.normalize("NFD", texto)

    # Remove os sinais de acentuação.
    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def valor_ou_indisponivel(valor, unidade=""):
    # Trata valores ausentes ou vazios.
    if valor is None or valor == "":
        return "Não informado"

    # Acrescenta unidade quando necessário.
    if unidade != "":
        return f"{valor} {unidade}"

    return str(valor)


def cortar_texto(texto, tamanho=25):
    # Evita que textos longos quebrem a comparação lado a lado.
    if texto is None:
        return "Não informado"

    texto = str(texto).strip()

    if len(texto) <= tamanho:
        return texto

    return texto[: tamanho - 3] + "..."
