from tkinter import *
from tkinter import ttk
import pandas as pd


class Tab_table:
    def __init__(self, my_notebook: ttk.Notebook, data, port_cargo):
        self.data = data
        self.port_cargo = port_cargo
        self.years = self.port_cargo["Ano"].drop_duplicates().to_list()

        self.my_notebook = my_notebook
        self.bg_color = "#313131"
        self.fg_color = "#ffffff"

        self.tree_frame = ttk.Frame(self.my_notebook)
        self.tree_frame.pack(fill="both", expand=1)

        self.years_options = ttk.Combobox(
            self.tree_frame, state="readonly", values=["Todos os anos"] + self.years
        )
        self.years_options.pack(padx=5, pady=5)

        # Scrollbar vertical da Text box
        self.tree_scroll = ttk.Scrollbar(self.tree_frame)
        # Pack da Scrollbar
        self.tree_scroll.pack(side="right", fill="y")

        self.my_notebook.add(self.tree_frame, text="Cluster 1")

        self.years_options.bind("<<ComboboxSelected>>", self.create_treeview)

    def create_treeview(self, _=None):
        option = self.years_options.get()

        if option != "Todos os anos":
            self.years = [int(option)]

        port_cargo_year = self.port_cargo.loc[(self.port_cargo["Ano"].isin(self.years))]
        self.port_cargo = port_cargo_year.loc[
            (port_cargo_year["Porto"].isin(self.data))
        ]

        my_tree = ttk.Treeview(
            self.tree_frame,
            yscrollcommand=self.tree_scroll.set,
            selectmode="extended",
            height=500,
        )
        my_tree.pack()

        # Configuração da Scrollbar
        self.tree_scroll.config(command=my_tree.yview)

        # Define o nome das colunas
        my_tree["columns"] = (
            "Ano",
            "UF",
            "Porto",
            "TipoNavegacao",
            "Sentido",
            "CDMercadoria",
            "TEU",
            "QTCarga",
            "PesoCargaBruta",
            "PesoCargaLiquida",
            "ValorKgCarga",
        )

        # Formatando as colunas
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Ano", anchor="center", width=100)
        my_tree.column("UF", anchor="center", width=100)
        my_tree.column("Porto", anchor="center", width=140)
        my_tree.column("TipoNavegacao", anchor="center", width=140)
        my_tree.column("Sentido", anchor="center", width=140)
        my_tree.column("CDMercadoria", anchor="center", width=140)
        my_tree.column("TEU", anchor="center", width=140)
        my_tree.column("QTCarga", anchor="center", width=140)
        my_tree.column("PesoCargaBruta", anchor="center", width=140)
        my_tree.column("PesoCargaLiquida", anchor="center", width=140)
        my_tree.column("ValorKgCarga", anchor="center", width=100)

        # Criando Headings
        my_tree.heading("#0", text="", anchor="w")
        my_tree.heading("Ano", text="Ano", anchor="center")
        my_tree.heading("UF", text="UF", anchor="center")
        my_tree.heading("Porto", text="Porto", anchor="center")
        my_tree.heading("TipoNavegacao", text="TipoNavegacao", anchor="center")
        my_tree.heading("Sentido", text="Sentido", anchor="center")
        my_tree.heading("CDMercadoria", text="CDMercadoria", anchor="center")
        my_tree.heading("TEU", text="TEU", anchor="center")
        my_tree.heading("QTCarga", text="QTCarga", anchor="center")
        my_tree.heading("PesoCargaBruta", text="PesoCargaBruta", anchor="center")
        my_tree.heading("PesoCargaLiquida", text="PesoCargaLiquida", anchor="center")
        my_tree.heading("ValorKgCarga", text="ValorKgCarga", anchor="center")

        # Inserindo dados na TreeView
        for index, row in self.port_cargo.iterrows():
            my_tree.insert("", 0, text=index, values=list(row))

    # def close_tab(self, _=None):
    #    self.frame.destroy()

    """def change_color(self, bg_color, fg_color):
        self.my_text.config(background=bg_color, fg=fg_color)
        self.txt_box_output.config(background=bg_color, fg=fg_color)
        self.linenumbers.configure(bg=bg_color)
        self.bg_color = bg_color
        self.fg_color = fg_color"""
