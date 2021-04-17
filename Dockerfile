FROM python:3.8-slim

RUN mkdir ~/Desktop/
RUN mkdir ~/Desktop/app/
WORKDIR ~/Desktop/app/

RUN apt-get update
RUN apt-get upgrade -y
RUN pip install fastapi[all]

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "main.py"]