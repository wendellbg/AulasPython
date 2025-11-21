import tkinter as tk
janela = tk.Tk()
janela.title("Minha Janela")
janela.configure(background="yellow")
janela.minsize(200,200)
janela.geometry("300x300+50+50")

#Adicionando rótulo na janela
tk.Label(janela, text="Este é um exemplo de rótulo na janela").pack()
tk.Label(janela, text=" - Wendell Bento Geraldes").pack()

#Adicionando um imagem na janela
image = tk.PhotoImage(file="linux.png")
tk.Label(janela, image=image).pack()

janela.mainloop()