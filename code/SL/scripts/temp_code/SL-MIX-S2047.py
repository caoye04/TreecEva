from collections import defaultdict

class BookNode:
    def __init__(self, book_id, count=0):
        self.book_id = book_id
        self.count = count
        self.next = None

class LibraryTracker:
    def __init__(self):
        self.head = None
        self.book_map = {}
    
    def add_book(self, book_id):
        new_node = BookNode(book_id)
        self.book_map[book_id] = new_node
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def update_checkouts(self, checkout_logs):
        for log in checkout_logs:
            if log in self.book_map:
                self.book_map[log].count += 1

def find_most_popular(library_tracker):
    current = library_tracker.head
    max_count = -1
    popular_book = None
    while current:
        if current.count > max_count:
            max_count = current.count
            popular_book = current.book_id
        current = current.next
    return popular_book

# Initialize tracker
tracker = LibraryTracker()
books = [101, 102, 103, 104, 105]
for book in books:
    tracker.add_book(book)

# Process checkout logs
checkouts_today = [101, 103, 101, 102, 101, 103, 101]
tracker.update_checkouts(checkouts_today)

# Find most popular book
most_popular_id = find_most_popular(tracker)
print(f"Result: {most_popular_id}")