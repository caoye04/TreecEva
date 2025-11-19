library_catalog = {'Python Tricks', 'Effective Java', 'Clean Code', 'Design Patterns', 'Refactoring'}
borrowed_books = {'Python Tricks', 'Clean Code'}

available_books = library_catalog - borrowed_books
book_count = len(available_books) if available_books else 0

print(f'Result: {book_count}')