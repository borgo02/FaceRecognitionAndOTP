# Usa l'immagine base di Python per ARM (Raspberry Pi)
#arm32v7/
#FROM arm32v7/python:3.9-slim
#FROM jritsema/opencv-tensorflow-lite-arm32v7
FROM inyoursaas/opencv:arm32v7

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
#RUN apt install libx265-165 libfontconfig1 libepoxy0 libopus0 libva-drm2 libsoxr0 libgsm1 libvpx5 libgdk-pixbuf2.0-0 libzvbi0 libx264-155 libwayland-egl1 libxcomposite1 libbluray2 libcairo2 libatspi2.0-0 libxfixes3 libjbig0 libswscale5 libdrm2 libxcb-shm0 libtwolame0 libavutil56 libmp3lame0 libgfortran5 libxcb-render0 librsvg2-2 libwayland-cursor0 libssh-gcrypt-4 libvorbis0a libxcursor1 libavformat58 libatk1.0-0 libva-x11-2 libgtk-3-0 libxdamage1 libtiff5 libwavpack1 libvorbisenc2 libogg0 libwebp6 libgme0 libwebpmux3 libdatrie1 libpangocairo-1.0-0 libcodec2-0.8.1 libpango-1.0-0 libatlas3-base libopenjp2-7 libxi6 libxrandr2 libxvidcore4 libatk-bridge2.0-0 libpangoft2-1.0-0 libavcodec58 libwayland-client0 libswresample3 libopenmpt0 libpixman-1-0 libcairo-gobject2 libtheora0 libchromaprint1 libvorbisfile3 libxinerama1 libthai0 libxkbcommon0 libsnappy1v5 libva2 libshine3 libspeex1 libaom0 libcroco3 libharfbuzz0b libvdpau1 libxrender1 libgraphite2-3 libmpg123-0
# Imposta la directory di lavoro
WORKDIR /app
# Installa le dipendenze necessarie (se presenti)
COPY requirements.txt .
#RUN apt-get update && apt-get install -y cmake
RUN pip install -r requirements.txt

# Copia il file Python nella directory di lavoro
COPY provaSeriale.py .
COPY trainer3.yml .
COPY labels3.pickle .
COPY haarcascade_frontalface_alt2.xml .
COPY capture_images.py .


#sudo docker run -v /var/run/docker.sock:/var/run/docker.sock --privileged test_docker_v14
#sudo docker run -v /home/marcopetrosilli/Desktop/:/shared --privileged test_docker_v14


# Comando per eseguire lo script Python
CMD ["python", "provaSeriale.py"]