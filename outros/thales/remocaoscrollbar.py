def update_main_image(gallery_frame, image_path):
	try:
		img = Image.open(image_path)
		img = img.resize((350, 250))  # Redimensiona para 400x300 pixels
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
	gallery_frame = ctk.CTkFrame(master=main_frame, corner_radius=20)
	gallery_frame.pack(pady=10, padx=20, fill="both", expand=True)
	
	# Botão de voltar
	back_button = ctk.CTkButton(master=gallery_frame, text="Voltar", command=lambda: show_content(current_category))
	back_button.pack(pady=10, anchor="w")
	
	# Carregando a imagem principal
	try:
		img = Image.open(place["image"])
		img = img.resize((350, 250))  # Redimensiona para 400x300 pixels
		image = ImageTk.PhotoImage(img)
		
		gallery_frame.main_image_label = ctk.CTkLabel(master=gallery_frame, image=image, text="")
		gallery_frame.main_image_label.image = image  # Mantém a referência da imagem
		gallery_frame.main_image_label.pack(pady=20)
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
		gallery_canvas = Canvas(gallery_frame, height=50)
		gallery_canvas.pack(pady=30, fill="both", expand=True)
		scrollbar = Scrollbar(gallery_frame, orient="horizontal", command=gallery_canvas.xview)
	# gallery_canvas.configure(xscrollcommand=scrollbar.set)
	# scrollbar.pack(side="bottom", fill="x") COMENTADO PARA REMOÇÃO DA SCROLLBAR