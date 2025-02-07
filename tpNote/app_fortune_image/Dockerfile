# Utiliser l'image de base PHP avec Apache
FROM php:7.4-apache

# Mettre à jour les paquets et installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    fortune \
    imagemagick \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers nécessaires dans le répertoire racine du serveur
COPY index.php /var/www/html/
COPY images /var/www/html/images
COPY convert.sh /root/

# Rendre le script exécutable et l'exécuter
RUN chmod +x /root/convert.sh && /root/convert.sh

# Exposer le port 80
EXPOSE 80
