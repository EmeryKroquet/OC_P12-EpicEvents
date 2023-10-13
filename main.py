from controllers.controller import CRMController, CustomGroupController, CustomUserController

def main():
    # Instanciez les contrôleurs
    crm_controller = CRMController()
    custom_group_controller = CustomGroupController()
    custom_user_controller = CustomUserController()

    while True:
        print("\n================================================")
        print("Bienvenue dans notre application CRM")
        print("\n================================================")
        print("1. Gérer les clients")
        print("2. Gérer les contrats")
        print("3. Gérer les événements")
        print("4. Gérer les groupes personnalisés")
        print("5. Gérer les utilisateurs personnalisés")
        print("6. Quitter")

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
                    crm_controller.add_client(nom_complet, email, telephone, nom_entreprise, contact_commercial)
                elif choix_client == "2":
                    clients = crm_controller.get_all_clients()
                    for client in clients:
                        print(f"ID: {client.id}, Nom: {client.nom_complet}, Email: {client.email}")
                elif choix_client == "3":
                    client_id = int(input("ID du client : "))
                    new_email = input("Nouvel email : ")
                    crm_controller.update_client_email(client_id, new_email)
                elif choix_client == "4":
                    client_id = int(input("ID du client : "))
                    crm_controller.delete_client(client_id)
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
                    crm_controller.add_contract(client_id, contact_commercial, montant_total, montant_restant, statut_contrat)
                elif choix_contrat == "2":
                    contracts = crm_controller.get_all_contracts()
                    for contract in contracts:
                        print(f"ID: {contract.identifiant_unique}, Client ID: {contract.client_id}, Montant Total: {contract.montant_total}, Statut: {contract.statut_contrat}")
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
                    crm_controller.add_event(contract_id, client_name, client_contact, event_date_start, event_date_end, support_contact, location, attendees, notes)
                elif choix_evenement == "2":
                    contract_id = int(input("ID du contrat : "))
                    events = crm_controller.get_events_by_contract(contract_id)
                    for event in events:
                        print(f"ID: {event.event_id}, Client: {event.client_name}, Début: {event.event_date_start}, Fin: {event.event_date_end}, Lieu: {event.location}")
                elif choix_evenement == "3":
                    break
                else:
                    print("Option invalide. Veuillez choisir une option valide.")

        elif choix == "4":
            # Menu de gestion des groupes personnalisés
            while True:
                print("1. Ajouter un groupe personnalisé")
                print("2. Afficher tous les groupes personnalisés")
                print("3. Supprimer un groupe personnalisé")
                print("4. Retour")

                choix_groupe = input("Veuillez entrer le numéro de l'option que vous souhaitez choisir : ")

                if choix_groupe == "1":
                    nom_groupe = input("Nom du groupe personnalisé : ")
                    custom_group_controller.add_custom_group(nom_groupe)
                elif choix_groupe == "2":
                    groupes = custom_group_controller.get_all_custom_groups()
                    for groupe in groupes:
                        print(f"ID: {groupe.id}, Nom: {groupe.name}")
                elif choix_groupe == "3":
                    groupe_id = int(input("ID du groupe personnalisé : "))
                    custom_group_controller.delete_custom_group(groupe_id)
                elif choix_groupe == "4":
                    break
                else:
                    print("Option invalide. Veuillez choisir une option valide.")

        elif choix == "5":
            # Menu de gestion des utilisateurs personnalisés
            while True:
                print("1. Ajouter un utilisateur personnalisé")
                print("2. Afficher tous les utilisateurs personnalisés")
                print("3. Supprimer un utilisateur personnalisé")
                print("4. Retour")

                choix_utilisateur = input("Veuillez entrer le numéro de l'option que vous souhaitez choisir : ")

                if choix_utilisateur == "1":
                    username = input("Nom d'utilisateur : ")
                    first_name = input("Prénom : ")
                    last_name = input("Nom : ")
                    email = input("Adresse e-mail : ")
                    password = input("Mot de passe : ")
                    is_staff = int(input("Est un membre du personnel (1 pour vrai, 0 pour faux) : "))
                    is_active = int(input("Est actif (1 pour vrai, 0 pour faux) : "))
                    department = input("Département : ")
                    custom_user_controller.add_custom_user(username, first_name, last_name, email, password,
                                                           is_staff, is_active, department)
                elif choix_utilisateur == "2":
                    utilisateurs = custom_user_controller.get_all_custom_users()
                    for utilisateur in utilisateurs:
                        print(
                            f"ID: {utilisateur.id}, Nom d'utilisateur: {utilisateur.username}, Email: {utilisateur.email}")
                elif choix_utilisateur == "3":
                    utilisateur_id = int(input("ID de l'utilisateur personnalisé : "))
                    custom_user_controller.delete_custom_user(utilisateur_id)
                elif choix_utilisateur == "4":
                    break
                else:
                    print("Option invalide. Veuillez choisir une option valide.")
if __name__ == "__main__":
    main()
