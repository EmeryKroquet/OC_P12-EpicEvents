# Point d'entrée principal de l'application
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from controllers.controller import CRMController
from views.view import CRMView

database_url = 'mysql+pymysql://root:Macpro-emery@@localhost/epicevent'

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()


def main():
    # Instanciez le contrôleur
    controller = CRMController()

    while True:
        print("1. Gérer les clients")
        print("2. Gérer les contrats")
        print("3. Gérer les événements")
        print("4. Quitter")

        choix = input("Veuillez entrer le numéro de l'option que vous souhaitez choisir : ")

        if choix == "1":
            # Menu de gestion des clients
            while True:
                print("1. Ajouter un client")
                print("2. Afficher tous les clients")
                print("3. Mettre à jour l'email d'un client")
                print("4. Supprimer un client")
                print("5. Retour")

                choix_client = input("Veuillez entrer le numéro de l'option que vous souhaitez choisir : ")

                if choix_client == "1":
                    nom_complet = input("Nom complet du client : ")
                    email = input("Email du client : ")
                    telephone = input("Téléphone du client : ")
                    nom_entreprise = input("Nom de l'entreprise : ")
                    contact_commercial = input("Nom du contact commercial : ")
                    controller.add_client(nom_complet, email, telephone, nom_entreprise, contact_commercial)
                elif choix_client == "2":
                    clients = controller.get_all_clients()
                    for client in clients:
                        print(f"ID: {client.id}, Nom: {client.nom_complet}, Email: {client.email}")
                elif choix_client == "3":
                    client_id = int(input("ID du client : "))
                    new_email = input("Nouvel email : ")
                    controller.update_client_email(client_id, new_email)
                elif choix_client == "4":
                    client_id = int(input("ID du client : "))
                    controller.delete_client(client_id)
                elif choix_client == "5":
                    break
                else:
                    print("Option invalide. Veuillez choisir une option valide.")
        elif choix == "2":
            # Menu de gestion des contrats
            while True:
                print("1. Ajouter un contrat")
                print("2. Afficher tous les contrats")
                print("3. Retour")

                choix_contrat = input("Veuillez entrer le numéro de l'option que vous souhaitez choisir : ")

                if choix_contrat == "1":
                    client_id = int(input("ID du client associé au contrat : "))
                    contact_commercial = input("Nom du contact commercial : ")
                    montant_total = float(input("Montant total du contrat : "))
                    montant_restant = float(input("Montant restant à payer : "))
                    statut_contrat = int(input("Statut du contrat (1 pour actif, 0 pour inactif) : "))
                    controller.add_contract(client_id, contact_commercial, montant_total, montant_restant,
                                            statut_contrat)
                elif choix_contrat == "2":
                    contracts = controller.get_all_contracts()
                    for contract in contracts:
                        print(
                            f"ID: {contract.identifiant_unique},"
                            f" Client ID: {contract.client_id},"
                            f" Montant Total: {contract.montant_total},"
                            f" Statut: {contract.statut_contrat}")
                elif choix_contrat == "3":
                    break
                else:
                    print("Option invalide. Veuillez choisir une option valide.")
        elif choix == "3":
            # Menu de gestion des événements
            while True:
                print("1. Ajouter un événement")
                print("2. Afficher les événements d'un contrat")
                print("3. Retour")

                choix_evenement = input("Veuillez entrer le numéro de l'option que vous souhaitez choisir : ")

                if choix_evenement == "1":
                    contract_id = int(input("ID du contrat associé à l'événement : "))
                    client_name = input("Nom du client : ")
                    client_contact = input("Contact du client : ")
                    event_date_start = input("Date de début de l'événement (YYYY-MM-DD HH:MM:SS) : ")
                    event_date_end = input("Date de fin de l'événement (YYYY-MM-DD HH:MM:SS) : ")
                    support_contact = input("Nom du contact de support : ")
                    location = input("Lieu de l'événement : ")
                    attendees = int(input("Nombre de participants : "))
                    notes = input("Notes sur l'événement : ")
                    controller.add_event(contract_id, client_name, client_contact, event_date_start, event_date_end,
                                         support_contact, location, attendees, notes)
                elif choix_evenement == "2":
                    contract_id = int(input("ID du contrat : "))
                    events = controller.get_events_by_contract(contract_id)
                    for event in events:
                        print(
                            f"ID: {event.event_id},"
                            f" Client: {event.client_name},"
                            f" Début: {event.event_date_start},"
                            f" Fin: {event.event_date_end},"
                            f" Lieu: {event.location}")
                elif choix_evenement == "3":
                    break
                else:
                    print("Option invalide. Veuillez choisir une option valide.")
        elif choix == "4":
            print("Merci d'avoir utilisé votre CRM. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    main()