from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Client, Contract, Event

fake = Faker()

# Créez une instance de votre moteur de base de données
database_url = 'mysql+pymysql://root:root123@localhost/epicevent'
engine = create_engine(database_url)

# Créez une session
Session = sessionmaker(bind=engine)
session = Session()

# Générer 5 clients fictifs et les insérer dans la base de données
for _ in range(5):
    new_client = Client(
        nom_complet=fake.name(),
        email=fake.email(),
        telephone=fake.phone_number()[:15],  # Limitez la longueur du numéro de téléphone à 15 caractères
        nom_entreprise=fake.company(),
        contact_commercial=fake.name()
    )
    session.add(new_client)

# Validez les modifications pour les clients
session.commit()

# Récupérez les clients générés
clients = session.query(Client).all()

# Générer 5 contrats fictifs liés à des clients existants et les insérer dans la base de données
for _ in range(5):
    client = random.choice(clients)
    new_contract = Contract(
        client_id=client.id,  # Utilisez l'ID du client existant
        contact_commercial=fake.name(),
        montant_total=random.uniform(1000, 5000),
        montant_restant_a_payer=random.uniform(500, 2000),
        statut_contrat=random.choice([0, 1])
    )
    session.add(new_contract)

# Validez les modifications pour les contrats
session.commit()

# Récupérez les contrats générés
contracts = session.query(Contract).all()

# Générer 5 événements fictifs liés à des contrats existants et les insérer dans la base de données
for _ in range(5):
    contract = random.choice(contracts)
    new_event = Event(
        contract_id=contract.identifiant_unique,  # Utilisez l'identifiant unique du contrat existant
        client_name=fake.name(),
        client_contact=fake.phone_number(),
        event_date_start=fake.date_time_this_decade(),
        event_date_end=fake.date_time_this_decade(),
        support_contact=fake.name(),
        location=fake.address(),
        attendees=random.randint(10, 100),
        notes=fake.text()
    )
    session.add(new_event)

# Validez les modifications pour les événements
session.commit()

# Récupérez les événements générés
events = session.query(Event).all()

# Affichez les clients générés
print("Clients générés:")
for client in clients:
    print(f"ID: {client.id},"
          f" Nom complet: {client.nom_complet},"
          f" Email: {client.email}")

# Affichez les contrats générés
print("\nContrats générés:")
for contract in contracts:
    print(
        f"ID: {contract.identifiant_unique},"
        f" Client ID: {contract.client_id},"
        f" Montant total: {contract.montant_total}")

# Affichez les événements générés
print("\nÉvénements générés:")
for event in events:
    print(
        f"ID: {event.event_id},"
        f" Contrat ID: {event.contract_id},"
        f" Lieu: {event.location},"
        f" Participants: {event.attendees}")

# Fermez la session
session.close()
