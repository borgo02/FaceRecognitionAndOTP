# Usa l'immagine base di Python per ARM (Raspberry Pi)
#gleissonbezerra/arm32v7-opencv-python:3.7-bullseye
#FROM arm32v7/python:3.9-slim
#FROM inyoursaas/opencv:arm32v7-20190219
#FROM elswork/tf-opencv:armv7l
FROM inyoursaas/opencv:arm32v7
#FROM jritsema/opencv-tensorflow-lite-arm32v7
RUN echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7 \
    libtiff5 \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    python3-tk \
    ghostscript \
    libharfbuzz-dev \
    libfribidi-dev \
    libxcb1-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fswebcam
#Imposta la directory di lavoro
WORKDIR /app

# Copia il file Python nella directory di lavoro
COPY capture_images.py .
# Installa le dipendenze necessarie (se presenti)
COPY requirements.txt .
#RUN apt-get update && apt-get install -y cmake
RUN pip install -r requirements.txt
# Comando per eseguire lo script Python
CMD ["python", "capture_images.py"]