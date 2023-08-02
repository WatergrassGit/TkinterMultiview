import tkinter as tk
from tkinter import ttk
from functools import partial


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
            object that HomePage resides in
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
                ttk.Button(self.frame, text=obj.title(), command=partial(self.display_object_view, obj))
            )

        for btn in self.frame_btns:
            btn.pack()

        # set object in view using grid geometry manager
        self.masthead.grid(row=0, column=0)
        self.intro.grid(row=1, column=0)
        self.frame.grid(row=2, column=0)

    def display_object_view(self, obj):
        self.callbacks['display_object_view'](obj)


class ObjectPage(ttk.Frame):
    """
    View for selected object.
    """

    def __init__(self, master, callbacks, *args, **kwargs):
        """
        Initialize Object View

        :arguments
        ----------
        master : tkinter object
            object that ObjectPage resides in
        callbacks : dictionary
            contains references to callable methods in `master`
        """

        super().__init__(master, *args, **kwargs)

        self.callbacks = callbacks

        self.masthead_title_text = tk.StringVar()

        self.masthead = ttk.Frame(self)
        self.masthead_title = ttk.Label(self.masthead, textvariable=self.masthead_title_text)
        self.masthead_title.grid(row=0, column=0, sticky='w')
        self.masthead_button = ttk.Button(self.masthead, text="Home", command=self.callbacks['display_homepage'])
        self.masthead_button.grid(row=0, column=1, sticky='e')
        self.masthead.grid_columnconfigure(1, weight=1)
        self.masthead.grid(row=0, column=0, sticky='nsew')

        # configure rows and columns with weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # frame to hold buttons
        self.frame = ttk.Frame(self)
        self.frame.grid(row=2, column=0)

    def refresh_page(self, obj):
        self.masthead_title_text.set(f"Object Page - {obj.title()}")
        self.masthead.grid(row=0, column=0)

        self.callbacks['set_object'](obj)

        # buttons to go into the frame
        self.details = self.callbacks['get_details']()  # get details as a list

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.frame_btns = []
        for det in self.details:
            self.frame_btns.append(
                ttk.Button(self.frame, text=det.title(), command=partial(self.display_detail_view, det))
            )

        for btn in self.frame_btns:
            btn.pack()


    def display_detail_view(self, det):
        print(det)
        #self.callbacks['display_detail_view'](det)


class DetailPage(ttk.Frame):
    pass


class VisibilityPage(ttk.Frame):
    pass
