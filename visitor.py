from datetime import datetime
import random
import string


class Visitor:
    def __init__(self, id, name, identity_card, id_card):
        self.id = id
        self.name = name
        self.identity_card = identity_card
        self.id_card = id_card
        self.time_enter = None
        self.time_out = None

    def check_in(self):
        self.time_enter = datetime.now().replace(microsecond=0)
        print(
            f"Visitor {self.name} checked in successfully at {self.time_enter}.\nPlease take your {self.id_card} visitor card.")

    def check_out(self):
        self.time_out = datetime.now().replace(microsecond=0)
        print(
            f"Visitor {self.name} checked out successfully at {self.time_out}.\nPlease take your {self.identity_card} card.")

    def __getitem__(self, key):
        return getattr(self, key)

    # def __str__(self):
    #     return f"Visitor(id={self.id}, name={self.name}, identity_card={self.identity_card}, id_card={self.id_card}, time_enter={self.time_enter}, time_out={self.time_out})"

    def __setitem__(self, key, value):
        setattr(self, key, value)
