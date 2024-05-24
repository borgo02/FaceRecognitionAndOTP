# Usa l'immagine base di Python per ARM (Raspberry Pi)
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file Python nella directory di lavoro
COPY provaSeriale.py .

# Installa le dipendenze necessarie (se presenti)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Comando per eseguire lo script Python
CMD ["python", "provaSeriale.py"]