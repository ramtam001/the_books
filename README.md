# the_books
Простое приложение на Django для коллекции книг.

## Что внутри

- `Author` — автор (имя)
- `Book` — книга (название, автор, дата публикации, жанр, кол-во страниц, описание)
- Список книг и страница отдельной книги
- Админка для добавления и редактирования книг

## Установка

```
cd bookshelf
python3 -m pip install -r requirements.txt
```

## Настройка базы данных

```
python3 manage.py makemigrations books
python3 manage.py migrate
python3 manage.py createsuperuser
```

При создании суперпользователя нужно будет ввести логин, email и пароль — они понадобятся для входа в админку.

## Запуск

```
python3 manage.py runserver
```

- Список книг: http://127.0.0.1:8000/
- Админка: http://127.0.0.1:8000/admin/

## Структура проекта

```
bookshelf/
├── manage.py
├── requirements.txt
├── bookshelf/          # настройки проекта
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── books/               # приложение
    ├── models.py
    ├── admin.py
    ├── views.py
    ├── urls.py
    └── templates/books/
```

## Добавление книг

Проще всего добавлять книги через админку (http://127.0.0.1:8000/admin/), предварительно создав хотя бы одного автора.
