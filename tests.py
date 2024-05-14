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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name', ['Book1', 'Book2'])
    def test_add_new_book(self, name):
        collector2 = BooksCollector()
        collector2.add_new_book('Book1')
        assert 'Book1' in collector2.books_genre

    def test_set_book_genre(self):
        collector3 = BooksCollector()

        collector3.add_new_book('Book3')
        collector3.set_book_genre('Book3', 'Ужасы')
        assert collector3.get_book_genre('Book3') == 'Ужасы'

    def test_get_book_genre(self):
        collector4 = BooksCollector()

        collector4.add_new_book('Book4')
        collector4.set_book_genre('Book4', "Фантастика")
        assert collector4.get_book_genre('Book4') == "Фантастика"

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre(self, genre):
        collector5 = BooksCollector()

        collector5.add_new_book('Book5')
        collector5.set_book_genre('Book5', 'Фантастика')
        assert collector5.get_book_genre('Book5') == 'Фантастика'

    def test_get_books_genre(self):
        collector6 = BooksCollector()

        collector6.add_new_book('Book6')
        assert collector6.get_books_genre() == {'Book6': ''}

    def test_get_books_for_children(self):
        collector7 = BooksCollector()

        collector7.add_new_book('Book7')
        collector7.set_book_genre('Book7', 'Мультфильмы')
        assert 'Book7' in collector7.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector8 = BooksCollector()

        collector8.add_new_book('Book8')
        collector8.add_book_in_favorites('Book8')
        assert 'Book8' in collector8.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector9 = BooksCollector()

        collector9.add_new_book('Book9')
        collector9.add_book_in_favorites('Book9')
        collector9.delete_book_from_favorites('Book9')
        assert 'Book9' not in collector9.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector10 = BooksCollector()

        collector10.add_new_book('Book10')
        collector10.add_book_in_favorites('Book10')
        assert collector10.get_list_of_favorites_books() == ['Book10']





