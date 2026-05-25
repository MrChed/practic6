# Magazine API

http://127.0.0.1:8000/api/v1/journals/ ИЛИ http://127.0.0.1:8000/api/v1/journals/1/ (для теста)

REST API для управления журналами, разработанный с использованием Django REST Framework.

## Модель данных

### Journal

- id — идентификатор
- title — название журнала
- publisher — издательство
- category — категория
- issue_number — номер выпуска
- release_date — дата выпуска
- price — цена

---

## Эндпоинты API

Базовый URL: 
/api/v1/journals/

### Получение списка журналов

GET /api/v1/journals/

Фильтры:

- GET /api/v1/journals/?category=IT
- GET /api/v1/journals/?publisher=Tech


Пример запроса:

```
{
  "title": "Python Magazine",
  "publisher": "Tech Media",
  "category": "IT",
  "issue_number": 25,
  "release_date": "2026-05-25",
  "price": "499.00"
}
```
Удаление журнала
DELETE /api/v1/journals/{id}/

Документация к API

http://127.0.0.1:8000/api/docs/

<img width="1496" height="807" alt="image" src="https://github.com/user-attachments/assets/299aa408-b42a-4361-aef9-c55ee8fbb056" />
<img width="1461" height="263" alt="image" src="https://github.com/user-attachments/assets/9780c077-b03d-4bb6-85ea-5840385b6a8c" />
