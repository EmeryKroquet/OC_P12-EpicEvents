from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Assurez-vous d'importer correctement les modèles depuis le module models
from models.model import Client, Contract, Event, CustomUser, CustomGroup

fake = Faker()

# Créez une instance de votre moteur de base de données
database_url = 'mysql+pymysql://root:root123@localhost/epicevent'
engine = create_engine(database_url)

# Créez une session
Session = sessionmaker(bind=engine)
session = Session()

# Générer 10 clients fictifs et les insérer dans la base de données
clients = []
for _ in range(5):
    new_client = Client(
        nom_complet=fake.name(),
        email=fake.email(),
        telephone=fake.phone_number()[:15],
        nom_entreprise=fake.company(),
        contact_commercial=fake.name()
    )
    session.add(new_client)
    clients.append(new_client)

# Validez les modifications pour les clients
session.commit()

# Générer 10 contrats fictifs liés à des clients existants et les insérer dans la base de données
contracts = []
for _ in range(5):
    client = random.choice(clients)
    new_contract = Contract(
        client_id=client.id,
        contact_commercial=fake.name(),
        montant_total=random.uniform(1000, 5000),
        montant_restant_a_payer=random.uniform(500, 2000),
        statut_contrat=random.choice([0, 1])
    )
    session.add(new_contract)
    contracts.append(new_contract)

# Validez les modifications pour les contrats
session.commit()

# Générer 10 événements fictifs liés à des contrats et clients existants
events = []
for _ in range(5):
    contract = random.choice(contracts)
    client = random.choice(clients)
    event = Event(
        contract_id=contract.identifiant_unique,
        client_id=client.id,
        client_name=client.nom_complet,
        client_contact=fake.phone_number(),
        event_date_start=fake.date_time_this_decade(),
        event_date_end=fake.date_time_this_decade(),
        support_contact=fake.name(),
        location=fake.address(),
        attendees=random.randint(10, 100),
        notes=fake.text()
    )
    session.add(event)
    events.append(event)

# Validez les modifications pour les événements
session.commit()

# Générer des données pour CustomUserController
custom_users = []
for _ in range(5):
    new_user = CustomUser(
        username=fake.user_name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=fake.password(),
        is_staff=random.choice([True, False]),
        is_active=random.choice([True, False]),
        department=fake.job()
    )
    session.add(new_user)
    custom_users.append(new_user)

# Validez les modifications pour les utilisateurs personnalisés
session.commit()

# Générer des données pour CustomGroupController
custom_groups = []
for _ in range(5):
    new_group = CustomGroup(
        name=fake.word()
    )
    session.add(new_group)
    custom_groups.append(new_group)

# Validez les modifications pour les groupes personnalisés
session.commit()

# Affichez les clients générés
print("Clients générés:")
for client in clients:
    print(
        f"ID: {client.id}, Nom complet: {client.nom_complet}, Email: {client.email}")

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

# Affichez les utilisateurs personnalisés générés
print("\nUtilisateurs personnalisés générés:")
for user in custom_users:
    print(f"ID: {user.id}, Nom d'utilisateur: {user.username}, Email: {user.email}")

# Affichez les groupes personnalisés générés
print("\nGroupes personnalisés générés:")
for group in custom_groups:
    print(f"ID: {group.id}, Nom du groupe: {group.name}")

# Fermez la session
session.close()
