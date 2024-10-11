from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage, set_appearance_mode
import customtkinter as ctk
from PIL import Image, ImageTk
from favoritos import toggle_favorite, on_enter, on_leave
from galeria import show_content, show_gallery, update_main_image, clear_frame
from categorias import (explorar_praia, explorar_bares, explorar_restaurantes, 
                        explorar_trilhas, explorar_cultura, explorar_lagoas, 
                        explorar_boates, explorar_hoteis_e_pousados, explorar_estacionamento)


# Configurar modo claro/ escuro
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        set_appearance_mode("dark")
        theme_button.configure(text="Modo Claro")
    else:
        set_appearance_mode("light")
        theme_button.configure(text="Modo Escuro")

    transparent_windows = [header, menu_frame, search_frame]

    for component in transparent_windows:
        component.configure(fg_color=app.cget("bg"))

# Lógica da Pesquisa
def search_action(query):
    all_items = (explorar_praia()[1] + explorar_bares()[1] + explorar_restaurantes()[1] 
                 + explorar_trilhas()[1] + explorar_cultura()[1] + explorar_lagoas()[1] 
                 + explorar_boates()[1] + explorar_hoteis_e_pousados()[1] + explorar_estacionamento()[1])

    # Filtrar os itens apenas se a query não estiver vazia
    if query.strip():  # Check if the query is not just whitespace
        filtered_items = [item for item in all_items if query.lower() in item["name"].lower()]
    else:
        filtered_items = []  # If no query, return an empty list

    show_content(main_frame, filtered_items)


# Carrega os ícones diretamente da pasta "icons"
def load_icons():
    icons = {
        "home": CTkImage(Image.open("icons/home.png"), size=(25, 25)),
        "explorar": CTkImage(Image.open("icons/explorar.png"), size=(25, 25)),
        "favoritos": CTkImage(Image.open("icons/favorito.png"), size=(25, 25)),
        "opcoes": CTkImage(Image.open("icons/opcoes.png"), size=(25, 25))
    }
    return icons

def show_gallery_callback(place):
    show_gallery(main_frame, place)

# Menu 'Inicio'
def show_home():
    clear_frame(main_frame)
    home_label = CTkLabel(master=main_frame, text="Bem-vindo à Maricá City!", font=("Arial", 18, "bold"))
    home_label.pack(pady=20)

# Menu 'Explorar'
def show_explore_menu():
    clear_frame(main_frame)
    scrollable_frame = ctk.CTkScrollableFrame(master=main_frame)
    scrollable_frame.pack(fill="both", expand=True)
    explore_options = [explorar_praia, explorar_bares, explorar_restaurantes, explorar_trilhas,
                       explorar_cultura, explorar_lagoas, explorar_boates,
                       explorar_hoteis_e_pousados, explorar_estacionamento]

    for option_func in explore_options:
        button_name, content, img_path = option_func()
        # Carregar e redimensionar a imagem
        pil_image = Image.open(img_path)
        resized_image = pil_image.resize((550, 100), Image.BICUBIC)

        # Criar uma imagem CTk
        ct_image = ctk.CTkImage(resized_image, size=(550, 100))

        button = ctk.CTkButton(master=scrollable_frame, text=button_name, command=lambda c=content: show_content(main_frame, c),
                               text_color="red", font=("Arial", 14, "bold"), fg_color="transparent", width=550,
                               height=100, image=ct_image, compound="top")
        button.pack(pady=5, padx=5, anchor="center", fill="x")
    # for option_func in explore_options:
    #     button_name, content = option_func()
    #     button = CTkButton(master=main_frame, text=button_name,
    #                        command=lambda c=content: show_content(main_frame, c),
    #                        fg_color="red")
    #     button.pack(pady=10, padx=20, side="top", anchor="w")

# Menu 'favoritos'
def show_favorites_menu():
    from favoritos import favorite_states
    clear_frame(main_frame)
    favoritos_label = CTkLabel(master=main_frame, text="Favoritos", font=("Arial", 18, "bold"))
    favoritos_label.pack(pady=20)

    # Filtrar os itens favoritos de qualquer categoria
    favorite_items = []
    for item_name, is_favorite in favorite_states.items():
        if is_favorite:
            for category in [explorar_praia(), explorar_bares(), explorar_restaurantes(), explorar_trilhas(), explorar_cultura()
                             , explorar_lagoas(), explorar_boates(), explorar_hoteis_e_pousados(), explorar_estacionamento()]:
                for item in category[1]:
                    if item["name"] == item_name:
                        favorite_items.append(item)

    show_content(main_frame, favorite_items)

# Menu 'Opções'
def show_options_menu():
    clear_frame(main_frame)
    global theme_button
    theme_button = CTkButton(master=main_frame, text="Modo Escuro", command=toggle_theme, fg_color="red")
    theme_button.pack(pady=10, padx=20)

#################### APLICATIVO ####################
app = CTk()
app.geometry("800x600")
app.title("Marica City")
app.resizable(width=False, height=False)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

# Nome MARICA CITY
header = CTkFrame(app, width=260, fg_color=app.cget("bg"))
header.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=(0, 10))

header_label = CTkLabel(header, text="MARICA CITY", text_color="red", font=("Arial", 20, "bold"))
header_label.grid(row=0, column=0, pady=10, padx=10)

# Botao de pesquisa
search_frame = CTkFrame(app, width=300, height=50, fg_color=app.cget("bg"))
search_frame.grid(row=0, column=1, sticky="ew", padx=(10, 0))

search_entry = CTkEntry(search_frame, width=200)
search_entry.grid(row=0, column=0, padx=(10, 0), pady=10)

search_button = CTkButton(search_frame, text="Pesquisar", command=lambda: search_action(search_entry.get().lower()), fg_color="red")
search_button.grid(row=0, column=1, padx=(5, 0), pady=10)

# Frame principal
main_frame = CTkFrame(master=app)
main_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

menu_frame = CTkFrame(master=app, fg_color=app.cget("bg"))
menu_frame.grid(row=1, column=0, sticky="ns", pady=(0, 10))

# Botoes da esquerda / MENU
icon = load_icons()
menu_buttons = [
    {"text": "   Inicio   ", "command": show_home, "icon": icon["home"]},
    {"text": " Explorar", "command": show_explore_menu, "icon": icon["explorar"]},
    {"text": "Favoritos", "command": show_favorites_menu, "icon": icon["favoritos"]},
    {"text": " Opções  ", "command": show_options_menu, "icon": icon["opcoes"]}
]

for index, btn in enumerate(menu_buttons):
    CTkButton(
        master=menu_frame,
        text=btn["text"],
        command=btn["command"],
        image=btn["icon"],
        compound="left",
        fg_color="red",
        width=150,
        height=40
    ).grid(row=index, column=0, pady=10, padx=10)

# Tema inicial
dark_mode = False
set_appearance_mode("light")

show_home()
app.mainloop()
