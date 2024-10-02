import customtkinter as ctk
from tkinter import *

import ui

import menu
#################### APLICATIVO ####################
app = ctk.CTk()
app.geometry("800x600")
app.title("Marica City")
app.resizable(width= False, height= False)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)




# Nome MARICA CITY
header = ctk.CTkFrame(app, width=260, fg_color=app.cget("bg"))
header.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=(0, 10))

header_label = ctk.CTkLabel(header, text="MARICA CITY", text_color= "red", font=("Arial", 20, "bold"))
header_label.grid(row=0, column=0, pady=10, padx=10)


# Botao de pesquisa
search_frame = ctk.CTkFrame(app, width=300, height=50, fg_color=app.cget("bg"))
search_frame.grid(row=0, column=1, sticky="ew", padx=(10, 0))

search_entry = ctk.CTkEntry(search_frame, width=200)
search_entry.grid(row=0, column=0, padx=(10, 0), pady=10)

search_button = ctk.CTkButton(search_frame, text="Pesquisar", command=lambda: ui.search_action(search_entry.get().lower()), fg_color= "red")
search_button.grid(row=0, column=1, padx=(5, 0), pady=10)


# Frame principal
main_frame = ctk.CTkFrame(master=app)
main_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

menu_frame = ctk.CTkFrame(master=app, fg_color=app.cget("bg"))
menu_frame.grid(row=1, column=0, sticky="ns", pady=(0, 10))

# Botoes da esquerda / MENU
icon = ui.load_icons()
menu_buttons = [
    {"text": "   Inicio   ", "command": menu.show_home, "icon": icon["home"]},  # Adiciona espaços extras para alinhar
    {"text": " Explorar", "command": menu.show_explore_menu, "icon": icon["explorar"]},
    {"text": "Favoritos", "command": menu.show_favorites_menu, "icon": icon["favoritos"]},
    {"text": " Opções  ", "command": menu.show_options_menu, "icon": icon["opcoes"]}
]

for index, btn in enumerate(menu_buttons):
    ctk.CTkButton(
        master=menu_frame,
        text=btn["text"],
        command=btn["command"],
        image=btn["icon"],
        compound="left",
        fg_color="red",
        width=150
    ).grid(row=index, column=0, pady=10, padx=10)



# # Exibe o menu inicial
# show_home()
# app.mainloop()
