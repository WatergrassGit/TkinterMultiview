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

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)  

        self.masthead = ttk.Label(self, text="Homepage", style='masthead.TLabel')
        self.intro = ttk.Label(self, text="Welcome to this project! Select a choice below.")
        self.frame = ttk.Frame(self)
        self.footer = ttk.Frame(self)

        # buttons to go into the frame
        self.objects = self.callbacks['get_objects']()  # get objects as a list

        self.frame_btns = []
        for obj in self.objects:
            self.frame_btns.append(
                ttk.Button(self.frame, text=obj.title(), command=partial(self.display_object_view, obj))
            )

        for btn in self.frame_btns:
            btn.pack()

        # set up footer
        self.footer_home_btn = ttk.Button(self.footer, text='Home', command=self.callbacks['display_homepage'])
        self.footer_settings_btn = ttk.Button(self.footer, text='Settings', command=self.callbacks['display_settings_view'])
        self.footer_home_btn.grid(row=0, column=0)
        self.footer_settings_btn.grid(row=0, column=1)

        # set object in view using grid geometry manager
        self.masthead.grid(row=0, column=0)
        self.intro.grid(row=1, column=0)
        self.frame.grid(row=2, column=0)
        self.footer.grid(row=3, column=0, sticky='w')

    def display_object_view(self, obj):
        self.callbacks['display_object_view'](obj)


class ObjectPage(ttk.Frame):
    """
    View for selected object page.
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

        # configure rows and columns with weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)  

        # section for masthead
        self.masthead = ttk.Frame(self)
        self.masthead.grid_columnconfigure(1, weight=1)
        self.masthead.grid(row=0, column=0, sticky='nsew')

        self.masthead_title = ttk.Label(self.masthead, text='Object Page', style='masthead.TLabel')
        self.masthead_back_btn = ttk.Button(self.masthead, text="Back", command=self.callbacks['display_homepage'])
        self.masthead_title.grid(row=0, column=0, sticky='w')
        self.masthead_back_btn.grid(row=0, column=1, sticky='e')

        # section for object page header
        self.header_text = tk.StringVar()
        self.header = ttk.Label(self, textvariable=self.header_text, style='header.TLabel')
        self.header.grid(row=1, column=0, sticky='w')

        # section for object page content
        self.frame = ttk.Frame(self)
        self.frame.grid(row=2, column=0)

        # set up footer
        self.footer = ttk.Frame(self)

        self.footer.grid(row=3, column=0, sticky='w')        

        self.footer_home_btn = ttk.Button(self.footer, text='Home', command=self.callbacks['display_homepage'])
        self.footer_settings_btn = ttk.Button(self.footer, text='Settings', command=self.callbacks['display_settings_view'])
        self.footer_home_btn.grid(row=0, column=0)
        self.footer_settings_btn.grid(row=0, column=1)

    def refresh_page(self, obj):
        self.header_text.set(f"{obj.title()}")
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
        self.callbacks['display_detail_view'](det)


class DetailPage(ttk.Frame):
    """
    View for selected detail page.
    """

    def __init__(self, master, callbacks, *args, **kwargs):
        """
        Initialize Detail Page View.
        Create detail page using masthead, header and content blocks.

        :arguments
        ----------
        master : tkinter object
            object that DetailPage resides in
        callbacks : dictionary
            contains references to callable methods in `master`
        """

        super().__init__(master, *args, **kwargs)

        self.callbacks = callbacks

        # configure rows and columns with weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)  

        # section for masthead
        self.masthead = ttk.Frame(self)
        self.masthead.grid(row=0, column=0, sticky='nswe')
        self.masthead.grid_columnconfigure(1, weight=1)

        self.masthead_title = ttk.Label(self.masthead, text= "Detail Page", style='masthead.TLabel')
        self.masthead_back_button = ttk.Button(self.masthead, text="Back", command=self.callbacks['change_view_detail_to_object'])
        self.masthead_title.grid(row=0, column=0, sticky='w')
        self.masthead_back_button.grid(row=0, column=1, sticky='e')

        # section for detail page header
        self.header_text = tk.StringVar()
        self.header = ttk.Label(self, textvariable=self.header_text, style='header.TLabel')
        self.header.grid(row=1, column=0, sticky='w')

        # section for detail page content
        self.frame = ttk.Frame(self)
        self.frame.grid(row=2, column=0)

        # set up footer
        self.footer = ttk.Frame(self)

        self.footer.grid(row=3, column=0, sticky='w')        

        self.footer_home_btn = ttk.Button(self.footer, text='Home', command=self.callbacks['display_homepage'])
        self.footer_settings_btn = ttk.Button(self.footer, text='Settings', command=self.callbacks['display_settings_view'])
        self.footer_home_btn.grid(row=0, column=0)
        self.footer_settings_btn.grid(row=0, column=1)

    def refresh_page(self, obj, det, message):
        self.header_text.set(f"{obj.title()}: {det.title()}")

        for widget in self.frame.winfo_children():
            widget.destroy()

        ttk.Label(self.frame, text=message).pack()


class SettingsPage(ttk.Frame):
    """
    View for Settings.
    """

    def __init__(self, master, callbacks, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.callbacks = callbacks

        # configure rows and columns with weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)  

        # section for masthead
        self.masthead = ttk.Frame(self)

        self.masthead.grid(row=0, column=0, sticky='nswe')
        self.masthead.grid_columnconfigure(1, weight=1)

        self.masthead_title = ttk.Label(self.masthead, text='Settings', style='masthead.TLabel')
        self.masthead_back_btn = ttk.Button(self.masthead, text='Back', command=self.callbacks['close_settings_view'])
        self.masthead_title.grid(row=0, column=0, sticky='w')
        self.masthead_back_btn.grid(row=0, column=1, sticky='e')

        # section for header
        self.header = ttk.Label(self, text='Change the settings below.')
        self.header.grid(row=1, column=0, sticky='w')

        # section for body
        self.body = ttk.Frame(self)
        self.body.grid(row=2, column=0)

        self.lighting = tk.StringVar()
        self.theme = 'light'
        self.lighting.set(self.theme)
        self.setting_light_mode = ttk.Radiobutton(self.body, text='Light Mode', variable=self.lighting, value='light', command=self.change_lighting)
        self.setting_dark_mode = ttk.Radiobutton(self.body, text='Dark Mode', variable=self.lighting, value='dark', command=self.change_lighting)

        self.setting_light_mode.grid(row=0, column=0)
        self.setting_dark_mode.grid(row=0, column=1)

        # section for footer
        self.footer = ttk.Frame(self)

        self.footer.grid(row=3, column=0, sticky='w')

        self.footer_home_btn = ttk.Button(self.footer, text='Home', command=self.callbacks['display_homepage'])
        self.footer_home_btn.grid(row=0, column=0)

    def change_lighting(self):

        lighting = self.lighting.get()
        if self.theme != lighting:
            self.theme = lighting
            self.callbacks['update_theme'](self.theme)
    