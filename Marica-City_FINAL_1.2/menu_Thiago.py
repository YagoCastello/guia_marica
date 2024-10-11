import customtkinter as ctk
from tkinter import *
import categorias
import ui
import main
from galeria import show_content
from favoritos import favorite_states
from PIL import Image, ImageTk


def show_home():
    ui.clear_frame(main.main_frame)
    home_label = ctk.CTkLabel(master=main.main_frame, text="Bem-vindo à Maricá City!", font=("Arial", 18, "bold"))
    home_label.pack(pady=20)
    # Carrega a imagem
    image_path = "images\logo.png"  # Use barras duplas
    image = Image.open(image_path)
    
    # Ajusta o tamanho da imagem (exemplo: 400x400)
    image = image.resize((400, 400), Image.LANCZOS)  # Altere os valores conforme necessário

    # Converte a imagem para um formato que o Canvas pode usar
    photo_image = ImageTk.PhotoImage(image)  # Usando ImageTk

    # Cria um Canvas para exibir a imagem
    canvas = ctk.CTkCanvas(master=main.main_frame, width=400, height=400)
    canvas.pack(pady=10, padx=10)

    # Adiciona a imagem ao Canvas
    canvas.create_image(200, 200, image=photo_image)  # Centraliza a imagem no Canvas

    # Mantém uma referência à imagem
    canvas.image = photo_image  # Isso é crucial para evitar que a imagem seja coletada pelo garbage collector

def show_explore_menu():
    ui.clear_frame(main.main_frame)
    scrollable_frame = ctk.CTkScrollableFrame(master=main.main_frame)
    scrollable_frame.pack(fill="both", expand=True)
    explore_options = [categorias.explorar_praia, categorias.explorar_bares,categorias.explorar_restaurantes,categorias.explorar_trilhas,categorias.explorar_cultura,categorias.explorar_lagoas,categorias.explorar_boates,categorias.explorar_hoteis_e_pousados,categorias.explorar_estacionamento]

    for option_func in explore_options:
        button_name, content ,img_path = option_func()
       # Carregar e redimensionar a imagem
        pil_image = Image.open(img_path)
        resized_image = pil_image.resize((550, 100), Image.BICUBIC)
        
        # Criar uma imagem CTk
        ct_image = ctk.CTkImage(resized_image, size=(550, 100))
        
        button = ctk.CTkButton(master=scrollable_frame,text=button_name ,command=lambda c=content: show_content(c),text_color="red",font=("Arial",14,"bold"), fg_color="transparent",width=550, height=100, image=ct_image, compound="top")
        button.pack(pady = 5,padx = 5, anchor="center", fill="x")


# Menu 'Opções'

# PARTE 2 MODIFICACOES
def show_favorites_menu():
    ui.clear_frame(main.main_frame)
    scrollable_frame = ctk.CTkScrollableFrame(master=main.main_frame)
    scrollable_frame.pack(fill="both", expand=True)
    favoritos_label = ctk.CTkLabel(master=scrollable_frame, text="Favoritos", font=("Arial", 18, "bold"))
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
