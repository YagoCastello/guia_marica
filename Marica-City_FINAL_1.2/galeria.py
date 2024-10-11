from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkImage, CTkCanvas
from PIL import Image
from favoritos import toggle_favorite, on_enter, on_leave
from categorias import all_items

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_content(main_frame, items):
    from favoritos import favorite_states
    clear_frame(main_frame)

    if not items:
        no_result_label = CTkLabel(master=main_frame, text="Nenhum resultado encontrado.", font=("Arial", 16, "bold"))
        no_result_label.pack(pady=20)
        return

    for item in items:
        frame = CTkFrame(master=main_frame, corner_radius=10)
        frame.pack(pady=10, padx=20, fill="x")

        try:
            print(f"Carregando a imagem: {item['image']}")  
            img = Image.open(item["image"])
            image = CTkImage(img, size=(120, 90))

            label_image = CTkLabel(master=frame, image=image, text="")
            label_image.image = image
            label_image.pack(side="left", padx=10)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {item['image']} - {e}")

        label_name = CTkLabel(master=frame, text=item["name"], font=("Arial", 16))
        label_name.pack(anchor="w", pady=(10, 0), padx=(10, 0))

        label_description = CTkLabel(master=frame, text=item["description"], wraplength=400)
        label_description.pack(anchor="w", pady=(10, 0), padx=(10, 0))

        favorite_button = CTkButton(master=frame, text="", image=CTkImage(Image.open("icons/favorito.png"), size=(30, 30)), 
                                    width=40, height=40, fg_color="transparent", hover=False)
        favorite_button.pack(pady=(0, 0), padx=(0, 10), anchor="e")

        favorite_button.bind("<Button-1>", lambda event, btn=favorite_button, item_name=item["name"]: toggle_favorite(btn, item_name))
        favorite_button.bind("<Enter>", lambda event, btn=favorite_button: on_enter(btn, "icons/favorito_active.png"))
        favorite_button.bind("<Leave>", lambda event, btn=favorite_button, item_name=item["name"]: on_leave(btn, item_name))

        initial_icon = "icons/favorito_active.png" if favorite_states.get(item["name"], False) else "icons/favorito.png"
        favorite_button.configure(image=CTkImage(Image.open(initial_icon), size=(20, 20)))

        button_details = CTkButton(master=frame, text="Ver mais", command=lambda p=item: show_gallery(main_frame, p, items), fg_color="red")
        button_details.pack(pady=(0, 10), padx=(0, 10), anchor="e")


def show_gallery(main_frame, place, all_items):
    clear_frame(main_frame)

    global last_clicked_category
    last_clicked_category = all_items

    back_button = CTkButton(master=main_frame, text="Voltar", command=lambda: show_content(main_frame, last_clicked_category), fg_color="red")
    back_button.pack(pady=(10, 5), padx=(10, 0), anchor="nw")

    try:
        img = Image.open(place["image"])
        image = CTkImage(img, size=(400, 300))
        main_image_label = CTkLabel(master=main_frame, image=image, text="")
        main_image_label.image = image
        main_image_label.pack(pady=(15, 10))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")

    label_name = CTkLabel(master=main_frame, text=place["name"], font=("Arial", 18, "bold"))
    label_name.pack(pady=(10, 5))

    label_description = CTkLabel(master=main_frame, text=place["description"], wraplength=400)
    label_description.pack(pady=(5, 10))

    gallery_images = place.get("gallery", [])
    if gallery_images:
        gallery_canvas = CTkCanvas(main_frame, height=150)
        gallery_canvas.pack(pady=10, fill="both", expand=True)

        gallery_container = CTkFrame(gallery_canvas)
        gallery_canvas.create_window((0, 0), window=gallery_container, anchor="nw")

        for image_path in gallery_images:
            try:
                img = Image.open(image_path)
                image = CTkImage(img, size=(120, 90))
                gallery_label = CTkButton(master=gallery_container, image=image, text="", 
                                          command=lambda img=image_path: update_main_image(main_image_label, img))
                gallery_label.image = image
                gallery_label.pack(side="left", padx=5)
            except Exception as e:
                print(f"Erro ao carregar a imagem da galeria: {image_path} - {e}")

        gallery_container.update_idletasks()
        gallery_canvas.config(scrollregion=gallery_canvas.bbox("all"))


def update_main_image(main_image_label, image_path):
    try:
        img = Image.open(image_path)
        image = CTkImage(img, size=(400, 300))
        main_image_label.configure(image=image)
        main_image_label.image = image
    except Exception as e:
        print(f"Erro ao carregar a imagem: {image_path} - {e}")
