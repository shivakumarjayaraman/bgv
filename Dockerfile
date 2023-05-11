FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
COPY server.py server.py
COPY Fraud.xlsx Fraud.xlsx
RUN pip3 install -r requirements.txt

CMD [ "python3", "server.py", "--host-0.0.0.0"]
