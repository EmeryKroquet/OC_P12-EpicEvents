from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser

# Créez un objet ConfigParser
config = configparser.ConfigParser()

# Lisez le fichier de configuration
config.read('config.cfg')

# Récupérez les informations de connexion à la base de données
database_user = config['database']['user']
database_password = config['database']['password']
database_host = config['database']['host']
database_name = config['database']['database_name']

# Construisez l'URL de la base de données avec les nouvelles informations
database_url = f'mysql+pymysql://{database_user}:{database_password}@{database_host}/{database_name}'

# Créez une instance de moteur de base de données en utilisant la nouvelle URL
engine = create_engine(database_url)

# Créez une session
Session = sessionmaker(bind=engine)
session = Session()
