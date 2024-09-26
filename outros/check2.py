import customtkinter as ctk
import json
import os

# Função para salvar checklist (texto e estado) em arquivo JSON
def salvar_checklist(checklist):
    with open("checklist.json", "w") as f:
        json.dump(checklist, f)

# Função para carregar checklist do arquivo JSON
def carregar_checklist():
    if os.path.exists("checklist.json"):
        with open("checklist.json", "r") as f:
            return json.load(f)
    return []

# Função para atualizar a checklist
def atualizar_checklist():
    checklist = []
    for i, item_var in enumerate(items_var):
        item_text = items_text[i].get()  # Obter o texto do item
        item_state = item_var.get()      # Obter o estado do item (marcado/desmarcado)
        checklist.append({"text": item_text, "state": item_state})
    salvar_checklist(checklist)

# Função para adicionar um novo item à checklist
def adicionar_item():
    novo_item = entry.get()
    if novo_item:
        var = ctk.IntVar(value=0)  # Iniciar novo item como desmarcado (0)
        text_var = ctk.StringVar(value=novo_item)

        items_var.append(var)
        items_text.append(text_var)

        checkbox = ctk.CTkCheckBox(frame, textvariable=text_var, variable=var, command=atualizar_checklist)
        checkbox.pack(anchor="w")
        entry.delete(0, ctk.END)
        atualizar_checklist()

# Configurando a janela principal
app = ctk.CTk()
app.title("Checklist")
app.geometry("300x400")

# Frame para os itens da checklist
frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=10, fill="both", expand=True)

# Lista para armazenar variáveis de estado (marcado/desmarcado) e texto dos itens
items_var = []
items_text = []

# Carregar checklist ao iniciar o app
checklist_salva = carregar_checklist()
for item in checklist_salva:
    var = ctk.IntVar(value=item["state"])  # Estado do checkbox (marcado/desmarcado)
    text_var = ctk.StringVar(value=item["text"])  # Texto do item

    items_var.append(var)
    items_text.append(text_var)

    checkbox = ctk.CTkCheckBox(frame, textvariable=text_var, variable=var, command=atualizar_checklist)
    checkbox.pack(anchor="w")

# Entrada de texto para adicionar novos itens
entry = ctk.CTkEntry(app, placeholder_text="Novo item")
entry.pack(pady=10)

# Botão para adicionar um item à checklist
botao_adicionar = ctk.CTkButton(app, text="Adicionar", command=adicionar_item)
botao_adicionar.pack()

app.mainloop()
