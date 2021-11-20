from ..views.home_menu_view import HomeMenuView
from .tournament_controller import TournamentMakerController
from ..models.menu import Menu

"""Docstring"""
class HomeMenuController:
    """Docstring"""
    def __init__(self):
        self.view = HomeMenuView(self.menu)
        self.menu = Menu()

    def __call__(self):
        self.menu.add("auto", "Creer un tournoi", TournamentMakerController())
        
        return