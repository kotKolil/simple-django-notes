FROM python:latest
WORKDIR /app

COPY r.txt ./

# creating virtual env for python
# RUN python3 -m venv venv
# RUN cd venv
# RUN cd Scripts
# RUN .\activate

RUN pip install --upgrade pip & pip install -r r.txt --user

COPY . .
EXPOSE 8000
CMD "cd djangoclipboard"

RUN ["python" "manage.py" "runserver" "0.0.0.0:8000"]
