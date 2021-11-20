from Chess.Controllers.home_menu_controller import HomeMenuController
from .home_menu_controller import HomeMenuController

"""Docstring"""

class ApplicationController:
    
    """Docstring"""
    
    def __init__(self):
        self.controller = None
    
    def start(self):
        self.controller = HomeMenuController()
