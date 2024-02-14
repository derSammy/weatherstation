FROM python:3.11-bookworm

COPY pirsensor.py requirements.txt ./

#RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
#    && apk add --no-cache \
#    xorg-server-utils \
#    mesa-dri-swrast \
#    mesa-gl \
#    libglu \
#    libxi \
#    libxrandr \
#    libxrender \
#    libxfixes \
#    libxcursor \
#    libxinerama \
#    libxxf86vm \
#    libdrm \
#    libxdamage \
#    libxtst \
#    libxcb \
#    libxau \
#    libxdmcp \
#    libbsd \
#    libxdmcp \
#    libxcomposite \
#    libxslt \
#    libxml2 \
#    libxml2-utils \
#    && pip install --no-cache-dir -r requirements.txt \
#    && apk del .build-deps

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "pirsensor.py"]
