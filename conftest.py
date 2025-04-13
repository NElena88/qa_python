import pytest


from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def book_1(collector):
    collector.add_new_book('Туда и обратно')
    collector.set_book_genre('Туда и обратно', 'Фантастика')
    book_1 = collector.set_book_genre

@pytest.fixture
def book_2(collector):
    collector.add_new_book('Колобок')
    collector.set_book_genre('Колобок', 'Мультфильмы')
    book_2 = collector.set_book_genre

@pytest.fixture
def book_3(collector):
    collector.add_new_book('Шерлок Холмс')
    collector.set_book_genre('Шерлок Холмс', 'Детектив')
    book_3 = collector.set_book_genre

