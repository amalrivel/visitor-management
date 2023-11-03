from visitor import Visitor
from card import Card
from tabulate import tabulate


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_visitor(self, visitors, cards):
        # id
        if len(visitors) == 0:
            id = 0
        else:
            for i in range(len(visitors)):
                if visitors[i]['id'] != i:
                    id = i
                    break
            else:
                id = i + 1
        # type card
        print("1. Visitor\n2. Tenant")
        while True:
            type = input(
                "Enter visitor identity card: ")
            if type not in ["1", "2"]:
                print("Invalid option. Please try again.")
                continue
            if type == "1":
                type = "Visitor"
                break
            elif type == "2":
                type = "Tenant"
                break
        # id card
        for card in cards:
            if card["type"] == type and card["status"] == False:
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
        visitors.append(visitor)

    def create_card(self, cards):
        # id
        if len(cards) == 0:
            id = 0
        else:
            for i in range(len(cards)):
                if cards[i]['id'] != i:
                    id = i
                    break
            else:
                id = i + 1
        # type card
        print("1. Visitor\n2. Tenant")
        while True:
            type = input(
                "Enter visitor type card: ")
            if type not in ["1", "2"]:
                print("Invalid option. Please try again.")
                continue
            if type == "1":
                type = "Visitor"
                break
            elif type == "2":
                type = "Tenant"
                break
        while True:
            if type == "Visitor":
                number_card = input(
                    "Enter number card: V")
                if not number_card.isdigit():
                    print("Card number must be number.\nPlease try agian")
                    continue
                elif not len(number_card) == 3:
                    print("Card number must 3 digits.\nPlease try agian")
                    continue
                number_card = "V" + number_card
            else:
                number_card = input(
                    "Enter number card: T")
                if not number_card.isdigit():
                    print("Card number must be number.\nPlease try agian")
                    continue
                elif not len(number_card) == 3:
                    print("Card number must 3 digits.\nPlease try agian")
                    continue
                number_card = "T" + number_card
            for card in cards:
                if card["number_card"] == number_card:
                    print("Card already exists")
                    break
            else:
                break

        card = Card(id, type, number_card)
        cards.append(card)
        print(f"Creating {number_card} card successfully")

    def display_all_visitors(self, visitors):
        data = {
            "Id": [visitor["id"] for visitor in visitors],
            "Name": [visitor["name"] for visitor in visitors],
            "Identity Card": [visitor["identity_card"] for visitor in visitors],
            "ID Card": [visitor["id_card"] for visitor in visitors],
            "Time enter": [visitor["time_enter"] for visitor in visitors],
            "Time out": [visitor["time_out"] for visitor in visitors],
        }
        print(tabulate(data, headers="keys"))

    def display_specific_visitors(self, visitors):
        print("Search by:\n1. Name\n2. ID Card")
        while True:
            option = input("Enter your choice: ")
            if option not in ["1", "2"]:
                print("Invalid option. Please try again.")
                continue
            if option == "1":
                name = input("Enter visitor name: ")
                data = [visitor for visitor in visitors if visitor["name"] == name]
                break
            elif option == "2":
                id_card = input("Enter ID card number: ")
                data = [
                    visitor for visitor in visitors if visitor["id_card"] == id_card]
                break
        if len(data) == 0:
            print("Data not found")
            return
        data = {
            "Id": [visitor["id"] for visitor in data],
            "Name": [visitor["name"] for visitor in data],
            "Identity Card": [visitor["identity_card"] for visitor in data],
            "ID Card": [visitor["id_card"] for visitor in data],
            "Time enter": [visitor["time_enter"] for visitor in data],
            "Time out": [visitor["time_out"] for visitor in data],
        }
        print(tabulate(data, headers="keys"))

    def display_all_cards(self, cards):
        data = {
            "Id": [card["id"] for card in cards],
            "Type": [card["type"] for card in cards],
            "Number Card": [card["number_card"] for card in cards],
            "Status": [card["status"] for card in cards],
        }
        print(tabulate(data, headers="keys"))

    def display_specific_cards(self, cards):
        print("Search by:\n1. Card Number\n2. Type")
        while True:
            option = input("Enter your choice: ")
            if option not in ["1", "2"]:
                print("Invalid option. Please try again.")
                continue
            if option == "1":
                number_card = input(
                        "Enter card number: ")
                data = [card for card in cards if card["number_card"] == number_card]
                break
            elif option == "2":
                print("1. Visitor\n2. Tenant")
                while True:
                    type = input(
                        "Enter visitor type card: ")
                    if type not in ["1", "2"]:
                        print("Invalid option. Please try again.")
                        continue
                    if type == "1":
                        type = "Visitor"
                        break
                    elif type == "2":
                        type = "Tenant"
                        break
                data = [card for card in cards if card["type"] == type]
                break
        if len(data) == 0:
            print("Data not found")
            return
        data = {
            "Id": [card["id"] for card in data],
            "Type": [card["type"] for card in data],
            "Number Card": [card["number_card"] for card in data],
            "Status": [card["status"] for card in data],
        }
        print(tabulate(data, headers="keys"))

    def update_visitor(self, visitors, cards):
        print("Search data by:\n1. Name\n2. ID Card")
        while True:
            option = input("Enter your choice: ")
            if option not in ["1", "2"]:
                print("Invalid option. Please try again.")
                continue
            if option == "1":
                name = input("Enter visitor name: ")
                data = [visitor for visitor in visitors if visitor["name"] == name]
                break
            elif option == "2":
                id_card = input("Enter ID card number: ")
                data = [
                    visitor for visitor in visitors if visitor["id_card"] == id_card]
                break
        if len(data) == 0:
            print("Data not found")
            return
        data = {
            "Id": [visitor["id"] for visitor in data],
            "Name": [visitor["name"] for visitor in data],
            "Identity Card": [visitor["identity_card"] for visitor in data],
            "ID Card": [visitor["id_card"] for visitor in data],
            "Time enter": [visitor["time_enter"] for visitor in data],
            "Time out": [visitor["time_out"] for visitor in data],
        }
        print(tabulate(data, headers="keys"))
        while True:
            temp = False
            id = input("Select data by ID: ")
            if not id.isdigit():
                print("ID must be number.\nPlease try agian")
                continue
            for visitor in data["Id"]:
                if visitor == int(id):
                    temp = True
                    break
            else:
                print("ID not found.\nPlease try agian.")
            if temp == True:
                break
        data = next(
            (visitor for visitor in visitors if visitor['id'] == int(id)), None)
        index = visitors.index(data)

        print("Please edit data you want.\nLeave it blank for skip.")
        # name
        name = input(f"Enter visitor name ({visitors[index]['name']}): ")
        if name == "":
            pass
        else:
            visitors[index]["name"] = name
        # identity card
        print("1. KTP\n2. SIM\n3. Passport")
        while True:
            identity_card = input(
                f"Enter visitor identity card ({visitors[index]['identity_card']}): ")
            if identity_card not in ["1", "2", "3", ""]:
                print("Invalid option. Please try again.")
                continue
            if identity_card == "1":
                visitors[index]['identity_card'] = "KTP"
                break
            elif identity_card == "2":
                visitors[index]['identity_card'] = "SIM"
                break
            elif identity_card == "3":
                visitors[index]['identity_card'] = "Passport"
                break
            elif identity_card == "":
                break
        # id card
        current_id_card = next(
            (card for card in cards if card['number_card'] == visitors[index]['id_card']), None)
        while True:
            new_id_card = input(
                f"Enter visitor identity card ({visitors[index]['id_card']}): ")
            if new_id_card == "":
                break
            else:
                found = False
                for card in cards:
                    if new_id_card == card["number_card"] and card["status"] == False:
                        visitors[index]['id_card'] = new_id_card
                        current_id_card.return_card()
                        card.take_card()
                        found = True
                        break
                else:
                    print("Card has been used or not found.")
                if found == True:
                    break
        print(f"Visitor {visitors[index]['name']} successfully edited")
    
    def delete_card(self, cards, temporarys):
        print("Search by:\n1. Card Number\n2. Type")
        while True:
            option = input("Enter your choice: ")
            if option not in ["1", "2"]:
                print("Invalid option. Please try again.")
                continue
            if option == "1":
                number_card = input(
                        "Enter card number: ")
                data = [card for card in cards if card["number_card"] == number_card]
                break
            elif option == "2":
                print("1. Visitor\n2. Tenant")
                while True:
                    type = input(
                        "Enter visitor type card: ")
                    if type not in ["1", "2"]:
                        print("Invalid option. Please try again.")
                        continue
                    if type == "1":
                        type = "Visitor"
                        break
                    elif type == "2":
                        type = "Tenant"
                        break
                data = [card for card in cards if card["type"] == type]
                break
        if len(data) == 0:
            print("Data not found")
            return
        data = {
            "Id": [card["id"] for card in data],
            "Type": [card["type"] for card in data],
            "Number Card": [card["number_card"] for card in data],
            "Status": [card["status"] for card in data],
        }
        print(tabulate(data, headers="keys"))

        while True:
            temp = False
            id = input("Select data by ID: ")
            if not id.isdigit():
                print("ID must be number.\nPlease try agian")
                continue
            for card in data["Id"]:
                if card == int(id):
                    temp = True
                    break
            else:
                print("ID not found.\nPlease try agian.")
            if temp == True:
                break

        data = next(
            (card for card in cards if card['id'] == int(id)), None)
        if data["status"] == True:
            print("Data can't be deleted")
        else:
            cards.remove(data)
            if len(temporarys) == 0:
                data["id"] = 0
            else:
                for i in range(len(temporarys)):
                    if temporarys[i]["id"] != i:
                        data["id"] = i
                        break
                else:
                    data["id"] = i + 1
            temporarys.append(data)
            print("Delete successfully.")

    def restore_data(self, cards, temporarys):
        if len(temporarys) == 0:
            print("Data not found")
            return
        
        data = {
            "Id": [temporary["id"] for temporary in temporarys],
            "Type": [temporary["type"] for temporary in temporarys],
            "Number temporary": [temporary["number_card"] for temporary in temporarys],
            "Status": [temporary["status"] for temporary in temporarys],
        }
        print(tabulate(data, headers="keys"))

        while True:
            temp = False
            id = input("Select data by ID: ")
            for temporary in data["Id"]:
                if temporary == int(id):
                    temp = True
                    break
            else:
                print("ID not found.\nPlease try agian.")
            if temp == True:
                break

        data = next(
            (temporary for temporary in temporarys if temporary['id'] == int(id)), None)
        temporarys.remove(data)
        if len(cards) == 0:
            data["id"] = 0
        else:
            for i in range(len(cards)):
                if cards[i]["id"] != i:
                    data["id"] = i
                    break
            else:
                data["id"] = i + 1
        cards.append(data)
        print("Restore data successfully.")
        
            
    def delete_permanently(self, temporarys):
        if len(temporarys) == 0:
            print("Data not found")
            return
        
        data = {
            "Id": [temporary["id"] for temporary in temporarys],
            "Type": [temporary["type"] for temporary in temporarys],
            "Number temporary": [temporary["number_card"] for temporary in temporarys],
            "Status": [temporary["status"] for temporary in temporarys],
        }
        print(tabulate(data, headers="keys"))

        while True:
            temp = False
            id = input("Select data by ID: ")
            if not id.isdigit():
                print("ID must be number.\nPlease try agian")
                continue
            for temporary in data["Id"]:
                if temporary == int(id):
                    temp = True
                    break
            else:
                print("ID not found.\nPlease try agian.")
            if temp == True:
                break

        data = next(
            (temporary for temporary in temporarys if temporary['id'] == int(id)), None)
        temporarys.remove(data)
        print("Delete successfully.")

