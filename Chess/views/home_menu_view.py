from ..models.menu import Menu
"""Docstring"""
class HomeMenuView:
    """Docstring"""

    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print()
        print("Accueil de gestion:")
        print()
        for key, entry in self.menu.items():
             print (f"{key}: {entry}")
        print()

    def get_user_choice(self):
        while True:
            #afficher le menu
            self._display_menu()
            #demander à l'utilisateur un choix
            choice = input(">> ")
            #valider le choix
            if choice in self.menu:
                #return choice
                return self.menu[choice]