class ListNode:
    def __init__(self, book_id=0, next=None):
        self.book_id = book_id
        self.next = next

# Initialize linked list: 101 -> 202 -> 103 -> 404 -> 105
head = ListNode(101)
head.next = ListNode(202)
head.next.next = ListNode(103)
head.next.next.next = ListNode(404)
head.next.next.next.next = ListNode(105)

# Traverse linked list and collect book IDs
node = head
book_ids = []
while node:
    book_ids.append(node.book_id)
    node = node.next

# Use list comprehension to find even book IDs
even_book_ids = [book_id for book_id in book_ids if book_id % 2 == 0]

even_book_count = len(even_book_ids)
print(f"Result: {even_book_count}")