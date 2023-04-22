import pytest

new_book = 'Гордость и предубеждение и зомби'
another_new_book = 'Что делать, если ваш кот хочет вас убить'
books_with_ratings = {
    new_book: 6,
    another_new_book: 10,
    '9 мест, где надо побывать с мертвой принцессой': 8
}


class TestBooksCollector:

    def test_init_books_rating_type_is_dictionary(self, collector):
        assert collector.get_books_rating() == {}, 'Books rating type is not dictionary'

    def test_init_favorites_type_is_list(self, collector):
        assert collector.get_list_of_favorites_books() == [], 'List of favorite books type is not a list'

    def test_add_new_book_add_two_books_count_books_two(self, collector):
        collector.add_new_book(new_book)
        collector.add_new_book(another_new_book)

        assert len(collector.get_books_rating()) == 2, 'Books arent added'

    def test_add_new_book_add_two_same_books_count_books_one(self, collector):
        collector.add_new_book(new_book)
        collector.add_new_book(new_book)

        assert len(collector.get_books_rating()) == 1, 'Same books added'

    def test_set_book_rating_add_rating_to_nonexistent_book_rating_is_none(self, collector):
        collector.set_book_rating(new_book, 10)

        assert collector.get_book_rating(new_book) is None, 'Rating of nonexistent book is set'

    @pytest.mark.parametrize('rating', [-1, 15])
    def test_set_book_rating_add_new_book_with_out_of_range_one_to_ten_rating_rating_not_change(self, collector, rating):
        collector.add_new_book(new_book)
        collector.set_book_rating(new_book, rating)

        assert collector.get_book_rating(new_book) != rating, 'Rating is out of range'

    def test_get_book_rating_get_nonexistent_book_rating_rating_is_none(self, collector):
        assert collector.get_book_rating(new_book) is None, 'Rating of nonexistent book is get'

    def test_add_book_in_favorites_add_new_book_book_in_favorites(self, collector):
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)

        assert new_book in collector.get_list_of_favorites_books(), 'Book isnt added to favorites'

    def test_get_books_with_specific_rating_add_three_new_books_one_book_with_rating_more_than_eight(self, collector):
        for book, book_rating in books_with_ratings.items():
            collector.add_new_book(book)
            collector.set_book_rating(book, book_rating)

        assert len(collector.get_books_with_specific_rating(8)) == 1, 'Not one book with a rating of more than eight'

    def test_delete_book_from_favorites_add_new_book_to_favorites_count_of_books_is_zero(self, collector):
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        collector.delete_book_from_favorites(new_book)

        assert len(collector.get_list_of_favorites_books()) == 0, 'Book isnt deleted'
