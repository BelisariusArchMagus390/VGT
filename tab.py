import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import os
import sys
import re


class Tab_table:
    def __init__(self, my_notebook: ttk.Notebook, root):
        self.my_notebook = my_notebook
        self.root = root
        self.bg_color = "#313131"
        self.fg_color = "#ffffff"

        self.frame = ttk.Frame(self.my_notebook)
        self.frame.pack(fill="both", expand=1)

        self.data = data

        self.tree_frame = ttk.Frame(self.my_notebook)
        self.tree_frame.pack()

        # Scrollbar vertical da Text box
        self.tree_scroll = ttk.Scrollbar(self.tree_frame)
        # Pack da Scrollbar
        self.tree_scroll.pack(side="right", fill="y")

        self.my_tree = ttk.Treeview(
            self.tree_frame, yscrollcommand=self.tree_scroll.set, selectmode="extended"
        )
        self.my_tree.pack()

        # Configuração da Scrollbar
        self.tree_scroll.config(command=self.my_tree.yview)

        # Define o nome das colunas
        self.my_tree["columns"] = (
            "Lexema",
            "Token",
            "Linha",
            "Coluna",
            "Tipo Token",
            "ID",
        )

        # Formatando as colunas
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Lexema", anchor="w", width=140)
        self.my_tree.column("Token", anchor="w", width=140)
        self.my_tree.column("Linha", anchor="w", width=140)
        self.my_tree.column("Coluna", anchor="w", width=140)
        self.my_tree.column("Tipo Token", anchor="w", width=140)
        self.my_tree.column("ID", anchor="center", width=100)

        # Criando Headings
        self.my_tree.heading("#0", text="", anchor="w")
        self.my_tree.heading("Lexema", text="Lexema", anchor="w")
        self.my_tree.heading("Token", text="Token", anchor="w")
        self.my_tree.heading("Linha", text="Linha", anchor="w")
        self.my_tree.heading("Coluna", text="Coluna", anchor="w")
        self.my_tree.heading("Tipo Token", text="Tipo Token", anchor="w")
        self.my_tree.heading("ID", text="ID", anchor="center")

        # Inserindo dados na TreeView
        for token in self.data:
            self.my_tree.insert("", END, values=token)

        self.my_notebook.add(self.tree_frame, text="Lexic Table")

    def execute(self, _=None):
        pass

    # def close_tab(self, _=None):
    #    self.frame.destroy()

    def close_output_terminal(self, _=None):
        self.fr_output.destroy()
        self.my_text.config(height=23)

    def change_color(self, bg_color, fg_color):
        self.my_text.config(background=bg_color, fg=fg_color)
        self.txt_box_output.config(background=bg_color, fg=fg_color)
        self.linenumbers.configure(bg=bg_color)
        self.bg_color = bg_color
        self.fg_color = fg_color

    def get_text_status_bar(self):
        return self.text_status_bar

    def get_text_title(self):
        return self.text_title
