FROM python:3.9-slim-buster

WORKDIR /app

COPY r.txt /app/
RUN pip config --user set global.progress_bar off
RUN pip install --upgrade pip
RUN apt-get upgrade
RUN pip install --no-cache-dir -r r.txt

COPY . /app/

RUN cd djangoclipboard

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000" ] 