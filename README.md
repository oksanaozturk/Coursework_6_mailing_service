## Coursework_6_mailing_service
## Курсовая 6. Основы веб-разработки на Django
## "Веб-сервис по управлению рассылками"

### Используемые технологии:

 - Python
 - Django
 - PostgerSQL
 - WSL
 - redis


### Инструкция по развертыванию проекта

* #### Для разворачивания проекта потребуется создать и заполнить файл .env  по шаблону файла env.sample
* #### Перед запуском web-приложения создайте базу данных, создайте и примените миграции
  - python manage.py migrate
* #### Используется виртуальное окружение - venv, зависимости записаны в файл requirements.txt
  - pip install -r requirements.txt

* #### Используйте команду "python manage.py csu" для создания суперпользователя.

* #### Для загрузки данных используйте команду
  - python manage.py loaddata data_blog.json
  - python manage.py loaddata data_main.json 
  - python manage.py loaddata data_users.json  

* #### Команда для запуска Приложения: 
  - python manage.py runserver
  
* #### В проекте используется кеширование, поэтому для работы нужно запустить сервер Redis. 
  - Ссылка на инструкцию https://redis.io/docs/latest/develop/.

* #### После создания клиентов и рассылок, используйте команду (отправка сообщений рассылок Получателям)
  - python manage.py runapscheduler


### Автор проекта https://github.com/oksanaozturk
