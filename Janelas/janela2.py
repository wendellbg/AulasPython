import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Widgets Principais para Janelas")

widgets = [tk.Label, tk.Checkbutton, ttk.Combobox, tk.Entry, tk.Button, tk.Radiobutton, tk.Scale, tk.Spinbox, ]

for widget in widgets:
    try:
        widget = widget(janela, text=widget.__name__)
    except tk.TclError:
        widget = widget(janela)
    widget.pack(padx=5, pady=5, fill="x")

janela.mainloop()