# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
#COPY requirements.txt requirements.txt
#RUN apt update 
RUN pip install -r requirements.txt && \
    pip install setuptools && \
    pip install --editable .
#COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]