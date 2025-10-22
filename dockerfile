# Usa un'immagine Python ufficiale
FROM python:3.12.10

# Imposta la directory di lavoro
WORKDIR /app

# Copia tutto il codice nel container
COPY . /app

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Imposta il comando di esecuzione
CMD ["python", "app.py"]
