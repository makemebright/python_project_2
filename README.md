# python_project_2
**Бот на aiogram**
Функционал: по ингредиентам или названию блюда выдает ссылку на рецепт, есть возможность добавить рецепт в индивидуальную для каждого пользоваетеля кулинарную книгу, в кулинарной книге есть возможность просматривать ранее добавленные рецепты. Управление осуществляется кнопками.\ 
Основной файл: main.py, в файле содержатся все хэндлеры. \
в файле func.py содержатся необходимые для парсинга или работы с файлами функции. \
В файле user_books.json ОБЯЗАТЕЛЬНО содержится список (вначале пустой), в который записываются юзернеймы пользователей и понравившиеся им рецепты. \
Второй .json файл вспомогательный, в него записываются ссылки на рецепты по запросам. \
Для запуска бота необходимо наличе файла config.py, с константой TOKEN, в которой содержится токен для запуска бота. 
