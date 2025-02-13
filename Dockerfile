FROM python:3.9

WORKDIR /app

COPY r.txt /app/
RUN pip config --user set global.progress_bar off
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r r.txt

COPY . /app/
EXPOSE 8000 8080 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
