import customtkinter as ctk
from tkinter import PhotoImage, Canvas, Scrollbar
from PIL import Image, ImageTk

# Função para trocar o conteúdo do frame principal
def show_content(category):
    clear_frame(main_frame)
    
    if category == 'Praias':
        places = [
            {"name": "Praia do Francês", "image": "images/praia1.png", "description": "Uma das mais belas praias do Brasil, localizada em Alagoas."},
            {"name": "Praia de Copacabana", "image": "images/praia2.png", "description": "Famosa praia do Rio de Janeiro, conhecida mundialmente."},
            {"name": "Praia de Ipanema", "image": "images/praia3.png", "description": "Um ícone da cidade do Rio de Janeiro, sempre cheia de turistas."},
            {"name": "Praia do Forte", "image": "images/praia4.png", "description": "Localizada na Bahia, famosa pelas tartarugas marinhas."},
            {"name": "Praia de Jericoacoara", "image": "images/praia5.png", "description": "Uma das mais belas e preservadas do Ceará."}
        ]
    elif category == 'Bares':
        places = [
            {"name": "Bar do Zeca", "image": "images/bar1.png", "description": "Bar descontraído com música ao vivo no Rio de Janeiro."},
            {"name": "Bar do Alemão", "image": "images/bar2.png", "description": "Famoso por seu chope artesanal e petiscos tradicionais."},
            {"name": "Boteco Belmonte", "image": "images/bar3.png", "description": "Boteco típico do Rio com pratos incríveis e bons drinks."},
            {"name": "Bar Brahma", "image": "images/bar4.png", "description": "Um dos bares mais tradicionais de São Paulo."},
            {"name": "Bar Astor", "image": "images/bar5.png", "description": "Bar sofisticado em Ipanema, perfeito para happy hours."}
        ]
    elif category == 'Trilhas':
        places = [
            {"name": "Trilha da Pedra do Elefante", "image": "images/trilha1.png", "description": "Trilha desafiadora em Itaipuaçu com vista deslumbrante."},
            {"name": "Trilha do Pão de Açúcar", "image": "images/trilha2.png", "description": "Uma das trilhas mais conhecidas do Rio de Janeiro."},
            {"name": "Trilha da Pedra Bonita", "image": "images/trilha3.png", "description": "Trilha que leva ao ponto de decolagem de parapentes no Rio."},
            {"name": "Trilha do Pico da Bandeira", "image": "images/trilha4.png", "description": "Uma das trilhas mais altas do Brasil, em Minas Gerais."},
            {"name": "Trilha dos Sete Lagos", "image": "images/trilha5.png", "description": "Trilha cênica em Itatiaia, atravessando lagos cristalinos."}
        ]
    else:  # Cultura e Artes
        places = [
            {"name": "Museu do Louvre", "image": "images/museu1.png", "description": "Famoso museu de arte em Paris, casa da Mona Lisa."},
            {"name": "Museu de Arte de São Paulo", "image": "images/museu2.png", "description": "Um dos museus de arte mais importantes do Brasil."},
            {"name": "Museu do Amanhã", "image": "images/museu3.png", "description": "Museu de ciências futurístico no Rio de Janeiro."},
            {"name": "Pinacoteca de São Paulo", "image": "images/museu4.png", "description": "Museu de artes visuais com um grande acervo."},
            {"name": "Centro Cultural Banco do Brasil", "image": "images/museu5.png", "description": "Centro de artes com exposições e peças no Rio e São Paulo."}
        ]
    
    for place in places:
        show_place(place)

# Função para limpar o frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Função para exibir cada lugar com imagem e descrição
def show_place(place):
    frame = ctk.CTkFrame(master=scrollable_frame, corner_radius=10)
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

# Interface principal
app = ctk.CTk()
app.geometry("800x600")
app.title("Opções de Lazer")

# Frame para os botões de categorias
button_frame = ctk.CTkFrame(master=app)
button_frame.pack(side="left", fill="y", padx=20, pady=20)

categories = ['Praias', 'Bares', 'Trilhas', 'Cultura e Artes']
for category in categories:
    button = ctk.CTkButton(master=button_frame, text=category, command=lambda c=category: show_content(c))
    button.pack(pady=10)

# Frame principal com canvas e scrollbar
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Adicionando o canvas com a scrollbar
canvas = Canvas(main_frame)
scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Empacotando o canvas e a scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

app.mainloop()
