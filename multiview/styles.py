import tkinter as tk
from tkinter import ttk


class StyleSheet(ttk.Frame):
    def __init__(self, master, callbacks, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.callbacks = callbacks

        self.master = master

        self.styles = ttk.Style()

        self.styles.configure('masthead.TLabel', font=('Helvetica', 18))
        self.styles.configure('header.TLabel', font=('helvetica', 12))

        #self.styles.configure('TButton', foreground='maroon')
        #self.styles.configure('home.TButton', foreground='green')
