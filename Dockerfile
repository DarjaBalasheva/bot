FROM python:3.11

WORKDIR /code

# Установка зависимостей для компиляции пакетов
RUN apt-get update && apt-get install -y build-essential

#Установка pipenv
RUN pip install pipenv

# Копирование Pipfile и Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Установка зависимостей с помощью pipenv
RUN pipenv install --system --deploy

#
COPY . .

#
CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
