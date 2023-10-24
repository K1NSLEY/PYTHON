import tkinter as tk

# Função para fechar a janela
def fechar_janela():
    janela.destroy()
def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)

# Criar a janela
janela = tk.Tk()
# Adicionar um rótulo à janela
rotulo = tk.Label(janela, text="Minha Janela")
rotulo.pack(padx=10, pady=10)

# Adicionar um botão para fechar a janela
botao_fechar = tk.Button(janela, text="Fechar Janela", command=fechar_janela)
botao_fechar.pack(pady=10)

# Definir o título da janela
janela.title("Janela Simples")

# Definir as dimensões iniciais da janela
largura = 300
altura = 200
janela.geometry(f"{largura}x{altura}")

# Iniciar o loop de eventos
janela.mainloop()
