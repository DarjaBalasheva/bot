FROM python:3.11

WORKDIR /code

# Установка зависимостей для компиляции пакетов
RUN apt-get update && apt-get install -y build-essential

# Копирование Pipfile и Pipfile.lock
COPY requirements.txt ./

# Установка зависимостей с помощью pipenv
RUN pip3 install -r requirements.txt 

#
COPY . .

#
CMD python3 bot.py
