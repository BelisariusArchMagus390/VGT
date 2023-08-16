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

        # Scrollbar vertical da Text box
        self.ver_scroll = ttk.Scrollbar(self.frame, orient="vertical")

        # Scrollbar horizontal da Text box
        self.hor_scroll = ttk.Scrollbar(self.frame, orient="horizontal")

        # Configuração das Scrollbars
        self.ver_scroll.config(command=self.my_text.yview)
        self.hor_scroll.config(command=self.my_text.xview)

        # Pack dos Scrollbars
        self.ver_scroll.pack(side="right", fill="y")
        self.hor_scroll.pack(side="bottom", fill="x")

        self.my_text.pack(side="top", fill="both", expand=True)
        self.my_notebook.add(self.frame, text="New File")

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
