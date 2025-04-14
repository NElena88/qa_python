# qa_python
# BooksCollector

**BooksCollector** — это приложение для управления коллекцией книг. Оно позволяет добавлять книги с жанрами, добавлять книги в избранное и получать различные списки книг в зависимости от жанра или других условий.

## Функционал

- **add_new_book** — добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.
- **set_book_genre** — устанавливает жанр книги, если книга есть в `books_genre` и её жанр входит в список доступных жанров.
- **get_book_genre** — выводит жанр книги по её названию.
- **get_books_with_specific_genre** — возвращает список книг с определённым жанром.
- **get_books_genre** — возвращает текущий словарь `books_genre`.
- **get_books_for_children** — возвращает книги, которые подходят детям (книги без возрастного рейтинга).
- **add_book_in_favorites** — добавляет книгу в избранное. Книга должна быть в словаре `books_genre`. Повторно добавить книгу в избранное нельзя.
- **delete_book_from_favorites** — удаляет книгу из избранного, если она там есть.
- **get_list_of_favorites_books** — возвращает список избранных книг.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/BooksCollector.git
   
2. Перейдите в директорию проекта:
   ```bash
   cd BooksCollector
   
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
Запуск тестов

Тесты написаны с использованием pytest. Для их запуска выполните следующую команду:
```bash
pytest
```
Описание тестов

1. test_add_new_book Добавляет книгу и проверяет, что их количество в словаре books_rating равно 2.
2. test_add_new_book_name_more_than40 Проверяем добавление книги, в названии которой более 40 символов.
3. test_add_new_book_empty_name Проверяем добавление книги с пустым наименованием. 
4. test_set_book_genre_valid Проверяет, что жанр книги "Туда и обратно" установлен как "Фантастика". 
5. test_set_book_genre_invalid_book Проверяет, что если книга не существует в books_genre, она не добавляется в список жанров. 
6. test_get_book_genre_various_cases (параметризованный тест) Проверяет жанры для различных книг: "Колобок" (Мультфильмы), "Шерлок Холмс" (Детектив) и несуществующую книгу (None). 
7. test_get_books_with_specific_genre_parametrized (параметризованный тест) Проверяет, что для жанра "Детектив" возвращается книга "Шерлок Холмс", а для "Комедии" — пустой список. 
8. test_get_books_genre_returns_correct_dict Проверяет, что словарь books_genre возвращает правильные пары "книга — жанр". 
9. test_get_books_genre_returns_empty_dict_initially Проверяет, что словарь books_genre пуст при инициализации нового экземпляра. 
10. test_get_books_for_children_returns_only_safe_genres Проверяет, что метод get_books_for_children возвращает только безопасные для детей жанры. 
11. test_add_book_in_favorites_various_cases (параметризованный тест) Проверяет добавление книги в избранное: книга должна быть в books_genre, иначе не добавляется. 
12. test_add_book_in_favorites_does_not_duplicate Проверяет, что книга не добавляется в избранное дважды. 
13. test_delete_book_from_favorites_removes_book Проверяет, что книга удаляется из избранного. 
14. test_get_list_of_favorites_books_returns_correct_list Проверяет, что метод get_list_of_favorites_books возвращает правильный список избранных книг.

