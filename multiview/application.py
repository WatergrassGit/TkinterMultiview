import tkinter as tk
from tkinter import ttk
from . models import DataModel
from . import views as v

class Application(tk.Tk):
    """Controller for model and views."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.wm_title("Multi View")
        self.geometry("600x400")

        self.callbacks = {}

        self.datamodel = DataModel()

        # initialize views
        self.homepage = v.HomePage(self, self.callbacks)
        self.objectpage = v.ObjectPage()
        self.detailpage = v.DetailPage()
        self.visibilitypage = v.VisibilityPage()

        # initialize Homepage view
        self.homepage.pack(fill="both", expand=True)
