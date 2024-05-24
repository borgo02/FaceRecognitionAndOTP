# Usa l'immagine base di Python per ARM (Raspberry Pi)
FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*
# Imposta la directory di lavoro
WORKDIR /app

# Copia il file Python nella directory di lavoro
COPY provaSeriale.py .

# Installa le dipendenze necessarie (se presenti)
COPY requirements.txt .
RUN apt-get update && apt-get install -y cmake
RUN pip install --no-cache-dir -r requirements.txt

# Comando per eseguire lo script Python
CMD ["python", "provaSeriale.py"]