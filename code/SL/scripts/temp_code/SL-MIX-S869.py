from collections import deque

# Book IDs processed during the day
book_operations = [
    ('return', 987),
    ('return', 123),
    ('checkout', None),
    ('return', 456),
    ('return', 234),
    ('checkout', None),
    ('return', 789)
]

library_queue = deque()

for operation, book_id in book_operations:
    if operation == 'return':
        library_queue.append(book_id)
    elif operation == 'checkout' and library_queue:
        library_queue.popleft()

# Sort remaining books in ascending order
sorted_books = sorted(library_queue)

# Calculate checksum as sum of first three book IDs
checksum = sum(sorted_books[:3])

print(f"Result: {checksum}")