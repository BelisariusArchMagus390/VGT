from tkinter import ttk
import pandas


class Tab_table:
    def __init__(self, my_notebook: ttk.Notebook, data, port_cargo):
        self.data = data
        self.port_cargo = port_cargo.loc[port_cargo["Porto"].isin(self.data)]
        self.years = self.port_cargo["Ano"].drop_duplicates().to_list()

        self.my_notebook = my_notebook
        # self.bg_color = "#313131"
        # self.fg_color = "#ffffff"

        self.tree_frame = ttk.Frame(self.my_notebook)
        self.tree_frame.pack(fill="both", expand=1)

        self.final_dataframe = port_cargo

        # Scrollbar vertical da Text box
        self.tree_scroll = ttk.Scrollbar(self.tree_frame)
        # Pack da Scrollbar
        self.tree_scroll.pack(side="right", fill="y")

        self.years_options = ttk.Combobox(
            self.tree_frame, state="readonly", values=["Todos os anos"] + self.years
        )
        self.years_options.current(0)
        self.years_options.pack(padx=5, pady=5)

        # Evento que se ativa sempre que for selecionado uma opção no Combobox
        self.years_options.bind("<<ComboboxSelected>>", self.filter_table)

        # Define o nome das colunas
        columns = list(self.port_cargo.columns)

        self.my_tree = ttk.Treeview(
            self.tree_frame,
            yscrollcommand=self.tree_scroll.set,
            selectmode="extended",
            height=500,
        )
        self.my_tree["columns"] = columns
        self.my_tree.pack(expand="true", fill="both")

        # Configuração da Scrollbar
        self.tree_scroll.config(command=self.my_tree.yview)

        # Preparando a tabela
        for item_table in columns:
            self.my_tree.column(item_table, anchor="center", width=120)
            self.my_tree.heading(item_table, text=item_table, anchor="center")
        
        # Inserindo dados na TreeView
        for index, row in self.port_cargo.iterrows():
            self.my_tree.insert("", "end", text=index, values=list(row))

        notebook_size = self.my_notebook.index("end")
        title = "Cluster "

        if notebook_size == 0:
            title = title+"1"
        elif notebook_size == 1:
            title = title+"2"
        else:
            title = title+str(notebook_size)

        
        self.my_notebook.add(self.tree_frame, text=title)

    def filter_table(self, _=None):
        self.my_tree.delete(*self.my_tree.get_children())

        option = self.years_options.get()

        if option != "Todos os anos":
            years = [int(option)]
        else:
            years = self.years

        port_cargo_filtered = self.port_cargo.loc[(self.port_cargo["Ano"].isin(years))]

        for index, row in port_cargo_filtered.iterrows():
            self.my_tree.insert("", "end", text=index, value=list(row))

        self.final_dataframe = port_cargo_filtered

    def get_final_dataframe(self):
        return self.final_dataframe

    """def change_color(self, bg_color, fg_color):
        self.my_text.config(background=bg_color, fg=fg_color)
        self.txt_box_output.config(background=bg_color, fg=fg_color)
        self.linenumbers.configure(bg=bg_color)
        self.bg_color = bg_color
        self.fg_color = fg_color"""
