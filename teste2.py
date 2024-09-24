import customtkinter as ctk
from tkinter import PhotoImage

# Função para trocar o conteúdo do frame principal
def show_content(category):
    clear_frame(main_frame)
    
    if category == 'Praias':
        places = [
            {"name": "Praia do Francês", "image": "images/praia1.jpg", "description": "Uma das mais belas praias do Brasil, localizada em Alagoas."},
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
    frame = ctk.CTkFrame(master=main_frame)
    frame.pack(pady=10, padx=20, fill="x", expand=True)
    
    # Carregando a imagem e mantendo referência
    try:
        image = PhotoImage(file=place["image"])  # Carregue a imagem local
        label_image = ctk.CTkLabel(master=frame, image=image, text="")
        label_image.image = image  # Para manter a referência
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

# Frame principal onde o conteúdo será exibido
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

app.mainloop()
