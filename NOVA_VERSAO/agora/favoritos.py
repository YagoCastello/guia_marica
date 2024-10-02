
from tkinter import *
from PIL import Image, ImageTk
import json
import os





def load_favorite_states():
    if os.path.exists("favorite_states.json"):
        with open("favorite_states.json", "r") as file:
            return json.load(file)
    return {}

# Função para salvar os estados favoritos em um arquivo JSON
def save_favorite_states():
    with open("favorite_states.json", "w") as file:
        json.dump(favorite_states, file)

# Inicializa os estados favoritos
favorite_states = load_favorite_states()

def toggle_favorite(button, item_name):
    # Verifica o estado atual do item
    is_favorite = favorite_states.get(item_name, False)

    # Atualizar o estado no dicionário
    favorite_states[item_name] = not is_favorite
    save_favorite_states()  # Salva os estados no arquivo JSON

    # Mudar o ícone com base no estado atual
    icon_path = "icons/favorito_active.png" if not is_favorite else "icons/favorito.png"
    img = Image.open(icon_path).resize((20, 20))
    image = ImageTk.PhotoImage(img)

    button.configure(image=image)
    button.image = image
    print(favorite_states)  # Log de verificação


# TESTE DE CODIGO NOVO TERMINA AQUI !!!!!!!!!!!!!! COD 1
# Toggle hover do icone de Favoritar
def on_enter(button, active_icon):
    # Trocar o ícone para o ativo ao passar o mouse
    img = Image.open(active_icon).resize((25, 25))
    image = ImageTk.PhotoImage(img)
    button.configure(image=image)
    button.image = image

def on_leave(button, item_name):
    # Trocar o ícone de volta com base no estado atual
    icon_path = "icons/favorito_active.png" if favorite_states.get(item_name, False) else "icons/favorito.png"
    img = Image.open(icon_path).resize((20, 20))
    image = ImageTk.PhotoImage(img)
    button.configure(image=image)
    button.image = image
