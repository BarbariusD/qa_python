import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_without_genre(self):
        collector = BooksCollector()
        
        collector.add_new_book('Гарри Поттер')

        assert collector.get_book_genre('Гарри Поттер') == ''


    def test_add_new_book_two_same_books(self):
        collector = BooksCollector()

        collector.add_new_book('Война и Мир')
        collector.add_new_book('Война и Мир')

        assert len(collector.get_books_genre()) == 1


    @pytest.mark.parametrize('name', ['', '40символов40символов40символов40символов4'])
    def test_add_new_book_without_name_and_more_than_40_symbols_failed(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0


    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Автостопом по Галактике')
        collector.set_book_genre('Автостопом по Галактике', 'Фантастика')

        assert collector.get_book_genre('Автостопом по Галактике') == 'Фантастика'


    def test_get_book_genre_book_without_genre(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Без названия') is None


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Танатонавты')
        collector.add_new_book('Автостопом по Галактике')
        collector.set_book_genre('Танатонавты', 'Фантастика')
        collector.set_book_genre('Автостопом по Галактике', 'Фантастика')

        collector.get_books_genre()

        assert collector.get_books_with_specific_genre('Фантастика') == ['Танатонавты', 'Автостопом по Галактике']


    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Ревизор')
        collector.add_new_book('Автостопом по Галактике')

        collector.set_book_genre('Автостопом по Галактике', 'Фантастика')
        collector.set_book_genre('Ревизор', 'Комедии')

        assert collector.get_books_genre() == {'Автостопом по Галактике' : 'Фантастика',
                                               'Ревизор' : 'Комедии'}


    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('2001: Космическая Одиссея')
        collector.set_book_genre('2001: Космическая Одиссея', 'Фантастика')

        assert collector.get_books_for_children() == ['2001: Космическая Одиссея']


    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Автостопом по Галактике')
        collector.add_book_in_favorites('Автостопом по Галактике')
        collector.delete_book_from_favorites('Автостопом по Галактике')

        assert collector.get_list_of_favorites_books() == []


    def test_add_book_in_favorites_two_same_books(self):
        collector = BooksCollector()

        collector.add_new_book('Танатонавты')
        collector.add_book_in_favorites('Танатонавты')
        collector.add_book_in_favorites('Танатонавты')

        assert collector.get_list_of_favorites_books() == ['Танатонавты'] 


    def test_get_books_for_children_not_allowed_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_for_children() == []