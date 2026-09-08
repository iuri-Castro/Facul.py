pacientes = []


def cadastrar_paciente():
    nome = input("Nome do paciente: ")
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida!")
        return
    telefone = input("Telefone: ")
    pacientes.append({"nome": nome, "idade": idade, "telefone": telefone})
    print("Paciente cadastrado com sucesso!\n")


def estatisticas():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return
    total = len(pacientes)
    media = sum(p["idade"] for p in pacientes) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])
    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.1f}")
    print(f"Mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)\n")


def buscar():
    nome = input("Digite o nome do paciente: ")
    for p in pacientes:
        if p["nome"].lower() == nome.lower():
            print(f"Encontrado: {p['nome']} - {p['idade']} anos - {p['telefone']}\n")
            return
    print("Paciente não encontrado.\n")


def listar():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return
    for p in pacientes:
        print(f"{p['nome']} - {p['idade']} anos - {p['telefone']}")
    print()


while True:
    print("=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")


    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        estatisticas()
    elif opcao == "3":
        buscar()
    elif opcao == "4":
        listar()
    elif opcao == "5":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida!\n")