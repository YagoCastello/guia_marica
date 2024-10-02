
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import main
import ui 

import favoritos
import menu



def show_content(items):
    ui.clear_frame(main.main_frame)

    if not items:
        no_result_label = ctk.CTkLabel(master=main.main_frame, text="Nenhum resultado encontrado.", font=("Arial", 16, "bold"))
        no_result_label.pack(pady=20)
        return

    for item in items:
        frame = ctk.CTkFrame(master=main.main_frame, corner_radius=10)
        frame.pack(pady=10, padx=20, fill="x")

        try:
            print(f"Carregando a imagem: {item['image']}")  # Linha de depuração
            img = Image.open(item["image"])
            img = img.resize((120, 90))
            image = ImageTk.PhotoImage(img)

            label_image = ctk.CTkLabel(master=frame, image=image, text="")
            label_image.image = image
            label_image.pack(side="left", padx=10)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {item['image']} - {e}")

        label_name = ctk.CTkLabel(master=frame, text=item["name"], font=("Arial", 16))
        label_name.pack(anchor="w", pady=(10, 0), padx=(10, 0))

        label_description = ctk.CTkLabel(master=frame, text=item["description"], wraplength=400)
        label_description.pack(anchor="w", pady=(10, 0), padx=(10, 0))

        # Criação do botão favorito
        favorite_button = ctk.CTkButton(master=frame, text="", image=ImageTk.PhotoImage(Image.open("icons/favorito.png").resize((20, 20))), 
                                          width=40, height=40, fg_color="transparent", hover=False)
        favorite_button.pack(pady=(0, 0), padx=(0, 10), anchor="e")

        # Adicionando a função para o botão favorito
        favorite_button.bind("<Button-1>", lambda event, btn=favorite_button, item_name=item["name"]: favoritos.toggle_favorite(btn, item_name))
        favorite_button.bind("<Enter>", lambda event, btn=favorite_button: favoritos.on_enter(btn, "icons/favorito_active.png"))
        favorite_button.bind("<Leave>", lambda event, btn=favorite_button, item_name=item["name"]: favoritos.on_leave(btn, item_name))

        # Inicializa o estado do favorito
        initial_icon = "icons/favorito_active.png" if favoritos.favorite_states.get(item["name"], False) else "icons/favorito.png"
        favorite_button.configure(image=ImageTk.PhotoImage(Image.open(initial_icon).resize((20, 20))))
        
        button_details = ctk.CTkButton(master=frame, text="Ver mais", command=lambda p=item: show_gallery(p), fg_color="red")
        button_details.pack(pady=(0, 10), padx=(0, 10), anchor="e")

def show_gallery(place):
    ui.clear_frame(main.main_frame)

    back_button = ctk.CTkButton(master=main.main_frame, text="Voltar", command=menu.show_explore_menu, fg_color="red")
    back_button.pack(pady=(10, 5), padx=(10, 0), anchor="nw")

    # Carregar a imagem principal
    try:
        img = Image.open(place["image"]).resize((400, 300))
        image = ImageTk.PhotoImage(img)
        
        main_image_label = ctk.CTkLabel(master=main.main_frame, image=image, text="")
        main_image_label.image = image  # Manter a referência da imagem
        main_image_label.pack(pady=(15, 10))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")

    # Nome do lugar
    label_name = ctk.CTkLabel(master=main.main_frame, text=place["name"], font=("Arial", 18, "bold"))
    label_name.pack(pady=(10, 5))

    # Descrição do lugar
    label_description = ctk.CTkLabel(master=main.main_frame, text=place["description"], wraplength=400)
    label_description.pack(pady=(5, 10))

    # Galeria de imagens adicionais
    gallery_images = place.get("gallery", [])
    if gallery_images:
        gallery_canvas = Canvas(main.main_frame, height=150)
        gallery_canvas.pack(pady=10, fill="both", expand=True)

        scrollbar = Scrollbar(main.main_frame, orient="horizontal", command=gallery_canvas.xview)
        gallery_canvas.configure(xscrollcommand=scrollbar.set)
        scrollbar.pack(side="bottom", fill="x")

        gallery_container = ctk.CTkFrame(gallery_canvas)
        gallery_canvas.create_window((0, 0), window=gallery_container, anchor="nw")

        for image_path in gallery_images:
            try:
                img = Image.open(image_path).resize((120, 90))
                image = ImageTk.PhotoImage(img)
                gallery_label = ctk.CTkButton(master=gallery_container, image=image, text="", 
                                              command=lambda img=image_path: update_main_image(main_image_label, img))
                gallery_label.image = image  # Manter a referência da imagem
                gallery_label.pack(side="left", padx=5)
            except Exception as e:
                print(f"Erro ao carregar a imagem da galeria: {image_path} - {e}")

        gallery_container.update_idletasks()
        gallery_canvas.config(scrollregion=gallery_canvas.bbox("all"))

# Atualizar a imagem principal na galeria
def update_main_image(main_image_label, image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((400, 300))
        image = ImageTk.PhotoImage(img)
        main_image_label.configure(image=image)
        main_image_label.image = image
    except Exception as e:
        print(f"Erro ao carregar a imagem: {image_path} - {e}")

