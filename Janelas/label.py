import tkinter as tk
janela = tk.Tk()
janela.title("Rótulo Tkinter")
janela.geometry("300x80")

label = tk.Label(janela, text="Olá Mundo!", font=("Helvetica", 30))
label.pack(expand=True)
                 
janela.mainloop()                 