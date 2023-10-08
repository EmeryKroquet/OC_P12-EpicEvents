class CRMView:
    @staticmethod
    def display_menu():
        print("Bienvenue dans votre CRM !")
        print("1. Ajouter un client")
        print("2. Afficher tous les clients")
        print("3. Rechercher un client par nom")
        print("4. Mettre à jour l'email d'un client")
        print("5. Supprimer un client")
        print("6. Quitter")

    @staticmethod
    def get_user_choice():
        return input("Veuillez entrer le numéro de l'option que vous souhaitez choisir : ")

    @staticmethod
    def get_client_details():
        nom_complet = input("Nom complet du client : ")
        email = input("Email du client : ")
        telephone = input("Téléphone du client : ")
        nom_entreprise = input("Nom de l'entreprise : ")
        contact_commercial = input("Nom du contact commercial : ")
        return nom_complet, email, telephone, nom_entreprise, contact_commercial

    @staticmethod
    def display_clients(clients):
        # Utilisez la liste des clients passée en argument pour l'affichage
        for client in clients:
            print(f"ID: {client.id}, Nom: {client.nom_complet}, Email: {client.email}")

    @staticmethod
    def get_client_id():
        return input("ID du client : ")

    @staticmethod
    def get_new_email():
        return input("Nouvel email : ")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_contracts(contracts):
        for contract in contracts:
            print(
                f"ID Contrat: {contract.identifiant_unique},"
                f" ID Client: {contract.client_id},"
                f" Montant Total: {contract.montant_total}")

    @staticmethod
    def display_custom_groups(groups):
        for group in groups:
            print(f"ID Groupe: {group.id},"
                  f" Nom: {group.name}")

    @staticmethod
    def display_custom_users(users):
        for user in users:
            print(f"ID Utilisateur: {user.id},"
                  f" Nom d'utilisateur: {user.username},"
                  f" Email: {user.email}")

    @staticmethod
    def display_events(events):
        for event in events:
            print(
                f"ID Événement: {event.event_id},"
                f" ID Contrat: {event.contract_id},"
                f" Nom Client: {event.client_name},"
                f" Date Début: {event.event_date_start}")
