# === SISTEMA CLÍNICA VIDA+ ===
# Autor: Nallanda
# Objetivo: Cadastro e estatísticas de pacientes

# Lista para armazenar pacientes
pacientes = []
fila = []
def cadastrar_paciente():
    try:
        nome = input("Nome do paciente: ")
        idade = int(input("Idade: "))
        telefone = input("Telefone: ")
        paciente = {"nome": nome, "idade": idade, "telefone": telefone}
        pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!\n")
    except ValueError:
        print("Erro: idade deve ser um número.\n")

def ver_estatisticas():
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.\n")
        return
    
    total = len(pacientes)
    media_idade = sum(p["idade"] for p in pacientes) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])
    
    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media_idade:.1f}")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)\n")

def buscar_paciente():
    nome_busca = input("Digite o nome do paciente: ")
    encontrados = [p for p in pacientes if p["nome"].lower() == nome_busca.lower()]
    if encontrados:
        for p in encontrados:
            print(f"Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    else:
        print("Paciente não encontrado.\n")

def listar_pacientes():
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.\n")
    else:
        print("=== Lista de Pacientes ===")
        for p in pacientes:
            print(f"Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
        print()

def inserir_na_fila():
    try:
        nome = input("Nome do paciente: ")
        cpf = input("CPF: ")
        paciente = {"nome": nome, "cpf": cpf}
        fila.append(paciente)
        print("Paciente inserido na fila!\n")
    except Exception as e:
        print(f"Erro ao inserir paciente: {e}\n")

def atender_paciente():
    if len(fila) == 0:
        print("Nenhum paciente na fila.\n")
    else:
        paciente = fila.pop(0)  # remove o primeiro
        print(f"Paciente atendido: {paciente['nome']} | CPF: {paciente['cpf']}\n")

def mostrar_fila():
    if len(fila) == 0:
        print("Fila vazia.\n")
    else:
        print("=== Pacientes na fila ===")
        for p in fila:
            print(f"Nome: {p['nome']} | CPF: {p['cpf']}")
        print()

def menu():
    while True:
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Inserir paciente na fila (com CPF)")
        print("6. Atender paciente da fila")
        print("7. Mostrar fila de atendimento")
        print("8. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            inserir_na_fila()
        elif opcao == "6":
            atender_paciente()
        elif opcao == "7":
            mostrar_fila()
        elif opcao == "8":    
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o sistema
menu()