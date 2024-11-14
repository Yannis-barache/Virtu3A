# Utiliser l'image de base Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers locaux dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exécuter l'application
CMD ["python", "app.py"]