from database import engine, session
from sqlalchemy.orm import sessionmaker
from models.model import Client, Contract, Event, CustomGroup, CustomUser

class CRMController:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def add_client(self, nom_complet, email, telephone, nom_entreprise, contact_commercial):
        session = self.Session()
        new_client = Client(
            nom_complet=nom_complet,
            email=email,
            telephone=telephone,
            nom_entreprise=nom_entreprise,
            contact_commercial=contact_commercial
        )
        session.add(new_client)
        session.commit()
        session.close()
        print("Client ajouté avec succès.")

    def get_all_clients(self):
        session = self.Session()
        clients = session.query(Client).all()
        session.close()
        return clients

    def search_client_by_name(self, nom):
        session = self.Session()
        clients = session.query(Client).filter(Client.nom_complet.like(f'%{nom}%')).all()
        session.close()
        return clients

    # Autres méthodes du contrôleur

    def update_client_email(self, client_id, new_email):
        session = self.Session()
        client = session.query(Client).filter_by(id=client_id).first()
        if client:
            client.email = new_email
            session.commit()
            session.close()
            print("Email du client mis à jour avec succès.")
        else:
            session.close()
            print("Client non trouvé.")

    def delete_client(self, client_id):
        session = self.Session()
        client = session.query(Client).filter_by(id=client_id).first()
        if client:
            session.delete(client)
            session.commit()
            session.close()
            print("Client supprimé avec succès.")
        else:
            session.close()
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

    # ...

class CustomUserController:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def add_custom_user(self, username, first_name, last_name, email, password, is_staff, is_active, department):
        session = self.Session()
        try:
            new_user = CustomUser(username=username, first_name=first_name, last_name=last_name, email=email,
                                  password=password, is_staff=is_staff, is_active=is_active, department=department)
            session.add(new_user)
            session.commit()
            print("Utilisateur personnalisé ajouté avec succès.")
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de l'ajout de l'utilisateur personnalisé : {str(e)}")
        finally:
            session.close()

    def get_all_custom_users(self):
        session = self.Session()
        users = session.query(CustomUser).all()
        session.close()
        return users

    def get_custom_user_by_id(self, user_id):
        session = self.Session()
        user = session.query(CustomUser).filter_by(id=user_id).first()
        session.close()
        return user

    def update_custom_user(self, user_id, username, first_name, last_name, email, password, is_staff, is_active, department):
        session = self.Session()
        try:
            user = session.query(CustomUser).filter_by(id=user_id).first()
            if user:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.password = password
                user.is_staff = is_staff
                user.is_active = is_active
                user.department = department
                session.commit()
                print("Utilisateur personnalisé mis à jour avec succès.")
            else:
                print("Utilisateur personnalisé non trouvé.")
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de la mise à jour de l'utilisateur personnalisé : {str(e)}")
        finally:
            session.close()

    def delete_custom_user(self, user_id):
        session = self.Session()
        try:
            user = session.query(CustomUser).filter_by(id=user_id).first()
            if user:
                session.delete(user)
                session.commit()
                print("Utilisateur personnalisé supprimé avec succès.")
            else:
                print("Utilisateur personnalisé non trouvé.")
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de la suppression de l'utilisateur personnalisé : {str(e)}")
        finally:
            session.close()

class CustomGroupController:

    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def add_custom_group(self, name):
        session = self.Session()
        try:
            new_group = CustomGroup(name=name)
            session.add(new_group)
            session.commit()
            print("Groupe personnalisé ajouté avec succès.")
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de l'ajout du groupe personnalisé : {str(e)}")
        finally:
            session.close()

    def get_all_custom_groups(self):
        session = self.Session()
        groups = session.query(CustomGroup).all()
        session.close()
        return groups

    def get_custom_group_by_id(self, group_id):
        session = self.Session()
        group = session.query(CustomGroup).filter_by(id=group_id).first()
        session.close()
        return group

    def update_custom_group(self, group_id, name):
        session = self.Session()
        try:
            group = session.query(CustomGroup).filter_by(id=group_id).first()
            if group:
                group.name = name
                session.commit()
                print("Groupe personnalisé mis à jour avec succès.")
            else:
                print("Groupe personnalisé non trouvé.")
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de la mise à jour du groupe personnalisé : {str(e)}")
        finally:
            session.close()

    def delete_custom_group(self, group_id):
        session = self.Session()
        try:
            group = session.query(CustomGroup).filter_by(id=group_id).first()
            if group:
                session.delete(group)
                session.commit()
                print("Groupe personnalisé supprimé avec succès.")
            else:
                print("Groupe personnalisé non trouvé.")
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de la suppression du groupe personnalisé : {str(e)}")
        finally:
            session.close()

