# Utiliser l'image officielle Apache avec PHP
FROM php:7.4-apache

# Installer git pour pouvoir cloner le dépôt GitHub
RUN apt-get update && apt-get install -y git

# Cloner le dépôt GitHub contenant le site de test
RUN git clone https://github.com/saint0101/e_dcpf.git
COPY ./e_dcpf/frontend/ /var/www/html

# Optionnel : Exposer le port 80
EXPOSE 80