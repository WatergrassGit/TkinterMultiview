import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    """Controller for model and views."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.wm_title("Multi View")

        self.callbacks = {}
        