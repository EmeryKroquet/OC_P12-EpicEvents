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
    # Instanciez le contrôleur et la vue
    controller = CRMController()
    view = CRMView()

    # Menu principal
    while True:
        view.display_menu()
        choix = view.get_user_choice()

        if choix == "1":
            # Menu de gestion des clients
            while True:
                view.display_clients(controller.get_all_clients())
                choix_client = view.get_user_choice()

                if choix_client == "1":
                    nom_complet, email, telephone, nom_entreprise, contact_commercial = view.get_client_details()
                    controller.add_client(nom_complet, email, telephone, nom_entreprise, contact_commercial)
                elif choix_client == "2":
                    clients = controller.get_all_clients()
                    view.display_clients(clients)
                elif choix_client == "3":
                    nom_recherche = input("Nom du client à rechercher : ")
                    clients = controller.search_client_by_name(nom_recherche)
                    view.display_clients(clients)
                elif choix_client == "4":
                    client_id = view.get_client_id()
                    new_email = view.get_new_email()
                    controller.update_client_email(int(client_id), new_email)
                elif choix_client == "5":
                    client_id = view.get_client_id()
                    controller.delete_client(int(client_id))
                elif choix_client == "6":
                    break
                else:
                    view.display_message("Option invalide. Veuillez choisir une option valide.")
        elif choix == "2":
            view.display_message("Fonctionnalité non implémentée.")
        elif choix == "3":
            view.display_message("Fonctionnalité non implémentée.")
        elif choix == "4":
            view.display_message("Merci d'avoir utilisé votre CRM. Au revoir !")
            break
        else:
            view.display_message("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
