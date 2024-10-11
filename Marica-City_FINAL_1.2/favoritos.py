from customtkinter import CTkImage
from PIL import Image
from json import load, dump


# Carregar os favoritos do .json
def load_favorite_states():
    try:
        with open("favorite_states.json", "r") as file:
            return load(file)
    except FileNotFoundError:
        return {}

# Salvar os favoritos no .json
def save_favorite_states():
    try:
        with open("favorite_states.json", "w") as file:
            dump(favorite_states, file)
    except FileNotFoundError:
        return {}

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
    img = Image.open(icon_path)
    image = CTkImage(img, size=(20,20))

    button.configure(image=image)
    button.image = image
    print(favorite_states)

# Toggle hover do icone de Favoritar
def on_enter(button, active_icon):
    img = Image.open(active_icon)
    image = CTkImage(img, size=(25,25))

    button.configure(image=image)
    button.image = image

def on_leave(button, item_name):
    icon_path = "icons/favorito_active.png" if favorite_states.get(item_name, False) else "icons/favorito.png"

    img = Image.open(icon_path)
    image = CTkImage(img)

    button.configure(image=image)
    button.image = image
