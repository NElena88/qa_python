import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2


    def test_set_book_genre_valid(collector, book_1):
        assert collector.books_genre['Туда и обратно'] == 'Фантастика'

    def test_set_book_genre_invalid_book(collector):
        collector.set_book_genre('4891', 'Фантастика')
        assert '4891' not in collector.get_books_genre()

    @pytest.mark.parametrize(
        'book_name, expected_genre',
        [
            ('Колобок', 'Мультфильмы'),
            ('Шерлок Холмс', 'Детектив'),
            ('Гарри Поттер', None),
        ]
    )
    def test_get_book_genre_various_cases(collector, book_2, book_3, book_name, expected_genre):
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize(
        'genre, expected_books',
        [
            ('Детектив', ['Шерлок Холмс']),
            ('Комедии', []),
        ]
    )
    def test_get_books_with_specific_genre_parametrized(collector, book_3, genre, expected_books):
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre_returns_correct_dict(collector, book_1, book_2, book_3):

        expected = {
        'Колобок': 'Мультфильмы',
        'Туда и обратно': 'Фантастика',
        'Шерлок Холмс': 'Детектив'
        }
        assert collector.get_books_genre() == expected

    def test_get_books_genre_returns_empty_dict_initially(collector):
        assert collector.get_books_genre() == {}

    def test_get_books_for_children_returns_only_safe_genres(collector, book_1, book_2, book_3):
        result = collector.get_books_for_children()

        assert 'Туда и обратно' in result
        assert 'Колобок' in result
        assert 'Шерлок Холмс' not in result

    @pytest.mark.parametrize(
        'book_name, expected_in_favorites',
        [
            ('Туда и обратно', True),
            ('Такой книги нет', False),
        ]
    )
    def test_add_book_in_favorites_various_cases(collector, book_1, book_name, expected_in_favorites):
        collector.add_book_in_favorites(book_name)
        result = collector.get_list_of_favorites_books()
        assert (book_name in result) == expected_in_favorites

    def test_add_book_in_favorites_does_not_duplicate(collector):
        collector.add_new_book('Туда и обратно')
        collector.add_book_in_favorites('Туда и обратно')
        collector.add_book_in_favorites('Туда и обратно')
        assert collector.get_list_of_favorites_books().count('Туда и обратно') == 1

    def test_delete_book_from_favorites_removes_book(collector):
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.delete_book_from_favorites('Шерлок Холмс')
        assert 'Шерлок Холмс' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_correct_list(collector):
        collector.add_new_book('Туда и обратно')
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Туда и обратно')
        collector.add_book_in_favorites('Шерлок Холмс')
        result = collector.get_list_of_favorites_books()
        assert result == ['Туда и обратно', 'Шерлок Холмс']
