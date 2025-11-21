import tkinter as tk

janela = tk.Tk()
janela.title("Botão Tkinter")
janela.geometry("200x100")

def on_click():
    label.config(text="Botão clicado")

botao = tk.Button(
    janela,
    text="Clique em mim",
    command=on_click,
)
botao.pack(padx=5, pady=5)

label = tk.Label(janela, text="Esperando um clique")
label.pack(padx=5, pady=5)

janela.mainloop()