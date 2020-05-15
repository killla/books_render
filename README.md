# Библиотека книг

Данная программа является библиотекой для чтения книг, ранее скачанных с сайта [tululu.org](tululu.org)

### Как установить

Для запуска программы на компьютере должен быть установлен Python третьей версии. 

- Скачайте все файлы библиотеки в отдельную папку 
- Установите зависимости командой `pip install -r requirements.txt`

### Как подготовить данные для библиотеки
Для подготовки данных необходимо скачать книги с сайта [tululu.org](tululu.org) с помощью программы
[parse_tululu](https://github.com/killla/parse_tululu) в соответствии с инструкцией.

Результат работы программы `parse_tululu`:
- файл `books.json`
- папка `books`
- папка `images`

следует сложить в папку библиотеки.

### Как запустить
Запустите программу командой `python3 render_website.py`

### Как пользоваться
- Перейдите по ссылке
[http://localhost:5500/](http://localhost:5500/)
- Откройте любую страницу с книгами
- Выберите понравившуюся книгу и нажмите кнопку `Читать`

### Библиотека онлайн
При наличии доступа в Интернет можно пользоваться библиотекой без установки по ссылке 
[https://killla.github.io/books/](https://killla.github.io/books/pages/index1.html)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).