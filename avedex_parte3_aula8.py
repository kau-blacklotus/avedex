print("=" * 40)
print(" AVEDEX")
print("=" * 40)

nome_usuario = input("Digite seu nome: ").strip()

opcao_menu = ""

while opcao_menu != "0":
    print()
    print("=" * 40)
    print("MENU PRINCIPAL")
    print("=" * 40)
    print("1 - Ver mensagem de boas-vindas")
    print("2 - Conhecer uma ave")
    print("3 - Ver uma curiosidade sobre aves")
    print("4 - Sobre a AveDex")
    print("0 - Sair")

    opcao_menu = input("Escolha uma opção: ").strip()

    print()

    if opcao_menu == "1":
        print(f"Olá, {nome_usuario}!")
        print("Seja bem-vindo(a) à AveDex.")
        print("Aqui vamos conhecer aves e praticar boas práticas de programação.")

    elif opcao_menu == "2":
        print("Ave escolhida: Bem-te-vi")
        print("Nome científico: Pitangus sulphuratus")
        print("O bem-te-vi é uma das aves mais conhecidas do Brasil.")

    elif opcao_menu == "3":
        print("Curiosidade:")
        print("Muitas aves ajudam no equilíbrio ambiental ao dispersar sementes.")

    elif opcao_menu == "4":
        print("Sobre a AveDex:")
        print("A AveDex será um catálogo interativo de aves.")
        print("Ao longo da disciplina, adicionaremos novas funcionalidades.")

    elif opcao_menu == "0":
        print("Encerrando a AveDex.")
        print(f"Até logo, {nome_usuario}!")

    else:
        print("Opção inválida. Digite apenas 0, 1, 2, 3 ou 4.")

    if opcao_menu != "0":
        input("\nPressione ENTER para voltar ao menu...")
