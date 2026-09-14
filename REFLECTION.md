# Reflection

##Test Failure

FAIL: test_book_in_database_appears_on_books_page (catalog.tests.BookListTests.test_book_in_database_appears_on_books_page)

AssertionError: False is not true : Couldn't find 'Unique Testing Book' in the following response

FAILED (failures=1)

My test failed because I temporarily changed the Books view so it returned no books from the database. This proved that the test correctly checks wheter a book in the database appears on the Books page.

#Question 1

The book model carries the ForeignKey to Publisher because each book belongs to one publisher, while one publisher can have many books. If i reversed it, the relationship would no longer correctly represent one publisher having multiple books.

##Question 2

I added 'publication_year to the Book model using an IntegerField because a year is a number. If I had used a CharField instead, Django would treat the year as text instead of numeric data.