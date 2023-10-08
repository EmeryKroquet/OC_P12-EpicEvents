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
            nom_complet, email, telephone, nom_entreprise, contact_commercial = view.get_client_details()
            controller.add_client(nom_complet, email, telephone, nom_entreprise, contact_commercial)
        elif choix == "2":
            contracts = controller.get_all_contracts()
            view.display_contracts(contracts)
        elif choix == "3":
            custom_groups = controller.get_all_custom_groups()
            view.display_custom_groups(custom_groups)
        elif choix == "4":
            custom_users = controller.get_all_custom_users()
            view.display_custom_users(custom_users)
        elif choix == "5":
            events = controller.get_all_events()
            view.display_events(events)
        elif choix == "6":
            view.display_message("Merci d'avoir utilisé votre CRM. Au revoir !")
            break
        else:
            view.display_message("Option invalide. Veuillez choisir une option valide.")
"""

        elif choix == "2":
            view.display_message("Fonctionnalité non implémentée.")
        elif choix == "3":
            view.display_message("Fonctionnalité non implémentée.")
        elif choix == "4":
            view.display_message("Merci d'avoir utilisé votre CRM. Au revoir !")
            break
        else:
            view.display_message("Option invalide. Veuillez choisir une option valide.") """

if __name__ == "__main__":
    main()
