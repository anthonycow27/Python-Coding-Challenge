"""
Module for providing a HTML in string format
for future use
"""


class HTMLText:
    def __init__(self):
        pass

    def get_string(self):
        new_str = ""
        path = 'html/example.html'
        with open((path), "r") as f:
            html_str = f.read()
            new_str = html_str
        return new_str
