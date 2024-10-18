from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkImage, CTkCanvas
from PIL import Image
from favoritos import toggle_favorite
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkImage, CTkCanvas
from PIL import Image
from favoritos import toggle_favorite, on_enter, on_leave

##### Color Index #####
light_color  = "#ff1818"
light_colorh = "#ce040a"

dark_color   = "#362AF2"
dark_colorh  = "#212ea0"

title_font = "Bahnschrift SemiBold" # 18
font = "Bahnschrift Light" # 14
#button = 13

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Menu da categoria
def show_content(main_frame, items,  app):
    from favoritos import favorite_states
    clear_frame(main_frame)

    main_frame._parent_canvas.yview_moveto(0.0)

    if not items:
        no_result_label = CTkLabel(master=main_frame, text="Nenhum resultado encontrado.", font=(font, 18, "bold"))
        no_result_label.pack(pady=20)
        return

    for item in items:
        frame = CTkFrame(master=main_frame, corner_radius=10, fg_color="transparent")
        frame.pack(pady=5, padx=20, fill="x")

        try:
            print(f"Carregando imagem {item['image']}")  
            img = Image.open(item["image"])
            image = CTkImage(img, size=(150, 120))

            label_image = CTkLabel(master=frame, image=image, text="")
            label_image.image = image
            label_image.pack(side="left", padx=10)
        except Exception as e:
            print(f"Erro ao carregar: {item['image']} - {e}")

        label_name = CTkLabel(master=frame, text=item["name"], font=(title_font, 18 , "bold"))
        label_name.pack(anchor="w", pady=(20, 0), padx=(10, 0))

        label_description = CTkLabel(master=frame, text=item["description"], font=(font, 14 ), justify="left", wraplength=650)
        label_description.pack(anchor="w", pady=(20, 0), padx=(10, 0))

        favorite_button = CTkButton(master=frame, text="", image=CTkImage(Image.open("icons/favorito.png"), size=(30, 30)), 
                                    width=40, height=40, fg_color="transparent", hover=False)
        favorite_button.pack(pady=(0, 0), padx=(0, 10), anchor="e")

        favorite_button.bind("<Button-1>", lambda event, btn=favorite_button, item_name=item["name"]: toggle_favorite(btn, item_name))
        favorite_button.bind("<Enter>", lambda event, btn=favorite_button: on_enter(btn, "icons/favorito_active.png"))
        favorite_button.bind("<Leave>", lambda event, btn=favorite_button, item_name=item["name"]: on_leave(btn, item_name))

        initial_icon = "icons/favorito_active.png" if favorite_states.get(item["name"], False) else "icons/favorito.png"
        favorite_button.configure(image=CTkImage(Image.open(initial_icon), size=(20, 20)))
    
        button_details = CTkButton(master=frame, text="Ver mais", font=(font, 13), command=lambda p=item: show_gallery(main_frame, p, items,  app),
                                    fg_color=(light_color, dark_color), hover_color=(light_colorh, dark_colorh))
        button_details.pack(pady=(0, 10), padx=(0, 10), anchor="e")

        line = CTkFrame(master=main_frame, height= 3, corner_radius= 0, fg_color=("gray62", "gray"))
        line.pack(padx = 30, fill="x")

# menu de 'Ver Mais'
def show_gallery(main_frame, place, all_items, app):
    clear_frame(main_frame)


    main_frame._parent_canvas.yview_moveto(0.0)

    global last_clicked_category
    last_clicked_category = all_items

    back_button = CTkButton(master=main_frame, text="Voltar", font=(font, 13), command=lambda: show_content(main_frame, last_clicked_category,  app),
                             fg_color=(light_color, dark_color), hover_color=(light_colorh, dark_colorh))
    back_button.pack(pady=(10, 5), padx=(10, 0), anchor="nw")

    try:
        img = Image.open(place["image"])
        image = CTkImage(img, size=(600, 400))
        main_image_label = CTkLabel(master=main_frame, image=image, text="")
        main_image_label.image = image
        main_image_label.pack(pady=(0, 0))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")

    label_name = CTkLabel(master=main_frame, text=place["name"], font=(title_font, 18, "bold"))
    label_name.pack(pady=(10, 5))

    label_description = CTkLabel(master=main_frame, text=place["address"], font=(font, 14), wraplength=600)
    label_description.pack(pady=(0, 40))

    gallery_images = place.get("gallery", [])
    if gallery_images:
        gallery_canvas = CTkCanvas(main_frame, height=140, highlightthickness=0 ,bg=app.cget("bg"), relief="sunken")
        gallery_canvas.pack(pady=5, padx = 10, fill="both", expand=True, anchor= "s")

        gallery_container = CTkFrame(gallery_canvas, fg_color=app.cget("bg"))
        gallery_canvas.create_window(gallery_canvas.winfo_width() // 200, 75, window=gallery_container, anchor="center")

        for image_path in gallery_images:
            try:
                img = Image.open(image_path)
                image = CTkImage(img, size=(150, 100))
                gallery_label = CTkButton(master=gallery_container, image=image, text="", 
                                          command=lambda img=image_path: update_main_image(main_image_label, img), fg_color=app.cget("bg"))
                gallery_label.image = image
                gallery_label.pack(side="left", padx=10, pady = 5)
            except Exception as e:
                print(f"Erro ao carregar a imagem da galeria: {image_path} - {e}")

        gallery_container.update_idletasks()
        gallery_canvas.config(scrollregion=gallery_canvas.bbox("all"))


def update_main_image(main_image_label, image_path):
    try:
        img = Image.open(image_path)
        image = CTkImage(img, size=(600, 400))
        main_image_label.configure(image=image)
        main_image_label.image = image
    except Exception as e:
        print(f"Erro ao carregar a imagem: {image_path} - {e}"), on_leave

##### Color Index #####
light_color  = "#ff1818"
light_colorh = "#ce040a"

dark_color   = "#362AF2"
dark_colorh  = "#212ea0"

title_font = "Bahnschrift SemiBold" # 18
font = "Bahnschrift Light" # 14

#button = 13


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Menu da categoria
def show_content(main_frame, items,  app):
    from favoritos import favorite_states
    clear_frame(main_frame)

    main_frame._parent_canvas.yview_moveto(0.0)

    if not items:
        no_result_label = CTkLabel(master=main_frame, text="Nenhum resultado encontrado.", font=(font, 18, "bold"))
        no_result_label.pack(pady=20)
        return

    for item in items:
        frame = CTkFrame(master=main_frame, corner_radius=10, fg_color=("#c1c1c1", "gray22"))
        frame.pack(pady=10, padx=20, fill="x")

        try:
            print(f"Carregando {item['image']}...")  
            img = Image.open(item["image"])
            image = CTkImage(img, size=(150, 120))

            label_image = CTkLabel(master=frame, image=image, text="")
            label_image.image = image
            label_image.pack(side="left", padx=10)
        except Exception as e:
            print(f"Erro ao carregar: {item['image']} - {e}")

        label_name = CTkLabel(master=frame, text=item["name"], font=(title_font, 18 , "bold"))
        label_name.pack(anchor="w", pady=(20, 0), padx=(10, 0))

        label_description = CTkLabel(master=frame, text=item["description"], font=(font, 14 ), justify="left", wraplength=650)
        label_description.pack(anchor="w", pady=(20, 0), padx=(10, 0))

        favorite_button = CTkButton(master=frame, text="", image=CTkImage(Image.open("icons/favorito.png"), size=(30, 30)), 
                                    width=40, height=40, fg_color="transparent", hover=False)
        favorite_button.pack(pady=(0, 0), padx=(0, 10), anchor="e")

        favorite_button.bind("<Button-1>", lambda event, btn=favorite_button, item_name=item["name"]: toggle_favorite(btn, item_name))
        favorite_button.bind("<Enter>", lambda event, btn=favorite_button: on_enter(btn, "icons/favorito_active.png"))
        favorite_button.bind("<Leave>", lambda event, btn=favorite_button, item_name=item["name"]: on_leave(btn, item_name))

        initial_icon = "icons/favorito_active.png" if favorite_states.get(item["name"], False) else "icons/favorito.png"
        favorite_button.configure(image=CTkImage(Image.open(initial_icon), size=(20, 20)))
    
        button_details = CTkButton(master=frame, text="Ver mais", font=(font, 13), command=lambda p=item: show_gallery(main_frame, p, items,  app),
                                    fg_color=(light_color, dark_color), hover_color=(light_colorh, dark_colorh))
        button_details.pack(pady=(0, 10), padx=(0, 10), anchor="e")

# menu de 'Ver Mais'
def show_gallery(main_frame, place, all_items, app):
    clear_frame(main_frame)


    main_frame._parent_canvas.yview_moveto(0.0)

    global last_clicked_category
    last_clicked_category = all_items

    back_button = CTkButton(master=main_frame, text="Voltar", font=(font, 13), command=lambda: show_content(main_frame, last_clicked_category,  app),
                             fg_color=(light_color, dark_color), hover_color=(light_colorh, dark_colorh))
    back_button.pack(pady=(10, 5), padx=(10, 0), anchor="nw")

    try:
        img = Image.open(place["image"])
        image = CTkImage(img, size=(600, 400))
        main_image_label = CTkLabel(master=main_frame, image=image, text="")
        main_image_label.image = image
        main_image_label.pack(pady=(0, 0))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")

    label_name = CTkLabel(master=main_frame, text=place["name"], font=(title_font, 18, "bold"))
    label_name.pack(pady=(10, 5))

    label_description = CTkLabel(master=main_frame, text=place["address"], font=(font, 14), wraplength=600)
    label_description.pack(pady=(0, 40))

    gallery_images = place.get("gallery", [])
    if gallery_images:
        gallery_canvas = CTkCanvas(main_frame, height=140, highlightthickness=0 ,bg=app.cget("bg"), relief="sunken")
        gallery_canvas.pack(pady=5, padx = 10, fill="both", expand=True, anchor= "s")

        gallery_container = CTkFrame(gallery_canvas, fg_color=app.cget("bg"))
        gallery_canvas.create_window(gallery_canvas.winfo_width() // 200, 75, window=gallery_container, anchor="center")

        for image_path in gallery_images:
            try:
                img = Image.open(image_path)
                image = CTkImage(img, size=(150, 100))
                gallery_label = CTkButton(master=gallery_container, image=image, text="", 
                                          command=lambda img=image_path: update_main_image(main_image_label, img), fg_color=app.cget("bg"))
                gallery_label.image = image
                gallery_label.pack(side="left", padx=10, pady = 5)
            except Exception as e:
                print(f"Erro ao carregar a imagem da galeria: {image_path} - {e}")

        gallery_container.update_idletasks()
        gallery_canvas.config(scrollregion=gallery_canvas.bbox("all"))


def update_main_image(main_image_label, image_path):
    try:
        img = Image.open(image_path)
        image = CTkImage(img, size=(600, 400))
        main_image_label.configure(image=image)
        main_image_label.image = image
    except Exception as e:
        print(f"Erro ao carregar a imagem: {image_path} - {e}")
