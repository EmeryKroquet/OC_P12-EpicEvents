from faker import Faker
import random

fake = Faker()


def generate_fake_clients(count=5):
    clients = []
    for _ in range(count):
        client = {
            "nom_complet": fake.name(),
            "email": fake.email(),
            "telephone": fake.phone_number(),
            "nom_entreprise": fake.company(),
            "contact_commercial": fake.name()
        }
        clients.append(client)
    return clients


def generate_fake_contracts(clients, count=5):
    contracts = []
    for _ in range(count):
        client_id = random.randint(1, len(clients))  # ID du client existant
        contract = {
            "identifiant_unique": random.randint(1, 1000),  # ID unique du contrat
            "client_id": client_id,
            "contact_commercial": fake.name(),
            "montant_total": random.uniform(1000, 5000),
            "montant_restant_a_payer": random.uniform(500, 2000),
            "statut_contrat": random.choice([0, 1])  # 0 pour inactif, 1 pour actif
        }
        contracts.append(contract)
    return contracts




def generate_fake_events(contracts, count=5):
    events = []
    for i in range(count):
        event = {
            "contract_id": random.choice(contracts)["identifiant_unique"],  # ID du contrat existant
            "client_name": fake.name(),
            "client_contact": fake.phone_number(),
            "event_date_start": fake.date_time_this_decade(),
            "event_date_end": fake.date_time_this_decade(),
            "support_contact": fake.name(),
            "location": fake.address(),
            "attendees": random.randint(10, 100),
            "notes": fake.text()
        }
        events.append(event)
    return events


if __name__ == "__main__":
    clients = generate_fake_clients()
    contracts = generate_fake_contracts(clients)
    events = generate_fake_events(contracts)

    # Vous pouvez maintenant utiliser les listes clients, contracts et events comme vous le souhaitez.
