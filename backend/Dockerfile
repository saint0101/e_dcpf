FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN git clone -b master https://github.com/saint0101/e_dcpf.git
COPY . /app
WORKDIR /app/e_dcpf/backend
# Afficher le contenu du répertoire
RUN ls .
RUN pip install -r requirements.txt
# Nettoyer les fichiers inutiles
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /app/e_dcpf/backend/app
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]