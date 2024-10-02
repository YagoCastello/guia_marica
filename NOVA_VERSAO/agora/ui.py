import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import menu
import main
import categorias
import galeria

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        ctk.set_appearance_mode("dark")
        menu.theme_button.configure(text="Modo Claro")
    else:
        ctk.set_appearance_mode("light")
        menu.theme_button.configure(text="Modo Escuro")

    transparent_windows = [main.header, main.menu_frame, main.search_frame]

    for component in transparent_windows:
        component.configure(fg_color=main.app.cget("bg"))



# Tema inicial
dark_mode = False
ctk.set_appearance_mode("light")

       
# Limpar o frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        

def load_icons():
    # Carrega os ícones diretamente da pasta "icons" (no mesmo diretório que o arquivo Python)
    icons = {
        "home": ImageTk.PhotoImage(Image.open("icons/home.png").resize((30, 30))),
        "explorar": ImageTk.PhotoImage(Image.open("icons/explorar.png").resize((30, 30))),
        "favoritos": ImageTk.PhotoImage(Image.open("icons/favorito.png").resize((30, 30))),
        "opcoes": ImageTk.PhotoImage(Image.open("icons/opcoes.png").resize((30, 30)))
    }
    return icons

# Lógica da Pesquisa
def search_action(query):
    # Lista de todas as categorias disponíveis
    all_items = categorias.explorar_praia()[1] + categorias.explorar_bares()[1] + categorias.explorar_restaurantes()[1] +categorias.explorar_trilhas()[1]+categorias.explorar_cultura()[1] + categorias.explorar_lagoas()[1]+categorias.explorar_boates()[1] + categorias.explorar_hoteis_e_pousados()[1]+categorias.explorar_estacionamento()[1]

    # Filtrar os itens
    filtered_items = [item for item in all_items if query in item["name"].lower()]
    galeria.show_content(filtered_items)



all_items = [] 
