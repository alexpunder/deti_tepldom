## Описание проекта.

_**АНО "Теплый дом"**_ - разработка для автономно некоммерческой организации социального обслуживания населения "Теплый дом" нового сайта на Django 5.0 вместо старого на Joomla! 3.6. Детально настроена админ-панель сайта для самостоятельного, простого для администратора добавления/редактирования/удаления различной информации и контента на страницах. Пользователь может написать обращение к организации через форму: информация сохраняется в БД, а так же обрабатывается и отправляется в качестве публикации через Telegram-бота в закрытый канал администраторов. Для проектов и новостей сделаны отдельны страницы с удобной навигацией; новости можно отфильтровать по тегу или категории.

Сайт развернут на сервере в Docker Compose с использованием проксирования через Nginx, установленного на сервере. Получены бесплатные сертификаты Let's Encrypt.

## Используемые технологии.

![Python 3.12](https://img.shields.io/badge/Python-3.12-brightgreen.svg?style=flat&logo=python&logoColor=white)
![Python-telegram-bot 21.4](https://img.shields.io/badge/python--telegram--bot-21.1.1-brightgreen.svg?style=flat&logo=python&logoColor=white)
![Django 5.0.7](https://img.shields.io/badge/Django-5.0.4-brightgreen.svg?style=flat&logo=django&logoColor=white)
![Django-filter 24.2](https://img.shields.io/badge/Django--filter-24.2-brightgreen.svg?style=flat&logo=django&logoColor=white)
![Django-phonenumber-field 8.0.0](https://img.shields.io/badge/Django--phonenumber--field-8.0.0-brightgreen.svg?style=flat&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-brightgreen.svg?style=flat&logo=docker&logoColor=white&color=blue)
![Gunicorn](https://img.shields.io/badge/Gunicorn-brightgreen.svg?style=flat&logo=gunicorn&logoColor=white&color=blue)
![Nginx](https://img.shields.io/badge/Nginx-brightgreen.svg?style=flat&logo=nginx&logoColor=white&color=blue)

## Локальное развертывание проекта
1. Находясь в дериктории, где будет размещаться проект, склонируйте его репозиторий:  
```
git@github.com:alexpunder/deti_tepldom.git
```
2. Перейди в папку проекта:  
```
cd deti_tepldom
```
4. Создайте и заполните .env-файл необходимыми данными  

### Вариант 1: Если установлен Python 3.12

5. Создайте и активируйте виртуальное окружение:
```
python -m venv venv
```
```
python venv/Scripts/activate
```
6. Перейдите в директорию самого Django-приложения:
```
cd teplyj_dom
```
7. При необходимости, обновите pip (`python -m pip install --upgrade pip`) и установите необходимые зависимости:
```
pip install -r requirements.txt
```
8. Выполните команды создания файлов миграций и их применение:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
9. Введите команду по запуску локального сервера средствами Django:
```
python manage.py runserver
```
10. Проект доступен по адресу `127.0.0.1:8000`

### Вариант 2: Если установлен Docker

5. Используя терминал, введите команду:  
```
docker compose -f docker-compose.local.yml up
```
6. После окончания сборки, проект станет доступен по адресу `localhost:8080`
7. Для корректной работы backend'а приложения, выполните команды:
7.1. Соберите всю статику проекта:
```
docker compose exec backend python manage.py collectstatic
```
7.2. Скопируйте её в Docker Volume:
```
docker compose exec backend cp -r /app/staticfiles/. /static/
```
7.3. Выполните команды создания файлов миграций и их применение:
```
docker compose exec backend python manage.py makemigrations
```
```
docker compose exec backend python manage.py migrate
```
