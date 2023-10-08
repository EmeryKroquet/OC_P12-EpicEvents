from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    nom_complet = Column(String(100), nullable=False)
    email = Column(String(254), nullable=False, unique=True)
    telephone = Column(String(15), nullable=False)
    nom_entreprise = Column(String(100), nullable=False)
    date_creation = Column(DateTime, default=func.now(), nullable=False)
    last_update = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    contact_commercial = Column(String(100), nullable=False)

    contracts = relationship('Contract', back_populates='client')
    events = relationship('Event', back_populates='client')

    def __str__(self):
        return (f"ID: {self.id},"
                f" Nom complet: {self.nom_complet},"
                f" Email: {self.email}")

    def __repr__(self):
        return (f"Client(id={self.id},"
                f" nom_complet='{self.nom_complet}'"
                f", email='{self.email}')")


class Contract(Base):
    __tablename__ = 'contract'

    identifiant_unique = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    contact_commercial = Column(String(100), nullable=False)
    montant_total = Column(Float(precision=2), nullable=False)
    montant_restant_a_payer = Column(Float(precision=2), nullable=False)
    date_creation_contrat = Column(DateTime, default=func.now(), nullable=False)
    statut_contrat = Column(Integer, nullable=False)

    client = relationship('Client', back_populates='contracts')
    events = relationship('Event', back_populates='contract')

    def __str__(self):
        return (f"Contrat {self.identifiant_unique}"
                f" - Client: {self.client_id},"
                f" Montant total: {self.montant_total},"
                f" Statut: {'Actif' if self.statut_contrat else 'Inactif'}")

    def __repr__(self):
        return (f"Contract(identifiant_unique={self.identifiant_unique},"
                f" client_id={self.client_id},"
                f" contact_commercial='{self.contact_commercial}',"
                f" montant_total={self.montant_total},"
                f" montant_restant_a_payer={self.montant_restant_a_payer},"
                f" date_creation_contrat='{self.date_creation_contrat}',"
                f" statut_contrat={self.statut_contrat})")


class Event(Base):
    __tablename__ = 'event'

    event_id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey('contract.identifiant_unique'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)  # Référence à la colonne client_id
    client_name = Column(String(100), nullable=False)
    client_contact = Column(String(100), nullable=False)
    event_date_start = Column(DateTime, nullable=False)
    event_date_end = Column(DateTime, nullable=False)
    support_contact = Column(String(100), nullable=False)
    location = Column(String(255))
    attendees = Column(Integer, nullable=False)
    notes = Column(String(1000))

    client = relationship('Client', back_populates='events')
    contract = relationship('Contract', back_populates='events')

    def __str__(self):
        return (f"Événement {self.event_id}"
                f" - Contrat: {self.contract_id},"
                f" Client: {self.client_id},"  # Ajoutez cette ligne pour afficher le client_id
                f" Date de début: {self.event_date_start},"
                f" Date de fin: {self.event_date_end},"
                f" Lieu: {self.location},"
                f" Participants: {self.attendees}")

    def __repr__(self):
        return (f"Event(event_id={self.event_id},"
                f" contract_id={self.contract_id},"
                f" client_id={self.client_id},"  # Ajoutez cette ligne pour afficher le client_id
                f" client_name='{self.client_name}',"
                f" client_contact='{self.client_contact}',"
                f" event_date_start='{self.event_date_start}',"
                f" event_date_end='{self.event_date_end}',"
                f" support_contact='{self.support_contact}',"
                f" location='{self.location}',"
                f" attendees={self.attendees},"
                f" notes='{self.notes}')")



class CustomGroup(Base):
    __tablename__ = 'custom_group'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)

class CustomUser(Base):
    __tablename__ = 'custom_user'

    id = Column(Integer, primary_key=True)
    username = Column(String(150), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    is_staff = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)
    date_joined = Column(DateTime, default=func.now(), nullable=False)
    department = Column(String(20))
    last_login = Column(DateTime)

    def __str__(self):
        return (f"CustomUser(id={self.id}, username='{self.username}',"
                f" first_name='{self.first_name}', last_name='{self.last_name}',"
                f" email='{self.email}', is_staff={self.is_staff},"
                f" is_active={self.is_active}, date_joined='{self.date_joined}',"
                f" department='{self.department}')")

    def __repr__(self):
        return (f"CustomUser(id={self.id},"
                f" username='{self.username}',"
                f" email='{self.email}',"
                f" first_name='{self.first_name}',"
                f" last_name='{self.last_name}',"
                f" department='{self.department}')")