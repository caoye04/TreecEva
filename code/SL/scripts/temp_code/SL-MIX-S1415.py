class ShelfNode:
    def __init__(self, books_dict):
        self.books = books_dict
        self.next = None

def create_linked_library(shelf_data_list):
    if not shelf_data_list:
        return None
    head = ShelfNode(shelf_data_list[0])
    current = head
    for books in shelf_data_list[1:]:
        current.next = ShelfNode(books)
        current = current.next
    return head

# Initial shelf data
shelf_inventories = [
    {'Quantum Mechanics': 5, 'Relativity': 3},
    {'Quantum Mechanics': 2, 'Thermodynamics': 7},
    {'Quantum Mechanics': 4, 'Electromagnetism': 6}
]

# Create linked list of shelves
library_head = create_linked_library(shelf_inventories)

# Restocking formula: new_count = original_count * 2 + 1
restock_formula = lambda count: count * 2 + 1

# Process each shelf
current_shelf = library_head
quantum_total = 0
while current_shelf:
    if 'Quantum Mechanics' in current_shelf.books:
        quantum_total += restock_formula(current_shelf.books['Quantum Mechanics'])
    current_shelf = current_shelf.next

print(f"Result: {quantum_total}")