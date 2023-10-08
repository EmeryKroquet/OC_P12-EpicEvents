from database import session
#from sqlalchemy.orm import session
from models.model import Client, Contract, Event

class CRMController:
    def __init__(self):
        self.session = session

    def add_client(self, nom_complet, email, telephone, nom_entreprise, contact_commercial):
        new_client = Client(nom_complet=nom_complet, email=email, telephone=telephone,
                            nom_entreprise=nom_entreprise, contact_commercial=contact_commercial)
        self.session.add(new_client)  # Utilisez la session importée pour ajouter un client
        self.session.commit()  # Committez les modifications pour les enregistrer dans la base de données
        print("Client ajouté avec succès.")

    def get_all_clients(self):
        return self.session.query(Client).all()

    def search_client_by_name(self, nom):
        return (
            self.session.query(Client)
            .filter(Client.nom_complet.like(f'%{nom}%'))
            .all()
        )

    def update_client_email(self, client_id, new_email):
        if client := self.session.query(Client).filter_by(id=client_id).first():
            client.email = new_email
            self.session.commit()
            print("Email du client mis à jour avec succès.")
        else:
            print("Client non trouvé.")

    def delete_client(self, client_id):
        if client := self.session.query(Client).filter_by(id=client_id).first():
            self.session.delete(client)
            self.session.commit()
            print("Client supprimé avec succès.")
        else:
            print("Client non trouvé.")

    def add_contract(self, client_id, contact_commercial, montant_total, montant_restant, statut_contrat):
        new_contract = Contract(client_id=client_id, contact_commercial=contact_commercial,
                                montant_total=montant_total, montant_restant_a_payer=montant_restant,
                                statut_contrat=statut_contrat)
        self.session.add(new_contract)
        self.session.commit()


    def get_all_contracts(self):
        return session.query(Contract).all()

    def get_contracts_by_client(self, client_id):
        return session.query(Contract).filter_by(client_id=client_id).all()

    def update_contract_amounts(self, contract_id, new_total_amount, new_remaining_amount):
        if (
            contract := session.query(Contract)
            .filter_by(identifiant_unique=contract_id)
            .first()
        ):
            contract.montant_total = new_total_amount
            contract.montant_restant_a_payer = new_remaining_amount
            session.commit()

    def delete_contract(self, contract_id):
        if (
            contract := session.query(Contract)
            .filter_by(identifiant_unique=contract_id)
            .first()
        ):
            session.delete(contract)
            session.commit()
        else:
            print("Contrat introuvable.")

    def add_event(self, contract_id, client_name, client_contact, event_date_start, event_date_end,
                  support_contact, location, attendees, notes):
        new_event = Event(contract_id=contract_id, client_name=client_name, client_contact=client_contact,
                          event_date_start=event_date_start, event_date_end=event_date_end,
                          support_contact=support_contact, location=location, attendees=attendees, notes=notes)
        self.session.add(new_event)
        self.session.commit()

    def get_events_by_contract(self, contract_id):
        return session.query(Event).filter_by(contract_id=contract_id).all()

    def update_event_details(self, event_id, new_location, new_notes):
        if event := session.query(Event).filter_by(event_id=event_id).first():
            event.location = new_location
            event.notes = new_notes
            session.commit()

    def delete_event(self, event_id):
        if event := session.query(Event).filter_by(event_id=event_id).first():
            session.delete(event)
            session.commit()
        else:
            print("Événement introuvable.")
# Exemple d'utilisation du contrôleur
controller = CRMController()

