FROM python:3

COPY . /commitapp/

WORKDIR /commitapp

RUN pip3 install -r reqs.txt

ENTRYPOINT ["gunicorn","-b", "0.0.0.0:5000", "-w", "3", "app:app"]