from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de connexion à la base de données MySQL
database_url = 'mysql+pymysql://root:root123@localhost/epicevent'

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

#ALTER TABLE client MODIFY COLUMN last_update DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;
