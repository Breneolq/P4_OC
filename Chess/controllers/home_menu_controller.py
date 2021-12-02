from views.home_menu_view import HomeMenuView
from .tournament_maker_controller import TournamentMakerController
from .going_back_tournament_controller import GoingBackTournamentController
from .player_controller import PlayerController
from .report_menu_controller import ReportMenuController
from .end_application_controller import EndApplicationController
from models.menu import Menu

"""Docstring"""
class HomeMenuController:
    """Docstring"""
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        self.menu.add("auto", "Creer un tournoi", TournamentMakerController())
        self.menu.add("auto", "Reprendre un tournoi", GoingBackTournamentController())
        self.menu.add("auto", "Ajouter un joueur dans la base de donnée", PlayerController())
        self.menu.add("auto", "Generer un rapport", ReportMenuController())
        self.menu.add("q", "Quitter l'application", EndApplicationController())
        
        user_choice = self.view.get_user_choice()

        return user_choice.controller