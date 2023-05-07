# Django/DRF/Swagger Test project
Тестовый проект по Django/DRF и документации Swagger


База данных - sqlite

Версия Django - 4.2.0

Версия Django REST Framework - 3.14.0



Стандартная админка:

http://127.0.0.1:8000/admin/


Сама апишка:

http://127.0.0.1:8000/

http://127.0.0.1:8000/departments/

http://127.0.0.1:8000/employees/


Документация по API:

http://127.0.0.1:8000/swagger/

http://127.0.0.1:8000/redoc/



Инструкция по развороту на локалке:

1) Сделать git clone данного репозитория
2) Создать виртуальное окружение Python (venv)
3) Установить внешние зависимости (python -m pip install -r requirements.txt)
4) Создать файл миграций (python manage.py makemigrations)
5) Залить миграции в базу (python manage.py migrate)
6) Создать в базе юзера-админа (python manage.py createsuperuser)
7) Запустить локальный сервер (python manage.py runserver)
8) ???
9) PROFIT!!1!
