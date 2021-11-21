from ..controllers import home_menu_controller
from ..models.menu import Menu
from ..views.report_menu_view import ReportMenuView

"""Docstring"""
class ReportMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = ReportMenuView(self.menu)
    
    def __call__(self):
        self.menu.add("auto", "Liste de tous les joueurs", ReportPlayerListController())
        self.menu.add("auto", "liste de tous les tournois", ReportTournamentListController())
        self.menu.add("auto", "Retour", home_menu_controller.HomeMenuController())
        self.menu.add("q", "Quitter l'application", lambda:None)
        
        user_choice = self.view.get_user_choice()

        return user_choice.controller

class ReportPlayerListController:
    def __init__(self):
        self.menu = Menu()
        self.view = ReportMenuView(self.menu)
    
    def __call__(self):
        self.menu.add("", "Liste des joueurs :", None)
        self.menu.add("auto", "Par ordre alphabétique", lambda:None)
        self.menu.add("auto", "Par classement", lambda:None)
        self.menu.add("auto", "Retour", ReportMenuController())
        self.menu.add("q", "Quitter l'application", lambda:None)

        user_choice = self.view.get_user_choice()

        return user_choice.controller

class ReportTournamentListController:
    def __init__(self):
        self.menu = Menu()
        self.view = ReportMenuView(self.menu)
    
    def __call__(self):
        self.menu.add("auto", "Retour", ReportMenuController())
        self.menu.add("q", "Quitter l'application", lambda:None)

        user_choice = self.view.get_user_choice()

        return user_choice.controller

