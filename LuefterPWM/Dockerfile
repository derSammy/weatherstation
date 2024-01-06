FROM python:3.11-alpine

COPY luefterPWM_Rasp4.py requirements.txt ./

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

CMD ["python", "luefterPWM_Rasp4.py"]
