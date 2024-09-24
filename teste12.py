import customtkinter as ctk
from PIL import Image, ImageTk
import os  # Para verificar se os arquivos de imagem existem

# Função para atualizar a imagem principal na galeria e permitir navegação
def update_main_image(gallery_frame, gallery_images, index):
    try:
        # Carrega e redimensiona a imagem da galeria
        img = Image.open(gallery_images[index])
        img = img.resize((400, 300))  # Redimensiona para 400x300 pixels
        image = ImageTk.PhotoImage(img)

        # Atualiza o rótulo da imagem principal
        gallery_frame.main_image_label.configure(image=image)
        gallery_frame.main_image_label.image = image  # Mantém a referência da imagem
        gallery_frame.current_image_index = index

        # Atualiza a navegação
        update_navigation_buttons(gallery_frame, gallery_images)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {gallery_images[index]} - {e}")

# Função para atualizar o estado dos botões de navegação
def update_navigation_buttons(gallery_frame, gallery_images):
    # Atualiza o botão "Anterior"
    if gallery_frame.current_image_index > 0:
        gallery_frame.previous_button.configure(state="normal", command=lambda: update_main_image(gallery_frame, gallery_images, gallery_frame.current_image_index - 1))
    else:
        gallery_frame.previous_button.configure(state="disabled")
    
    # Atualiza o botão "Próximo"
    if gallery_frame.current_image_index < len(gallery_images) - 1:
        gallery_frame.next_button.configure(state="normal", command=lambda: update_main_image(gallery_frame, gallery_images, gallery_frame.current_image_index + 1))
    else:
        gallery_frame.next_button.configure(state="disabled")

# Função para exibir a galeria e a descrição detalhada do local escolhido
def show_gallery(place):
    clear_frame(main_frame)
    
    # Frame para galeria de imagens e descrição
    gallery_frame = ctk.CTkFrame(master=main_frame, corner_radius=10)
    gallery_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # Botão de voltar
    back_button = ctk.CTkButton(master=gallery_frame, text="Voltar", command=lambda: show_content(current_category))
    back_button.pack(pady=10, anchor="w")

    # Adicionar a imagem principal à galeria
    gallery_images = [place["image"]] + place.get("gallery", [])
    
    # Carregando a imagem principal (inicial)
    update_main_image(gallery_frame, gallery_images, 0)

    # Nome do lugar
    label_name = ctk.CTkLabel(master=gallery_frame, text=place["name"], font=("Arial", 18, "bold"))
    label_name.pack(pady=10)

    # Descrição detalhada
    label_description = ctk.CTkLabel(master=gallery_frame, text=place["description"], wraplength=400)
    label_description.pack(pady=10)

    if gallery_images:
        # Inicializa os botões de navegação
        navigation_frame = ctk.CTkFrame(master=gallery_frame)
        navigation_frame.pack(pady=10)

        # Botão "Anterior"
        gallery_frame.previous_button = ctk.CTkButton(master=navigation_frame, text="Anterior", state="disabled")
        gallery_frame.previous_button.pack(side="left", padx=5)

        # Botão "Próximo"
        gallery_frame.next_button = ctk.CTkButton(master=navigation_frame, text="Próximo", state="normal")
        gallery_frame.next_button.pack(side="left", padx=5)

        # Atualiza a navegação inicial
        update_navigation_buttons(gallery_frame, gallery_images)

# Função para trocar o conteúdo do frame principal
def show_content(category):
    global current_category
    current_category = category
    clear_frame(main_frame)

    if category == 'Praias':
        places = [
            {"name": "Praia do Francês", "image": "images/praia1.png", "description": "Uma das mais belas praias do Brasil, localizada em Alagoas.", "gallery": ["images/praia1_1.png", "images/praia1.png","images/praia1_2.png"]},
            {"name": "Praia de Copacabana", "image": "images/praia2.png", "description": "Famosa praia do Rio de Janeiro, conhecida mundialmente.", "gallery": ["images/praia2_1.png", "images/praia2_2.png"]},
            {"name": "Praia de Ipanema", "image": "images/praia3.png", "description": "Um ícone da cidade do Rio de Janeiro, sempre cheia de turistas.", "gallery": ["images/praia3_1.png", "images/praia3_2.png"]},
            {"name": "Praia do Forte", "image": "images/praia4.png", "description": "Localizada na Bahia, famosa pelas tartarugas marinhas.", "gallery": ["images/praia4_1.png", "images/praia4_2.png"]},
            {"name": "Praia de Jericoacoara", "image": "images/praia5.png", "description": "Uma das mais belas e preservadas do Ceará.", "gallery": ["images/praia5_1.png", "images/praia5_2.png"]}
        ]
    # Outras categorias (Bares, Trilhas, Cultura e Artes) seguem o mesmo formato...

    for place in places:
        show_place(place)

# Função para limpar o frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Função para exibir cada lugar com imagem e botão de mais detalhes
def show_place(place):
    frame = ctk.CTkFrame(master=main_frame, corner_radius=10)
    frame.pack(pady=10, padx=20, fill="x", expand=True)

    # Redimensionando a imagem para não ocupar muito espaço
    try:
        img_path = place["image"]
        if os.path.exists(img_path):  # Verifica se o arquivo de imagem existe
            img = Image.open(img_path)
            img = img.resize((120, 90))  # Redimensiona para 120x90 pixels
            image = ImageTk.PhotoImage(img)

            # Armazenar referência da imagem
            frame.image_ref = image

            label_image = ctk.CTkLabel(master=frame, image=image, text="")
            label_image.image = image  # Mantém a referência da imagem
            label_image.pack(side="left", padx=10)
        else:
            print(f"Imagem não encontrada: {img_path}")
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")

    # Nome do lugar
    label_name = ctk.CTkLabel(master=frame, text=place["name"], font=("Arial", 16))
    label_name.pack(anchor="w")

    # Descrição do lugar
    label_description = ctk.CTkLabel(master=frame, text=place["description"], wraplength=400)
    label_description.pack(anchor="w")

    # Botão para abrir a galeria
    button_details = ctk.CTkButton(master=frame, text="Ver mais", command=lambda p=place: show_gallery(p))
    button_details.pack(anchor="e", pady=10)

# Função para mudar a cor base do aplicativo
def change_color_mode(mode):
    ctk.set_appearance_mode(mode)

# Interface principal
app = ctk.CTk()
app.geometry("800x600")
app.title("Opções de Lazer")

# Mudando a cor base inicial
ctk.set_appearance_mode("light")  # Você pode mudar para "dark" ou "System"

# Frame para os botões de categorias
button_frame = ctk.CTkFrame(master=app)
button_frame.pack(side="left", fill="y", padx=20, pady=20)

# Botões para mudar a cor base
theme_frame = ctk.CTkFrame(master=button_frame)
theme_frame.pack(pady=10)

light_mode_button = ctk.CTkButton(master=theme_frame, text="Modo Claro", command=lambda: change_color_mode("light"))
light_mode_button.pack(pady=5)

dark_mode_button = ctk.CTkButton(master=theme_frame, text="Modo Escuro", command=lambda: change_color_mode("dark"))
dark_mode_button.pack(pady=5)

system_mode_button = ctk.CTkButton(master=theme_frame, text="Modo do Sistema", command=lambda: change_color_mode("system"))
system_mode_button.pack(pady=5)

categories = ['Praias', 'Bares', 'Trilhas', 'Cultura e Artes']
for category in categories:
    button = ctk.CTkButton(master=button_frame, text=category, command=lambda c=category: show_content(c))
    button.pack(pady=10)

# Frame principal para exibir os conteúdos
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

app.mainloop()
