# cinema

## Структура базы данных

### Movie (Фильмы)
- title — название фильма
- genre — жанр
- duration — длительность
- release_date — дата выхода
- rating — рейтинг
- description — описание

### Hall (Залы)
- name — название зала
- capacity — вместимость
- hall_type — тип зала

### Customer (Клиенты)
- full_name — имя клиента
- phone — телефон
- email — email

### Session (Сеансы)
- movie — фильм
- hall — зал
- start_time — время начала
- price — цена
- language — язык

### Ticket (Билеты)
- customer — клиент
- session — сеанс
- seat_number — место
- purchase_date — дата покупки
- status — статус


## эндпойнты

### Movies
- GET /api/v1/movies/
- GET /api/v1/movies/{id}/
- POST /api/v1/movies/
- PATCH /api/v1/movies/{id}/
- DELETE /api/v1/movies/{id}/

### Halls
- GET /api/v1/halls/
- GET /api/v1/halls/{id}/
- POST /api/v1/halls/
- PATCH /api/v1/halls/{id}/
- DELETE /api/v1/halls/{id}/

### Customers
- GET /api/v1/customers/
- GET /api/v1/customers/{id}/
- POST /api/v1/customers/
- PATCH /api/v1/customers/{id}/
- DELETE /api/v1/customers/{id}/

### Sessions
- GET /api/v1/sessions/
- GET /api/v1/sessions/{id}/
- POST /api/v1/sessions/
- PATCH /api/v1/sessions/{id}/
- DELETE /api/v1/sessions/{id}/

### Tickets
- GET /api/v1/tickets/
- GET /api/v1/tickets/{id}/
- POST /api/v1/tickets/
- PATCH /api/v1/tickets/{id}/
- DELETE /api/v1/tickets/{id}/

Swagger UI:
http://127.0.0.1:8000/api/docs/

## Запуск проекта

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver/
```
