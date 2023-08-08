import tkinter as tk
from tkinter import ttk


class StyleSheet(ttk.Style):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.configure('masthead.TLabel', font=('Helvetica', 18))
        self.configure('header.TLabel', font=('helvetica', 12))

        #self.configure('TButton', foreground='maroon')
        #self.configure('home.TButton', foreground='green')
