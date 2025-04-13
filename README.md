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

1. test_add_new_book_add_two_books
Добавляет две книги и проверяет, что их количество в словаре books_rating равно 2.
```python
def test_add_new_book_add_two_books(self):
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    assert len(collector.get_books_rating()) == 2
```

2. test_set_book_genre_valid 
Проверяет, что жанр книги "Туда и обратно" установлен как "Фантастика".
```python
2. test_set_book_genre_valid
Проверяет, что жанр книги "Туда и обратно" установлен как "Фантастика".
```

3. test_set_book_genre_invalid_book
Проверяет, что если книга не существует в books_genre, она не добавляется в список жанров.
```python
def test_set_book_genre_invalid_book(collector):
    collector.set_book_genre('4891', 'Фантастика')
    assert '4891' not in collector.get_books_genre()
```
4. test_get_book_genre_various_cases (параметризованный тест)
Проверяет жанры для различных книг: "Колобок" (Мультфильмы), "Шерлок Холмс" (Детектив) и несуществующую книгу (None).
```python
@pytest.mark.parametrize(
    'book_name, expected_genre',
    [
        ('Колобок', 'Мультфильмы'),
        ('Шерлок Холмс', 'Детектив'),
        ('Гарри Поттер', None),
    ]
)
def test_get_book_genre_various_cases(self, book_name, expected_genre):
    assert collector.get_book_genre(book_name) == expected_genre
```
5. test_get_books_with_specific_genre_parametrized (параметризованный тест)
Проверяет, что для жанра "Детектив" возвращается книга "Шерлок Холмс", а для "Комедии" — пустой список.
```python
@pytest.mark.parametrize(
    'genre, expected_books',
    [
        ('Детектив', ['Шерлок Холмс']),
        ('Комедии', []),
    ]
)
def test_get_books_with_specific_genre_parametrized(self, genre, expected_books):
    assert collector.get_books_with_specific_genre(genre) == expected_books
```

6. test_get_books_genre_returns_correct_dict
Проверяет, что словарь books_genre возвращает правильные пары "книга — жанр".
```python
def test_get_books_genre_returns_correct_dict(collector):
    expected = {
        'Колобок': 'Мультфильмы',
        'Туда и обратно': 'Фантастика',
        'Шерлок Холмс': 'Детектив'
    }
    assert collector.get_books_genre() == expected
```

7. test_get_books_genre_returns_empty_dict_initially
Проверяет, что словарь books_genre пуст при инициализации нового экземпляра.
```python
def test_get_books_genre_returns_empty_dict_initially():
    collectors = BooksCollector()
    assert collectors.get_books_genre() == {}
```

8. test_get_books_for_children_returns_only_safe_genres
Проверяет, что метод get_books_for_children возвращает только безопасные для детей жанры.
```python
def test_get_books_for_children_returns_only_safe_genres(self, collector):
    result = collector.get_books_for_children()
    assert 'Туда и обратно' in result
    assert 'Колобок' in result
    assert 'Шерлок Холмс' not in result
```

9. test_add_book_in_favorites_various_cases (параметризованный тест)
Проверяет добавление книги в избранное: книга должна быть в books_genre, иначе не добавляется.
```python
@pytest.mark.parametrize(
    'book_name, expected_in_favorites',
    [
        ('Туда и обратно', True),
        ('Такой книги нет', False),
    ]
)
def test_add_book_in_favorites_various_cases(self, book_name, expected_in_favorites):
    collector.add_book_in_favorites(book_name)
    result = collector.get_list_of_favorites_books()
    assert (book_name in result) == expected_in_favorites
```

10. test_add_book_in_favorites_does_not_duplicate
Проверяет, что книга не добавляется в избранное дважды.
```python
def test_add_book_in_favorites_does_not_duplicate(self, collector):
    collector.add_book_in_favorites('Туда и обратно')
    collector.add_book_in_favorites('Туда и обратно')
    assert collector.get_list_of_favorites_books().count('Туда и обратно') == 1
```

11. test_delete_book_from_favorites_removes_book
Проверяет, что книга удаляется из избранного.
```python
def test_delete_book_from_favorites_removes_book(self, collector):
    collector.add_book_in_favorites('Шерлок Холмс')
    collector.delete_book_from_favorites('Шерлок Холмс')
    assert 'Шерлок Холмс' not in collector.get_list_of_favorites_books()
```

12. test_get_list_of_favorites_books_returns_correct_list
Проверяет, что метод get_list_of_favorites_books возвращает правильный список избранных книг.
```python
def test_get_list_of_favorites_books_returns_correct_list(self, collector):
    collector.add_book_in_favorites('Туда и обратно')
    collector.add_book_in_favorites('Шерлок Холмс')
    result = collector.get_list_of_favorites_books()
    assert result == ['Туда и обратно', 'Шерлок Холмс']
```

