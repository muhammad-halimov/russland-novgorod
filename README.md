# Dolor Novgorod-Russland

- Авторизация и регистрация
- Загрузка и скачивания фото и видео
- Создания альбомов 
- Редактирование альбомов и добавление фото
- Отдельные страницы альбомов/фото/видео
- Поиск по тегам, фед. округам
- Редактор фотографий и обложек
- Админ. панель (переход на главной странице в /admin)
- Профиль пользователя
- Редактирования данных пользователя
- Автоопределение тегов через ИИ
- Слайдер для просмотра содержимого альбомов
- Добавление соавторов в альбомы
- Разделение альбомов на личные и публичные

# Установка и запуск
- Установить python
- Создать виртуальную среду:
```
python3 - Linux/macOS
python - Windows NT
pip3 - Linux/macOS
pip - Windows NT
```
```
python -m venv venv
```
- Активировать виртуальную среду:
```
venv/Scripts/activate - Windows 
```
```
source venv/bin/activate - GNU/Linux & macOS/BSD
```
- Дальше по инструкции:
```
pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
```
CTRL + C - для остановки сервера
```

## Лицензия

Лицензировано под лицензией:

* GPL3 license (https://www.gnu.org/licenses/gpl-3.0.en.html)

## Целевая ОС

- Windows NT 10/11
- GNU/Linux - дистрибутивы
- BSD/Mach - macOS
