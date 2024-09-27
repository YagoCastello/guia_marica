import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk


# Configurar modo claro/escuro
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        ctk.set_appearance_mode("dark")
        theme_button.configure(text="Modo Claro")
    else:
        ctk.set_appearance_mode("light")
        theme_button.configure(text="Modo Escuro")

    components_to_update = [header, menu_frame, search_frame]

    for component in components_to_update:
        component.configure(fg_color=app.cget("bg"))


# Lógica da Pesquisa
def search_action(query):
    results = search_items(query)  # Obter os resultados da pesquisa
    show_content(results)  # Mostrar os resultados no main_frame


# Função para buscar em todas as categorias
def search_items(query):
    # Lista de todas as categorias disponíveis
    all_items = explorar_praia()[1] + explorar_bares()[1]

    # Filtrar os itens que contêm o termo pesquisado no nome
    filtered_items = [item for item in all_items if query in item["name"].lower()]
    return filtered_items


# Limpar o frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Exibir a galeria e descrição de cada item dentro das categorias
def show_gallery(place):
    clear_frame(main_frame)

    back_button = ctk.CTkButton(master=main_frame, text="Voltar", command=show_explore_menu, fg_color="red")
    back_button.pack(pady=(10, 5), padx=(10, 0), anchor="nw")

    try:
        img = Image.open(place["image"])
        img = img.resize((400, 300))
        image = ImageTk.PhotoImage(img)
        main_image_label = ctk.CTkLabel(master=main_frame, image=image, text="")
        main_image_label.image = image
        main_image_label.pack(pady=(15, 10))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")

    label_name = ctk.CTkLabel(master=main_frame, text=place["name"], font=("Arial", 18, "bold"))
    label_name.pack(pady=(10, 5))

    label_description = ctk.CTkLabel(master=main_frame, text=place["description"], wraplength=400)
    label_description.pack(pady=(5, 10))

    gallery_images = place.get("gallery", [])
    if gallery_images:
        gallery_canvas = Canvas(main_frame, height=150)
        gallery_canvas.pack(pady=10, fill="both", expand=True)

        scrollbar = Scrollbar(main_frame, orient="horizontal", command=gallery_canvas.xview)
        gallery_canvas.configure(xscrollcommand=scrollbar.set)
        scrollbar.pack(side="bottom", fill="x")

        gallery_container = ctk.CTkFrame(gallery_canvas)
        gallery_canvas.create_window((0, 0), window=gallery_container, anchor="nw")

        for image_path in gallery_images:
            try:
                img = Image.open(image_path)
                img = img.resize((120, 90))
                image = ImageTk.PhotoImage(img)
                gallery_label = ctk.CTkButton(master=gallery_container, image=image, text="",
                                              command=lambda img=image_path: update_main_image(main_image_label, img))
                gallery_label.image = image
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


# Exibir o conteúdo de uma categoria ou resultado de pesquisa
def show_content(items):
    clear_frame(main_frame)

    if not items:
        no_result_label = ctk.CTkLabel(master=main_frame, text="Nenhum resultado encontrado.", font=("Arial", 16, "bold"))
        no_result_label.pack(pady=20)
        return

    for item in items:
        frame = ctk.CTkFrame(master=main_frame, corner_radius=10)
        frame.pack(pady=10, padx=20, fill="x")

        try:
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

        button_details = ctk.CTkButton(master=frame, text="Ver mais", command=lambda p=item: show_gallery(p),
                                       fg_color="red")
        button_details.pack(pady=(0, 10), padx=(0, 10), anchor="e")


# Funções individuais de exploração
def explorar_praia():
    praias = [
        {"name": "Praia do Francês", "image": "images/praia1.png",
         "description": "Uma das mais belas praias do Brasil.",
         "gallery": ["images/praia1.png", "images/praia1_1.png"]},
        {"name": "Praia de Copacabana", "image": "images/praia2.png", "description": "Famosa praia no Rio de Janeiro.",
         "gallery": ["images/praia2_1.png"]},
    ]
    return "Praias", praias


def explorar_bares():
    bares = [
        {"name": "Bar do Zé", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.",
         "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Botequim do João", "image": "images/bar2.png",
         "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2_1.png"]},
    ]
    return "Bares", bares


# Menu 'Inicio'
def show_home():
    clear_frame(main_frame)
    home_label = ctk.CTkLabel(master=main_frame, text="Bem-vindo à Maricá City!", font=("Arial", 18, "bold"))
    home_label.pack(pady=20)


# Menu 'Explorar'
def show_explore_menu():
    clear_frame(main_frame)
    explore_options = [explorar_praia, explorar_bares]

    for option_func in explore_options:
        button_name, content = option_func()
        button = ctk.CTkButton(master=main_frame, text=button_name, command=lambda c=content: show_content(c),
                               fg_color="red")
        button.pack(pady=10, padx=20)


# Menu 'Opções'
def show_options_menu():
    clear_frame(main_frame)
    global theme_button
    theme_button = ctk.CTkButton(master=main_frame, text="Modo Claro", command=toggle_theme, fg_color="red")
    theme_button.pack(pady=10, padx=20)


#################### APLICATIVO ####################
app = ctk.CTk()
app.geometry("1200x800")
app.title("Marica City")

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

header = ctk.CTkFrame(app, width=260, fg_color=app.cget("bg"))
header.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=(0, 10))

header_label = ctk.CTkLabel(header, text="MARICA CITY", text_color="red", font=("Arial", 20, "bold"))
header_label.grid(row=0, column=0, pady=10)

search_frame = ctk.CTkFrame(app, width=300, height=50, fg_color=app.cget("bg"))
search_frame.grid(row=0, column=1, sticky="ew", padx=(10, 0))

search_entry = ctk.CTkEntry(search_frame, width=200)
search_entry.grid(row=0, column=0, padx=(10, 0), pady=10)

search_button = ctk.CTkButton(search_frame, text="Pesquisar", command=lambda: search_action(search_entry.get().lower()),
                              fg_color="red")
search_button.grid(row=0, column=1, padx=(5, 0), pady=10)

main_frame = ctk.CTkFrame(master=app)
main_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

menu_frame = ctk.CTkFrame(master=app, fg_color=app.cget("bg"))
menu_frame.grid(row=1, column=0, sticky="ns", pady=(0, 10))

menu_buttons = [
    {"text": "Inicio", "command": show_home},
    {"text": "Explorar", "command": show_explore_menu},
    {"text": "Opções", "command": show_options_menu},
]

for index, btn in enumerate(menu_buttons):
    ctk.CTkButton(master=menu_frame, text=btn["text"], command=btn["command"], fg_color="red").grid(row=index, column=0, pady=10, padx=10)

dark_mode = False

show_home()
app.mainloop()