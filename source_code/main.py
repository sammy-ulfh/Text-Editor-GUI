#!/usr/bin/env python3

import tkinter as tk
from editor import SimpleTextEditor

def main():

    root = tk.Tk() # Main Window
    root.title("Editor de texto")
    root.geometry("900x700")

    editor = SimpleTextEditor(root)

    menu_bar = tk.Menu(root, bg="gray")
    menu_options = tk.Menu(menu_bar, tearoff=0)

    menu_options.add_command(label="Nuevo", command=editor.new_file)
    menu_options.add_command(label="Abrir", command=editor.open_file)
    menu_options.add_command(label="Guardar", command=editor.save_file)
    menu_options.add_command(label="Salir", command=editor.quit_confirm)

    root.config(menu=menu_bar)
    menu_bar.add_cascade(label="Archivo", menu=menu_options)

    root.mainloop()

if __name__ == '__main__':
    main()
