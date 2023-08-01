class DataModel:
    """Model which contains data."""

    def __init__(self):
        self.data = {
            'object 1': {
                'detail 1': {
                    'visible': True,
                    'text': "The Python programming language was first released on February 20, 1991."
                },
                'detail 2': {
                    'visible': True,
                    'text': "The Python 3.0 release date was December 3, 2008."
                },
                'detail 3': {
                    'visible': True,
                    'text': "The original creator of Python is Guido van Rossum."
                },
            },
            'object 2': {
                'detail 1': {
                    'visible': True,
                    'text': "Tkinter is a GUI toolkit for Python released in 1991."
                },
                'detail 2': {
                    'visible': True,
                    'text': "Tkinter stands for Tk interface."
                },
            },
        }

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, new_data):
        self._data = new_data
