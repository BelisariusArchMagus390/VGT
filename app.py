from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
from .tab import Tab_editor
import os


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("TextPad")
        self.root.geometry("1200x680")

        # https://acervolima.com/o-que-o-atributo-tearoff-faz-em-um-menu-tkinter/
        self.root.option_add("*tearOff", False)

        self.style = ttk.Style(self.root)

        self.dir_path = Path(__file__).parent.joinpath("themes")
        self.root.tk.call("source", os.path.join(self.dir_path, "forest-light.tcl"))
        self.root.tk.call("source", os.path.join(self.dir_path, "forest-dark.tcl"))

        self.style.theme_use("forest-dark")

        self.root.resizable(False, False)

        self.my_notebook = ttk.Notebook(self.root)
        self.my_notebook.pack(pady=15)

        # self.tabs = []

        # tab = Tab_editor(self.my_notebook, self.status_bar, self.root)
        # self.tabs.append(tab)

        # Menu
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)

        # Adiciona Run Menu
        self.run_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Executar", menu=self.run_menu)
        self.run_menu.add_command(
            label="Executar", command=self.execute, accelerator="F5"
        )

        self.graph_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Gráficos", menu=self.graph_menu)
        self.graph_menu.add_command(
            label="Novo gráfico", command=self.new_graph, accelerator="Ctrl + F"
        )

        # Adiciona View Menu
        """self.view = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="View", menu=self.view)
        self.view.add_command(
            label="Dark Mode", command=self.change_theme_dark, accelerator="Crtl+D"
        )
        self.view.add_command(
            label="Light Mode",
            command=self.change_theme_light,
            accelerator="Ctrl+L",
        )"""

        # self.root.bind("<Control-F4>", self.close_tab)

        # Atalho de Run
        self.root.bind("<F5>", self.execute)

        # Atalho de novo gráfico
        self.root.bind("<Control-Key-f>", self.new_graph)

        # Atalhos de View
        # self.root.bind("<Control-Key-d>", self.change_theme_dark)
        # self.root.bind("<Control-Key-l>", self.change_theme_light)

        # Atalho para mudar de Tab
        self.root.bind("<Control-KeyPress-Tab>", self.change_tab)

        # Associando a função ao evento de mudança de tab
        self.my_notebook.bind("<<NotebookTabChanged>>", self.on_tab_text_change)

    def change_tab(self):
        idx = self.my_notebook.index(self.my_notebook.select())
        qt_tabs = self.my_notebook.index("end")

        if (idx + 1) < qt_tabs:
            self.my_notebook.select(idx + 1)

    def on_tab_text_change(self, event):
        tab = self.get_tab()
        self.status_bar.config(text=f"{tab.get_text_status_bar()}        ")
        self.root.title(f"{tab.get_text_title()} - TextPad")

    def execute(self, _=None):
        tab = self.get_tab()
        tab.execute()

    def get_tab(self):
        idx = self.my_notebook.index(self.my_notebook.select())
        tab = self.tabs[idx]
        return tab

    def new_graph():
        pass

    """def close_tab(self, _=None):
        if len(self.tabs) != 1:
            tab = self.get_tab()
            tab.close_tab()"""

    """def change_theme_light(self):
        bg_color = "#ffffff"
        fg_color = "#313131"

        self.change_color_general(bg_color, fg_color, "forest-light")

    def change_theme_dark(self):
        bg_color = "#313131"
        fg_color = "#ffffff"
        self.change_color_general(bg_color, fg_color, "forest-dark")

    def change_color_general(self, bg_color, fg_color, theme):
        self.style.theme_use(theme)
        self.root.configure(background=bg_color)
        self.status_bar.configure(background=bg_color, fg=fg_color)
        tab = self.get_tab()
        tab.change_color(bg_color, fg_color)
        self.change_color_menus(bg_color, fg_color)

    def change_color_menus(self, bg_color, fg_color):
        self.file_menu.configure(background=bg_color, foreground=fg_color)
        self.edit_menu.configure(background=bg_color, foreground=fg_color)
        self.run_menu.configure(background=bg_color, foreground=fg_color)
        self.view.configure(background=bg_color, foreground=fg_color)"""

    def startApp(self):
        self.root.mainloop()
