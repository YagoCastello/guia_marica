import customtkinter as ctk
from tkinter import Canvas, Scrollbar
from PIL import Image, ImageTk

# Função para alternar entre modo claro e escuro
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        ctk.set_appearance_mode("dark")  # Modo escuro
        theme_button.configure(text="Modo Claro")
    else:
        ctk.set_appearance_mode("light")  # Modo claro
        theme_button.configure(text="Modo Escuro")

# Configurações iniciais
dark_mode = True
ctk.set_appearance_mode("dark")  # Começa no modo escuro
ctk.set_default_color_theme("blue")  # Altere para a cor de tema desejada

# Função para atualizar a imagem principal na galeria ao clicar em uma imagem da galeria
def update_main_image(gallery_frame, image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((400, 300))  # Redimensiona para 400x300 pixels
        image = ImageTk.PhotoImage(img)
        
        # Atualiza o rótulo da imagem principal
        gallery_frame.main_image_label.configure(image=image)
        gallery_frame.main_image_label.image = image  # Atualiza a referência da imagem
    except Exception as e:
        print(f"Erro ao carregar a imagem: {image_path} - {e}")

# Função para exibir a galeria e a descrição detalhada do local escolhido
def show_gallery(place):
    clear_frame(main_frame)
    
    # Frame para galeria de imagens e descrição
    gallery_frame = ctk.CTkFrame(master=main_frame, corner_radius=10)
    gallery_frame.pack(pady=10, padx=20, fill="both", expand=True)
    
    # Botão de voltar
    back_button = ctk.CTkButton(master=gallery_frame, text="Voltar", command=lambda: show_content(current_category))
    back_button.pack(pady=10, anchor="w")
    
    # Carregando a imagem principal
    try:
        img = Image.open(place["image"])
        img = img.resize((400, 300))  # Redimensiona para 400x300 pixels
        image = ImageTk.PhotoImage(img)

        gallery_frame.main_image_label = ctk.CTkLabel(master=gallery_frame, image=image, text="")
        gallery_frame.main_image_label.image = image  # Mantém a referência da imagem
        gallery_frame.main_image_label.pack(pady=10)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")
    
    # Nome do lugar
    label_name = ctk.CTkLabel(master=gallery_frame, text=place["name"], font=("Arial", 18, "bold"))
    label_name.pack(pady=10)
    
    # Descrição detalhada
    label_description = ctk.CTkLabel(master=gallery_frame, text=place["description"], wraplength=400)
    label_description.pack(pady=10)
    
    # Galeria de imagens adicionais (se houver mais imagens)
    gallery_images = place.get("gallery", [])
    
    if gallery_images:
        gallery_canvas = Canvas(gallery_frame, height=150)
        gallery_canvas.pack(pady=10, fill="both", expand=True)
        scrollbar = Scrollbar(gallery_frame, orient="horizontal", command=gallery_canvas.xview)
        gallery_canvas.configure(xscrollcommand=scrollbar.set)
        scrollbar.pack(side="bottom", fill="x")
        
        gallery_container = ctk.CTkFrame(gallery_canvas)
        gallery_canvas.create_window((0, 0), window=gallery_container, anchor="nw")
        
        for image_path in gallery_images:
            try:
                img = Image.open(image_path)
                img = img.resize((120, 90))  # Redimensiona para 120x90 pixels
                image = ImageTk.PhotoImage(img)

                # Cada imagem da galeria será um botão clicável
                gallery_label = ctk.CTkButton(master=gallery_container, image=image, text="", 
                                              command=lambda img=image_path: update_main_image(gallery_frame, img))
                gallery_label.image = image  # Mantém a referência da imagem
                gallery_label.pack(side="left", padx=5)
            except Exception as e:
                print(f"Erro ao carregar a imagem da galeria: {image_path} - {e}")
        
        gallery_container.update_idletasks()
        gallery_canvas.config(scrollregion=gallery_canvas.bbox("all"))

# Função para trocar o conteúdo do frame principal
def show_content(category):
    global current_category
    current_category = category
    clear_frame(main_frame)
    
    if category == 'Praias':
        places = [
            {"name": "Praia do Francês", "image": "images/praia1.png", "description": "Uma das mais belas praias do Brasil, localizada em Alagoas.", "gallery": ["images/praia1.png" ,"images/praia1_1.png","images/praia1_2.png"]},
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
        img = Image.open(place["image"])
        img = img.resize((120, 90))  # Redimensiona para 120x90 pixels
        image = ImageTk.PhotoImage(img)
        
        label_image = ctk.CTkLabel(master=frame, image=image, text="")
        label_image.image = image  # Mantém a referência da imagem
        label_image.pack(side="left", padx=10)
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

# Interface principal
app = ctk.CTk()
app.geometry("800x600")
app.title("Opções de Lazer")

# Frame para os botões de categorias
button_frame = ctk.CTkFrame(master=app)
button_frame.pack(side="left", fill="y", padx=20, pady=20)

# Botão para alternar o tema
theme_button = ctk.CTkButton(master=button_frame, text="Modo Claro", command=toggle_theme)
theme_button.pack(pady=10)

# Lista de categorias
categories = ['Praias', 'Bares', 'Trilhas', 'Cultura e Artes']
for category in categories:
    button = ctk.CTkButton(master=button_frame, text=category, command=lambda c=category: show_content(c))
    button.pack(pady=10)

# Frame principal para exibir os conteúdos
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Variável global para armazenar a categoria atual
current_category = None

app.mainloop()
