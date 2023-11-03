from admin import Admin
from visitor import Visitor
from card import Card
import time
import sys


class System:
    def __init__(self):
        self.visitors = []
        self.cards = [
            Card(0, "Visitor", "V001"),
            Card(1, "Visitor", "V002"),
            Card(2, "Visitor", "V003"),
            Card(3, "Visitor", "V004"),
            Card(4, "Visitor", "V005"),
            Card(5, "Visitor", "V006"),
            Card(6, "Visitor", "V007"),
            Card(7, "Visitor", "V008"),
            Card(8, "Visitor", "V009"),
            Card(9, "Visitor", "V010"),
            Card(10, "Tenant", "T001"),
            Card(11, "Tenant", "T002"),
            Card(12, "Tenant", "T003"),
        ]
        self.admin = Admin("admin", "password")
        self.temporarys = []

    def log_in_as_admin(self):
        while True:
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if username == self.admin.username and password == self.admin.password:
                print("Login successful.")
                break
            else:
                print("Invalid credentials. Please try again.")

    def log_in_as_visitor(self):
        # id
        if len(self.visitors) == 0:
            id = 0
        else:
            for i in range(len(self.visitors)):
                if self.visitors[i]['id'] != i:
                    id = i
                    break
            else:
                id = i + 1
        # id card
        for card in self.cards:
            if card["type"] == "Visitor" and card["status"] == False:
                id_card = card["number_card"]
                card.take_card()
                break
        else:
            print("No card left, please contact the officer.")
            return
        # name

        name = input("Enter visitor name: ")

        # identity card
        print("1. KTP\n2. SIM\n3. Passport")
        while True:
            identity_card = input(
                "Enter visitor identity card: ")
            if identity_card not in ["1", "2", "3"]:
                print("Invalid option. Please try again.")
                continue
            if identity_card == "1":
                identity_card = "KTP"
                break
            elif identity_card == "2":
                identity_card = "SIM"
                break
            elif identity_card == "3":
                identity_card = "Passport"
                break

        visitor = Visitor(id, name, identity_card, id_card)
        visitor.check_in()
        self.visitors.append(visitor)

    def log_out_as_visitor(self):
        id_card = input("Enter your visitor number card: ")
        for visitor in self.visitors:
            if visitor["id_card"] == id_card and visitor["time_out"] == None:
                visitor.check_out()
                for card in self.cards:
                    if card["number_card"] == visitor["id_card"]:
                        card.return_card()
                        break
                break
        else:
            print(f"{id_card} not found or already checked out.")

    def run(self):
        while True:
            print("")
            print("Welcome to Sinarmas Land Surabaya")
            print("Please choose an option:")
            print("1. Log in as a admin")
            print("2. Log in as a visitor")
            print("3. Log out as a visitor")

            option = input("Enter your choice: ")
            if option not in ["1", "2", "3"]:
                print("Invalid option. Please try again.")
                continue
            if option == "1":
                self.log_in_as_admin()
                while True:
                    print("")
                    print("Welcome admin")
                    print("Please choose an option:")
                    print("1. Create data")
                    print("2. Dislay data")
                    print("3. Update a visitor")
                    print("4. Detele a card")
                    print("5. Trash bin")
                    print("6. Log out")
                    print("0. Shut down")

                    option = input("Enter your choice: ")
                    if option not in ["1", "2", "3", "4", "5", "6", "0"]:
                        print("Invalid option. Please try again.")
                        continue
                    if option == "1":
                        while True:
                            print("")
                            print("Please choose an option:")
                            print("1. Create a visitor")
                            print("2. Create a card")
                            print("0. Back")
                            option = input("Enter your choice: ")
                            if option not in ["1", "2", "0"]:
                                print("Invalid option. Please try again.")
                                continue
                            if option == "1":
                                self.admin.create_visitor(
                                    self.visitors, self.cards)
                            elif option == "2":
                                self.admin.create_card(self.cards)
                            elif option == "0":
                                break
                    elif option == "2":
                        while True:
                            print("")
                            print("Please choose an option:")
                            print("1. Display specific visitor")
                            print("2. Display all visitor")
                            print("3. Display specific card")
                            print("4. Display all card")
                            print("0. Back")
                            option = input("Enter your choice: ")
                            if option not in ["1", "2", "3", "4", "0"]:
                                print("Invalid option. Please try again.")
                                continue
                            if option == "1":
                                self.admin.display_specific_visitors(
                                    self.visitors)
                            elif option == "2":
                                self.admin.display_all_visitors(self.visitors)
                            elif option == "3":
                                self.admin.display_specific_cards(self.cards)
                            elif option == "4":
                                self.admin.display_all_cards(self.cards)
                            elif option == "0":
                                break
                        self.admin.display_all_visitors(self.visitors)
                    elif option == "3":
                        self.admin.update_visitor(self.visitors, self.cards)
                    elif option == "4":
                        self.admin.delete_card(self.cards, self.temporarys)

                    elif option == "5":
                        while True:
                            print("")
                            print("Please choose an option:")
                            print("1. Restore data")
                            print("2. Delete pemanently")
                            print("0. Back")
                            option = input("Enter your choice: ")
                            if option not in ["1", "2", "0"]:
                                print("Invalid option. Please try again.")
                                continue
                            if option == "1":
                                self.admin.restore_data(
                                    self.cards, self.temporarys)
                            elif option == "2":
                                self.admin.delete_permanently(
                                    self.temporarys)
                            elif option == "0":
                                break
                    elif option == "6":
                        break
                    elif option == "0":
                        print("Thank you for using the visitor management system.")
                        sys.exit(0)
            elif option == "2":
                self.log_in_as_visitor()
            elif option == "3":
                self.log_out_as_visitor()
