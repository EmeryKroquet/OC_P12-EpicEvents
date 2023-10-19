## Epicevent

<h3 align="center">
    <img alt="Logo" title="#logo" src="16903799358611_P12-02.png">
    <br>
</h3>

Epicevent est une application de gestion d'événements qui permet aux utilisateurs de créer, organiser et suivre des événements et des contrats associés. Cette application est particulièrement utile pour les entreprises de gestion d'événements, les organisateurs d'événements et les professionnels du marketing qui souhaitent rationaliser leur processus de gestion des événements.

## Fonctionnalités principales

Gestion des Clients: Ajoutez, mettez à jour et supprimez les détails des clients, y compris les informations de contact et les détails de l'entreprise.
Gestion des Contrats: Créez des contrats liés à des clients, spécifiez les détails financiers et suivez les paiements.
Gestion des Événements: Planifiez des événements, spécifiez les détails tels que la date, l'emplacement et le nombre d'invités, et ajoutez des notes pertinentes.
Suivi des Participants : Gardez une trace du nombre d'invités et des présences pour chaque événement.
Interface Utilisateur Conviviale : Une interface utilisateur intuitive et conviviale pour faciliter la navigation et l'utilisation de l'application.

## Table des matières

- [Installation](#obj)
- [Configuration](#competences)
- [Utilisation](#techs)
- [Requirements](#reqs)
- [Architecture](#architecture)
- [Configuration locale](#localconfig)

## Architecture

<h3 align="center">
    <img alt="Logo" title="#logo" src="img.png">
    <br>
</h3>


# Pour installer Epicevent sur votre système local, suivez ces étapes :

## Clonez le repository depuis GitHub :

```bash
git clone https://github.com/EmeryKroquet/OC_P12-EpicEvents.git
```

## Se placer dans le repertoire du projet:
````bash cd OC_P12-EpicEvents````

## Créez et activez votre environnement virtuel (venv) :
```bash
python -m venv venv
```

## Activer l'environnement virtuel du projet :
```bash
source venv/bin/activate  # Sur Windows, utilisez venv\Scripts\activate
```

## Désactiver l'environnement :
```bash
deactivate 
```

## Installez les dépendances nécessaires :
```bash
pip install -r requirements.txt
```

## Créez le fichier de configuration :
Créez un fichier .env à la racine du projet et ajoutez les variables d'environnement nécessaires :

## Créer une session de connexion de la base de données :
```bash
DATABASE_URL=mysql+pymysql://utilisateur:motdepasse@localhost/nom_de_la_base_de_donnees
```

## Appliquez les migrations à la base de données :
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Générer un fake data pour la base de données  avec Faker en exécutant :
```bash
python -m generate_fake_data
````
ou 
```bash
python3 generate_fake_data.py
````

## Exécutez l'application :
```bash
python -m main
````
ou
```bash
python3 main.py
````