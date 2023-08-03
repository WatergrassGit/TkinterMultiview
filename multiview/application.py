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

        self.callbacks = {
            'get_objects': self.get_objects,
            'set_object': self.set_object,
            'display_homepage': self.display_homepage,
            'display_object_view': self.display_object_view,
            'get_details': self.get_details,
            'display_detail_view': self.display_detail_view,
        }

        # keep track of view object and detail page
        self.active_view = {
            'object': None,
            'detail': None,
        }

        self.datamodel = DataModel()

        # create view objects
        self.homepage = v.HomePage(self, self.callbacks)
        self.objectpage = v.ObjectPage(self, self.callbacks)
        self.detailpage = v.DetailPage(self, self.callbacks)
        self.visibilitypage = v.VisibilityPage()

        # initialize view
        self.homepage.grid(row=0, column=0, sticky="nsew")
        self.objectpage.grid(row=0, column=0, sticky="nsew")
        self.detailpage.grid(row=0, column=0, sticky="nsew")

        # configure rows and columns with weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # start with Homepage on top
        self.show_view(self.homepage)

    def get_objects(self):
        """Returns keys from model's data attribute as a list."""

        return list(self.datamodel.data.keys())
    
    def show_view(self, view):
        """Displays the inputted view at the top."""

        view.tkraise()

    def display_homepage(self):
        """Display the Homepage."""

        self.active_view.update({'object': None, 'detail': None})
        self.show_view(self.homepage)

    def display_object_view(self, obj):
        """
        Displays the object view corresponding to input at the top.
        
        
        :arguments
        ----------
        obj : string
            name of asssociated object to be displayed in the Object Page
        """

        self.objectpage.refresh_page(obj)
        self.active_view.update({'object': obj, 'detail': None})
        self.show_view(self.objectpage)

    def set_object(self, obj):
        self.active_view.update({'object': obj})

    def get_details(self):
        """
        Returns keys from model's data attribute for a given object as a list.
        """

        return list(self.datamodel.data[self.active_view['object']].keys())
    
    def display_detail_view(self, det):
        """
        Displays the detail view corresponding to input argument det and
        the current active view.
        
        
        :arguments
        ----------
        det : string
            name of asssociated detail page to be displayed in the Detail Page
        """

        obj = self.active_view['object']
        message = self.datamodel.data[obj][det]['text']

        self.detailpage.refresh_page(obj, det, message)
        self.active_view.update({'detail': det})
        self.show_view(self.detailpage)
