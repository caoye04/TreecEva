import bisect

def find_insertion_point(sorted_books, new_book_id):
    return bisect.bisect_left(sorted_books, new_book_id)

library_shelf = [10, 15, 23, 31, 37, 45, 58, 63, 72, 89]
target_book = 42
insertion_index = find_insertion_point(library_shelf, target_book)
print(f'Result: {insertion_index}')