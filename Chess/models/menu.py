"""Docstring"""
class MenuEntry:
    def __init__(self, option, handler):
        self.option = option
        self.controller = handler
    
    def __str__(self):
        return str(self.option)


class Menu:
    """Docstring"""
    def __init__(self):
        self._entries = {}
        self._autokey = 1

    def add(self, key, option, handler):
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1

        self._entries[str(key)] = MenuEntry(option, handler)
    
    def items(self):
        return self._entries.items()
    
    def __contains__(self, choice):
        return str(choice) in self._entries
    
    def __getitem__(self, choice):
        return self._entries[choice]