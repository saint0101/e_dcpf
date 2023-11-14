# Utiliser l'image officielle Apache avec PHP
FROM php:7.4-apache

# Installer git pour pouvoir cloner le dépôt GitHub
RUN apt-get update && apt-get install -y git

# Cloner le dépôt GitHub contenant le site de test
RUN git clone -b testprod https://github.com/saint0101/e_dcpf.git

RUN ls .

WORKDIR /e_dcpf/frontend

RUN ls .

COPY . /var/www/html

# Définir les permissions pour le répertoire
RUN chown -R www-data:www-data /var/www/html

WORKDIR /etc/apache2/sites-available

RUN ls .

RUN a2ensite 000-default.conf

# WORKDIR /var/www/html

# RUN touch .htaccess && echo "Options +Indexes" >> .htaccess

# Optionnel : Exposer le port 80
EXPOSE 80

# Start Apache when the container launches
CMD ["apache2-foreground"]