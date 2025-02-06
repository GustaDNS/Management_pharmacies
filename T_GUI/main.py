import tkinter as tk
from tkinter import messagebox
import json
import os

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    if os.path.exists("medicamentos.json"):
        with open("medicamentos.json", "r") as file:
            return json.load(file)
    else:
        return []

# Função para salvar os dados no arquivo JSON
def salvar_dados(medicamentos):
    with open("medicamentos.json", "w") as file:
        json.dump(medicamentos, file, indent=4)

# Função para adicionar um novo medicamento
def adicionar_medicamento():
    codigo = entry_codigo.get()
    nome = entry_nome.get()
    categoria = entry_categoria.get()
    quantidade = entry_quantidade.get()
    validade = entry_validade.get()

    if not codigo or not nome or not categoria or not quantidade or not validade:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios")
        return

    if quantidade.isdigit() == False:
        messagebox.showerror("Erro", "Quantidade deve ser um número")
        return

    quantidade = int(quantidade)

    medicamento = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "validade": validade
    }

    medicamentos = carregar_dados()
    medicamentos.append(medicamento)
    salvar_dados(medicamentos)

    messagebox.showinfo("Sucesso", "Medicamento adicionado com sucesso")
    limpar_campos()

# Função para atualizar a quantidade em stock
def atualizar_quantidade():
    codigo = entry_codigo.get()
    nova_quantidade = entry_quantidade.get()

    if not codigo or not nova_quantidade:
        messagebox.showerror("Erro", "Código e nova quantidade são obrigatórios")
        return

    if nova_quantidade.isdigit() == False:
        messagebox.showerror("Erro", "Quantidade deve ser um número")
        return

    nova_quantidade = int(nova_quantidade)

    medicamentos = carregar_dados()
    medicamento_encontrado = False
    for medicamento in medicamentos:
        if medicamento["codigo"] == codigo:
            medicamento["quantidade"] = nova_quantidade
            salvar_dados(medicamentos)
            messagebox.showinfo("Sucesso", "Quantidade atualizada com sucesso")
            medicamento_encontrado = True
            break

    if not medicamento_encontrado:
        messagebox.showerror("Erro", "Medicamento não encontrado")

# Função para remover um medicamento
def remover_medicamento():
    codigo = entry_codigo.get()

    if not codigo:
        messagebox.showerror("Erro", "Código é obrigatório")
        return

    medicamentos = carregar_dados()
    medicamento_encontrado = False
    for i, medicamento in enumerate(medicamentos):
        if medicamento["codigo"] == codigo:
            del medicamentos[i]
            salvar_dados(medicamentos)
            messagebox.showinfo("Sucesso", "Medicamento removido com sucesso")
            medicamento_encontrado = True
            break

    if not medicamento_encontrado:
        messagebox.showerror("Erro", "Medicamento não encontrado")

# Função para procurar medicamento por nome
def procurar_por_nome():
    nome = entry_nome.get()

    if not nome:
        messagebox.showerror("Erro", "Nome é obrigatório")
        return

    medicamentos = carregar_dados()
    resultados = [med for med in medicamentos if nome.lower() in med["nome"].lower()]

    if resultados:
        resultado_str = "\n".join([f"{med['nome']} - {med['quantidade']} em stock" for med in resultados])
        messagebox.showinfo("Resultado", resultado_str)
    else:
        messagebox.showinfo("Resultado", "Nenhum medicamento encontrado")

# Função para procurar medicamento por categoria
def procurar_por_categoria():
    categoria = entry_categoria.get()

    if not categoria:
        messagebox.showerror("Erro", "Categoria é obrigatória")
        return

    medicamentos = carregar_dados()
    resultados = [med for med in medicamentos if categoria.lower() in med["categoria"].lower()]

    if resultados:
        resultado_str = "\n".join([f"{med['nome']} - {med['quantidade']} em stock" for med in resultados])
        messagebox.showinfo("Resultado", resultado_str)
    else:
        messagebox.showinfo("Resultado", "Nenhum medicamento encontrado")

# Função para determinar o medicamento com menor quantidade em stock
def medicamento_com_menor_stock():
    medicamentos = carregar_dados()

    if not medicamentos:
        messagebox.showinfo("Resultado", "Não há medicamentos registrados")
        return

    medicamento = min(medicamentos, key=lambda x: x["quantidade"])
    messagebox.showinfo("Resultado", f"Medicamento com menor quantidade: {medicamento['nome']} ({medicamento['quantidade']} em stock)")

# Função para limpar os campos
def limpar_campos():
    entry_codigo.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_validade.delete(0, tk.END)


# Configuração da interface gráfica
root = tk.Tk()
root.title("Gestão de Medicamentos")
root.geometry("600x500")  # Define o tamanho da janela
root.config(bg="#f5f5f5")  # Cor de fundo da janela

# Frame para agrupar os campos
frame_campos = tk.Frame(root, bg="#f5f5f5")
frame_campos.pack(pady=20)

# Definindo os campos e títulos
label_codigo = tk.Label(frame_campos, text="Código", font=("Arial", 12), bg="#f5f5f5")
label_codigo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_codigo = tk.Entry(frame_campos, font=("Arial", 12))
entry_codigo.grid(row=0, column=1, padx=10, pady=10)

label_nome = tk.Label(frame_campos, text="Nome", font=("Arial", 12), bg="#f5f5f5")
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_nome = tk.Entry(frame_campos, font=("Arial", 12))
entry_nome.grid(row=1, column=1, padx=10, pady=10)

label_categoria = tk.Label(frame_campos, text="Categoria", font=("Arial", 12), bg="#f5f5f5")
label_categoria.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_categoria = tk.Entry(frame_campos, font=("Arial", 12))
entry_categoria.grid(row=2, column=1, padx=10, pady=10)

label_quantidade = tk.Label(frame_campos, text="Quantidade", font=("Arial", 12), bg="#f5f5f5")
label_quantidade.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_quantidade = tk.Entry(frame_campos, font=("Arial", 12))
entry_quantidade.grid(row=3, column=1, padx=10, pady=10)

label_validade = tk.Label(frame_campos, text="Data de Validade", font=("Arial", 12), bg="#f5f5f5")
label_validade.grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_validade = tk.Entry(frame_campos, font=("Arial", 12))
entry_validade.grid(row=4, column=1, padx=10, pady=10)

# Frame para os botões
frame_botoes = tk.Frame(root, bg="#f5f5f5")
frame_botoes.pack(pady=20)

# Botões
button_adicionar = tk.Button(frame_botoes, text="Adicionar Medicamento", font=("Arial", 12), bg="#4CAF50", fg="white", command=adicionar_medicamento)
button_adicionar.grid(row=0, column=0, padx=20, pady=10)

button_atualizar = tk.Button(frame_botoes, text="Atualizar Quantidade", font=("Arial", 12), bg="#FFA500", fg="white", command=atualizar_quantidade)
button_atualizar.grid(row=0, column=1, padx=20, pady=10)

button_remover = tk.Button(frame_botoes, text="Remover Medicamento", font=("Arial", 12), bg="#f44336", fg="white", command=remover_medicamento)
button_remover.grid(row=0, column=2, padx=20, pady=10)

button_procurar_nome = tk.Button(frame_botoes, text="Procurar por Nome", font=("Arial", 12), bg="#2196F3", fg="white", command=procurar_por_nome)
button_procurar_nome.grid(row=1, column=0, padx=20, pady=10)

button_procurar_categoria = tk.Button(frame_botoes, text="Procurar por Categoria", font=("Arial", 12), bg="#2196F3", fg="white", command=procurar_por_categoria)
button_procurar_categoria.grid(row=1, column=1, padx=20, pady=10)

button_menor_stock = tk.Button(frame_botoes, text="Menor Quantidade", font=("Arial", 12), bg="#9C27B0", fg="white", command=medicamento_com_menor_stock)
button_menor_stock.grid(row=1, column=2, padx=20, pady=10)

button_limpar = tk.Button(frame_botoes, text="Limpar Campos", font=("Arial", 12), bg="#607D8B", fg="white", command=limpar_campos)
button_limpar.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
