import json
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Medicamento:
    def __init__(self, codigo, nome, categoria, quantidade, validade):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.validade = validade

    def __str__(self):
        return f"\nCódigo: {self.codigo}\nNome: {self.nome}\nCategoria: {self.categoria}\nQuantidade: {self.quantidade}\nValidade: {self.validade}\n\n"

def adicionar_medicamento(medicamentos):
    codigo = input("Digite o código do medicamento: ")
    nome = input("Digite o nome do medicamento: ")
    categoria = input("Digite a categoria do medicamento: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    validade = input("Digite a data de validade (DD/MM/AAAA): ")
    novo_medicamento = Medicamento(codigo, nome, categoria, quantidade, validade)
    medicamentos.append(novo_medicamento)
    print("Medicamento adicionado com sucesso!")

def atualizar_quantidade(medicamentos):
    codigo = input("Digite o código do medicamento a ser atualizado: ")
    nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
    for medicamento in medicamentos:
        if medicamento.codigo == codigo:
            medicamento.quantidade = nova_quantidade
            print("Quantidade atualizada com sucesso!")
            return
    print("Medicamento não encontrado.")

def remover_medicamento(medicamentos):
    codigo = input("Digite o código do medicamento a ser removido: ")
    for i, medicamento in enumerate(medicamentos):
        if medicamento.codigo == codigo:
            del medicamentos[i]
            print("Medicamento removido com sucesso!")
            return
    print("Medicamento não encontrado.")

def procurar_por_nome(medicamentos):
    nome = input("Digite o nome do medicamento a ser procurado: ")
    for medicamento in medicamentos:
        if nome.lower() in medicamento.nome.lower():
            print(medicamento)

def procurar_por_categoria(medicamentos):
    categoria = input("Digite a categoria do medicamento a ser procurado: ")
    for medicamento in medicamentos:
        if medicamento.categoria.lower() == categoria.lower():
            print(medicamento)

def menor_quantidade(medicamentos):
    menor_quantidade = float('inf')
    medicamento_menor_quantidade = None
    for medicamento in medicamentos:
        if medicamento.quantidade < menor_quantidade:
            menor_quantidade = medicamento.quantidade
            medicamento_menor_quantidade = medicamento
    print(f"O medicamento com menor quantidade em estoque é: {medicamento_menor_quantidade}")

def salvar_em_json(medicamentos, arquivo="medicamentos.json"):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump([medicamento.__dict__ for medicamento in medicamentos], f, indent=4)

def carregar_de_json():
    arquivos_json = [f for f in os.listdir() if f.endswith('.json')]
    if not arquivos_json:
        print("Nenhum arquivo JSON encontrado.")
        return []
    
    print("Arquivos JSON encontrados:")
    for i, arquivo in enumerate(arquivos_json, 1):
        print(f"{i}. {arquivo}")
    
    escolha = int(input("Escolha um arquivo para carregar: "))
    arquivo_escolhido = arquivos_json[escolha - 1]

    try:
        with open(arquivo_escolhido, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            medicamentos = []
            for dado in dados:
                medicamento = Medicamento(**dado)
                medicamentos.append(medicamento)
            return medicamentos
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return []

def menu():
    print("\nMenu:")
    print("1. Adicionar medicamento")    
    print("2. Atualizar quantidade")
    print("3. Remover medicamento")
    print("4. Procurar por nome")
    print("5. Procurar por categoria")
    print("6. Menor quantidade")
    print("7. Sair e salvar")
    print("0. Sair sem salvar\n")

if __name__ == "__main__":

    medicamentos = carregar_de_json()
    if medicamentos:
        while True:
            menu()
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                adicionar_medicamento(medicamentos)
            elif opcao == '2':
                atualizar_quantidade(medicamentos)
            elif opcao == '3':
                remover_medicamento(medicamentos)
            elif opcao == '4':
                procurar_por_nome(medicamentos)
            elif opcao == '5':
                procurar_por_categoria(medicamentos)
                input()
                limpar_tela()
            elif opcao == '6':
                menor_quantidade(medicamentos)
            elif opcao == '7':
                salvar_em_json(medicamentos)
                print("Dados salvos em JSON com sucesso!")
                break
            elif opcao == '0':
                print("Saindo sem salvar.")
                break
            else:
                print("Opção inválida.")
    else:
        print("Não há medicamentos para carregar.")
