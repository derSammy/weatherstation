FROM python:3.11-bookworm

COPY luefterPWM_Rasp4.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "luefterPWM_Rasp4.py"]
