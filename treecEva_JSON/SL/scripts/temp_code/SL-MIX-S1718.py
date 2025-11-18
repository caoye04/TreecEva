class BookNode:
    def __init__(self, isbn, available=True, next_node=None):
        self.isbn = isbn
        self.available = available
        self.next = next_node

def create_library():
    # Creating a small library collection as a linked list
    book3 = BookNode(9780262033848, False)
    book2 = BookNode(9780134092656, True, book3)
    book1 = BookNode(9780262033847, True, book2)
    return book1

library_head = create_library()

# Lambda to check if a book is available
is_available = lambda node: node.available if node else False

# Logical operation to determine if we can borrow a book
book_to_check = library_head.next  # Checking the second book
other_condition = True

# Complex logical expression using AND, OR, NOT
can_borrow = (is_available(book_to_check) and other_condition) or (not is_available(book_to_check) and not other_condition)

print(f"Result: {int(can_borrow)}")