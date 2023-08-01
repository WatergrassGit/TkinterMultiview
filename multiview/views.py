import tkinter as tk
from tkinter import ttk


class HomePage(ttk.Frame):
    """
    View which displays content when application is first loaded
    and allows object selection.
    """

    def __init__(self, master, callbacks, *args, **kwargs):
        """
        Initialize HomePage

        :arguments
        ----------
        master : tkinter object
            object that MainView resides in
        callbacks : dictionary
            contains references to callable methods in `master`
        """

        super().__init__(master, *args, **kwargs)

        self.callbacks = callbacks

        self.masthead = ttk.Label(self, text="Homepage")
        self.intro = ttk.Label(self, text="Welcome to this project\nSelect an object below.")
        self.frame = ttk.Frame(self)

        # buttons to go into the frame
        self.objects = self.callbacks['get_objects']()  # get objects as a list

        self.frame_btns = []
        for obj in self.objects:
            self.frame_btns.append(
                ttk.Button(self.frame, text=obj.title())
            )

        for btn in self.frame_btns:
            btn.pack()

        # set object in view using grid geometry manager
        self.masthead.grid(row=0, column=0)
        self.intro.grid(row=1, column=0)
        self.frame.grid(row=2, column=0)


class ObjectPage(ttk.Frame):
    pass


class DetailPage(ttk.Frame):
    pass


class VisibilityPage(ttk.Frame):
    pass
