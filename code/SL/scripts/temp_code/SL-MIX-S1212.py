class InventoryNode:
    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity
        self.next = None

def calculate_content_hash(item_id, quantity):
    return hash(f"{item_id}:{quantity}") % 1000000

def process_warehouse_updates():
    # Initialize linked list with base inventory
    head = InventoryNode('WH001', 150)
    head.next = InventoryNode('WH002', 200)
    head.next.next = InventoryNode('WH003', 75)
    
    # Hash table for tracking item categories
    category_map = {
        'WH001': 'ELECTRONICS',
        'WH002': 'CLOTHING',
        'WH003': 'BOOKS'
    }
    
    # Process inventory updates
    updates = [
        ('WH001', -25),   # Sold 25 units
        ('WH002', 50),    # Received 50 units
        ('WH004', 125),   # New item
        ('WH003', -30)    # Sold 30 units
    ]
    
    # Add new node for WH004
    current = head
    while current.next:
        current = current.next
    current.next = InventoryNode('WH004', 0)
    
    # Apply updates using nested loops
    for location, delta in updates:
        current = head
        found = False
        while current and not found:
            if current.item_id == location:
                current.quantity += delta
                found = True
            else:
                current = current.next
        
        if not found and location == 'WH004':
            # Update the newly added node
            current = head
            while current.next:
                current = current.next
            current.quantity = delta
    
    # Calculate final checksum using list comprehension
    node_values = []
    current = head
    while current:
        node_values.append((current.item_id, current.quantity))
        current = current.next
    
    # String transformations for category labeling
    labeled_quantities = [
        f"{category_map.get(item_id, 'OTHER')}:{qty}" 
        for item_id, qty in node_values
    ]
    
    # Final checksum calculation
    checksum_components = [
        calculate_content_hash(item_id, qty) 
        for item_id, qty in node_values
    ]
    
    final_checksum = sum(checksum_components) % 997
    
    # Apply correction factor based on category
    electronics_count = sum(
        qty for item_id, qty in node_values 
        if category_map.get(item_id) == 'ELECTRONICS'
    )
    
    if electronics_count > 100:
        final_checksum = (final_checksum * 3) % 997
    else:
        final_checksum = (final_checksum + 42) % 997
    
    return final_checksum

final_checksum = process_warehouse_updates()
print(f"Result: {final_checksum}")