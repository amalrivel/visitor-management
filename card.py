class Card:
    def __init__(self, id, type, number_card):
        self.id = id
        self.type = type
        self.number_card = number_card
        self.status = False

    def take_card(self):
        self.status = True

    def return_card(self):
        self.status = False

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)