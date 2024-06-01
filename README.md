# api_final_yatube

api_final_yatube - это проект для управления БД, который предоставляет возможности для создания, обновления, удаления и просмотра: подписок, постов и комментариев к ним, через RESTful API.


## Установка

Клонируйте репозиторий  
git clone git@github.com:SkullPiercer/api_final_yatube.git

Перейдите в рабочую директорию  
cd api_final_yatube

Установите виртуальное окружение  
python -m venv venv

Активируйте виртуальное окружение  
source venv/Scripts/activate

Обновите пакетный менеджер  
python -m pip install --upgrade pip

Установите необходимые библиотеки  
pip install -r requirements.txt

Выполните миграции  
python manage.py migrate

Запустите сервер  
python manage.py runserver

## Примеры запросов

Тип запроса: GET  
Эндпоинт: /api/v1/posts/  
Описание: Вернет вам все посты. Так же вы можете использовать параметры offset и limit для разграничения выборки

Тип запроса: POST  
Эндпоинт: /api/v1/posts/{post_id}/comments/  
Описание: Создаст комментарий к посту с переданным id

Тип запроса: Delete  
Эндпоинт: /api/v1/posts/{post_id}/comments/{id}/  
Описание: Удалить ваш комментарий. Доступно только автору!

Тип запроса: GET  
Эндпоинт: /api/v1/jwt/create/  
Описание: Адрест для получения JWT-токена  

## Использованные технологии
Использованные технологии
Python: основной язык программирования для логики приложения.  
Django: веб-фреймворк для разработки серверной части.  
Django REST Framework: библиотека для создания RESTful API.  
SQLite: база данных по умолчанию (может быть заменена на PostgreSQL, MySQL и другие).


## Авторы
Имя: Александр  
email: akatsuki_sanya@vk.com  
GitGub: SkullPiercer  
При поддержке Ревьюера и команды Яндекс Практикума