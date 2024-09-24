import customtkinter as ctk

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

# Criação da janela principal
app = ctk.CTk()
app.title("Tema Claro/Escuro")
app.geometry("300x200")

# Botão para mudar o tema
theme_button = ctk.CTkButton(app, text="Modo Claro", command=toggle_theme)
theme_button.pack(pady=50)

# Executa o aplicativo
app.mainloop()
