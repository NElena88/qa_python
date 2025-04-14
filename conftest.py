import pytest


from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def book_1(collector):
    collector.add_new_book('Туда и обратно')
    collector.set_book_genre('Туда и обратно', 'Фантастика')
    return collector

@pytest.fixture
def book_2(collector):
    collector.add_new_book('Колобок')
    collector.set_book_genre('Колобок', 'Мультфильмы')
    return collector

@pytest.fixture
def book_3(collector):
    collector.add_new_book('Шерлок Холмс')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')
    return collector

