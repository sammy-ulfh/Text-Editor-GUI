#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleTextEditor:

    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_open_filename = ''

    def new_file(self): # For clear the text area

        self.text_area.delete("1.0", tk.END)
        self.current_open_filename = ''

    def open_file(self): # For open and show the selected file content

        filename = filedialog.askopenfilename()

        if filename:

            self.text_area.delete("1.0", tk.END)
            with open(filename, 'r') as file:
                self.text_area.insert("1.0", file.read())

            self.current_open_filename = filename

    def save_file(self): # For save changes or a new file

        if not self.current_open_filename:

            new_filename =  filedialog.asksaveasfilename()

            if new_filename:
                self.current_open_filename = new_filename
            else:
                return

        with open(self.current_open_filename, 'w') as file:
            file.write(self.text_area.get("1.0", tk.END))

    def quit_confirm(self): # For close the app

        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir del programa?"):
            self.root.destroy()
