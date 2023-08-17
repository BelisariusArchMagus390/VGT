import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import os
import sys
import re
import pandas as pd


class Tab_table:
    def __init__(self, my_notebook: ttk.Notebook, root, data):
        self.data = data

        file = Path(__file__).parent.joinpath("data").joinpath("cargas2011a2021.xlsx")
        port_cargo = pd.read_excel(file)

        years = port_cargo["Ano"].drop_duplicates().to_list()
        port_cargo_year = port_cargo.loc[(port_cargo["Ano"].isin(years))]
        port_cargo_year = port_cargo_year.loc[(port_cargo["Porto"].isin(data))]

        self.df = port_cargo_year.to_numpy().tolist()

        self.my_notebook = my_notebook
        self.root = root
        self.bg_color = "#313131"
        self.fg_color = "#ffffff"

        self.frame = ttk.Frame(self.my_notebook)
        self.frame.pack(fill="both", expand=1)

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
        for value_df in self.df:
            self.my_tree.insert("", END, values=value_df)

        self.my_notebook.add(self.tree_frame, text="Lexic Table")

    # def close_tab(self, _=None):
    #    self.frame.destroy()

    """def change_color(self, bg_color, fg_color):
        self.my_text.config(background=bg_color, fg=fg_color)
        self.txt_box_output.config(background=bg_color, fg=fg_color)
        self.linenumbers.configure(bg=bg_color)
        self.bg_color = bg_color
        self.fg_color = fg_color"""
