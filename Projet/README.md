# Remarques

Pour la partie concernant la base de données, on peut soit lancer une base avec Docker, soit avancer et ne pas traiter cette partie.

## Instructions pour Installer Docker et Créer une Base de Données PostgreSQL

### Installer Docker

1. **Télécharger Docker** :
   - Allez sur le site officiel de Docker : [Docker](https://www.docker.com/)
   - Téléchargez et installez Docker Desktop pour votre système d'exploitation.

2. **Vérifier l'installation** :
   - Ouvrez un terminal et tapez la commande suivante pour vérifier que Docker est bien installé :
     ```sh
     docker --version
     ```

### Créer une Base de Données PostgreSQL avec Docker

1. **Tirer l'image Docker de PostgreSQL** :
   ```sh
   docker pull postgres
   ```

2. **Lancer un conteneur PostgreSQL** :
   ```sh
   docker run --name my_postgres_db -e POSTGRES_PASSWORD=mysecretpassword -d postgres_user
   ```

3. **Se connecter au conteneur PostgreSQL** :
   - Vous pouvez vous connecter au conteneur en utilisant `psql` :
     ```sh
     docker exec -it my_postgres_db psql -U postgres
     ```
   - Créez une base de données pour votre projet :
     ```sql
     CREATE DATABASE nomDeLaBase;
     ```

Vous pouvez aussi lancer votre base de données dans l'appliation `Docker Desktop`