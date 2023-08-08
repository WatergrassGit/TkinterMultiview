import tkinter as tk
from tkinter import ttk


class StyleSheet(ttk.Style):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.configure('masthead.TLabel', font=('Helvetica', 18))
        self.configure('header.TLabel', font=('helvetica', 12))

        self.set_theme('light')

    def set_theme(self, theme):
        if theme == 'light':
            self.set_theme_light()
        else:
            self.set_theme_dark()

    def set_theme_light(self):
        bg = '#EDEAE0'  # Alabaster
        text_color = 'maroon'

        self.set_background_color(bg)
        self.set_label_color(text_color)

    def set_theme_dark(self):
        bg = '#4E6E81'  # Aegean Blue
        text_color = '#F0EFE7'  # White Dove

        self.set_background_color(bg)
        self.set_label_color(text_color)

    def set_background_color(self, bg):
        self.configure('TFrame', background=bg)
        self.configure('TLabel', background=bg)
        self.configure('TButton', background=bg)
        self.configure('TRadiobutton', background=bg)

    def set_label_color(self, text_color):
        self.configure('TLabel', foreground=text_color)
        self.configure('TRadiobutton', foreground=text_color)
