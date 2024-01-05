FROM python:3.11.7-slim-bookworm

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "luefterPWM_Rasp4.py"]