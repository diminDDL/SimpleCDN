FROM python:3.11-bullseye

WORKDIR /app/

COPY ./requirements.txt /tmp/requirements.txt

WORKDIR /tmp/

RUN apt-get update && apt-get upgrade -y

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

WORKDIR /app/

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "--chdir", "./simplecdn", "simplecdn:app"]
