# Usa l'immagine base di Python per ARM (Raspberry Pi)
#arm32v7/
FROM arm32v7/python:3.9-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*
# Imposta la directory di lavoro
WORKDIR /app

# Copia il file Python nella directory di lavoro
COPY provaSeriale.py .
COPY trainer.yml .
COPY labels.pickle .
COPY haarcascade_frontalface_alt2.xml .


# Installa le dipendenze necessarie (se presenti)
COPY requirements.txt .
RUN apt-get update && apt-get install -y cmake
RUN pip install -r requirements.txt

# Comando per eseguire lo script Python
CMD ["python", "provaSeriale.py"]