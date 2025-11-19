class BookNode:
    def __init__(self, book_id, checkout_count):
        self.book_id = book_id
        self.checkout_count = checkout_count
        self.next = None

def build_linked_list(book_data):
    if not book_data:
        return None
    head = BookNode(book_data[0][0], book_data[0][1])
    current = head
    for book_id, count in book_data[1:]:
        current.next = BookNode(book_id, count)
        current = current.next
    return head

def update_counts_from_returns(head, returns_log):
    # Create dictionary from linked list for efficient updates
    book_dict = {}
    current = head
    while current:
        book_dict[current.book_id] = current
        current = current.next
    
    # Process returns (negative checkouts)
    for book_id, return_count in returns_log.items():
        if book_id in book_dict:
            book_dict[book_id].checkout_count -= return_count
    
    return head

def calculate_popular_books_score(head):
    score = 0
    current = head
    while current:
        if current.checkout_count > 5:
            score += current.checkout_count
        current = current.next
    return score

# Initial book data: (book_id, checkout_count)
initial_books = [
    ('SCI001', 8),
    ('FIC002', 3),
    ('HIS003', 12),
    ('MTH004', 7),
    ('ART005', 2)
]

# Returns processing log (book_id, return_count)
returns_processing_log = {
    'SCI001': 2,
    'HIS003': 3,
    'MTH004': 1,
    'ART005': 1
}

# Build the linked list
library_collection = build_linked_list(initial_books)

# Update counts based on returns
updated_collection = update_counts_from_returns(library_collection, returns_processing_log)

# Calculate final popularity score
final_popularity_score = calculate_popular_books_score(updated_collection)

print(f'Result: {final_popularity_score}')