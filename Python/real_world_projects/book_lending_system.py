def borrow_book(available_books, borrowed_books, book_title):
    if book_title in available_books:
        available_books.remove(book_title)
        borrowed_books.append(book_title)
        return True
    else:
        return False

available = ['1984', 'Dom Casmurro', 'O Rabbit']
borrowed_books = []

title_input = input('Enter the book title: ')
update_books = borrow_book(available, borrowed_books, title_input)

if update_books:
    print('Book available, you can take it!')
else:
    print('Book unavailable at the moment!')

formatted_available = ', '.join(f'{book}' for book in available)
formatted_borrowed = ', '.join(f'{book}' for book in borrowed_books)

print(f'Available books: {formatted_available}')
print(f'Unavailable books: {formatted_borrowed}')
