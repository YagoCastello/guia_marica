import customtkinter as ctk
from tkinter import *
import categorias
import ui
import main
from galeria import show_content
from favoritos import favorite_states


# Menu 'Inicio'
def show_home():
    ui.clear_frame(main.main_frame)
    home_label = ctk.CTkLabel(master=main.main_frame, text="Bem-vindo à Maricá City!", font=("Arial", 18, "bold"))
    home_label.pack(pady=20)

# Menu 'Explorar'
def show_explore_menu():
    ui.clear_frame(main.main_frame)
    explore_options = [categorias.explorar_praia, categorias.explorar_bares,categorias.explorar_restaurantes,categorias.explorar_trilhas,categorias.explorar_cultura,categorias.explorar_lagoas,categorias.explorar_boates,categorias.explorar_hoteis_e_pousados,categorias.explorar_estacionamento]

    for option_func in explore_options:
        button_name, content = option_func()
        button = ctk.CTkButton(master=main.main_frame, text=button_name, command=lambda c=content: show_content(c), fg_color="red")
        button.pack(pady=10, padx=20, side= "top", anchor= "w")


# Menu 'Opções'

# PARTE 2 MODIFICACOES
def show_favorites_menu():
    ui.clear_frame(main.main_frame)
    favoritos_label = ctk.CTkLabel(master=main.main_frame, text="Favoritos", font=("Arial", 18, "bold"))
    favoritos_label.pack(pady=20)

    # Filtrar os itens favoritos de qualquer categoria
    favorite_items = []
    for item_name, is_favorite in favorite_states.items():
        if is_favorite:
            for category in [categorias.explorar_praia(), categorias.explorar_bares(),categorias.explorar_restaurantes(),categorias.explorar_trilhas(),categorias.explorar_cultura(),categorias.explorar_lagoas(),categorias.explorar_boates(),categorias.explorar_hoteis_e_pousados(),categorias.explorar_estacionamento()]:
                for item in category[1]:
                    if item["name"] == item_name:
                        favorite_items.append(item)

    show_content(favorite_items)

# PARTE 2 MODIFICACOES FIM !!!!
def show_options_menu():
    ui.clear_frame(main.main_frame)
    global theme_button
    theme_button = ctk.CTkButton(master=main.main_frame, text="Modo Escuro", command=ui.toggle_theme, fg_color="red")
    theme_button.pack(pady=10, padx=20)
