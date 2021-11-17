class Tournament:
    def __init__ (self, name, place, start_date, end_date, rounds, players, time_control, description, status):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.round_numbers = 4
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description
        self.status = status