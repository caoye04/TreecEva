from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

class ListNode:
    def __init__(self, movement_type: str, quantity: int):
        self.movement_type = movement_type  # 'IN' or 'OUT'
        self.quantity = quantity
        self.next: Optional['ListNode'] = None

def process_movements(head: ListNode) -> int:
    # Base case
    if not head:
        return 0
    
    # Early return for single node
    if not head.next:
        return head.quantity if head.movement_type == 'IN' else -head.quantity
    
    # Divide the list into two halves
    slow = head
    fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Split the list
    prev.next = None
    
    # Conquer: recursively process both halves
    left_change = process_movements(head)
    right_change = process_movements(slow)
    
    return left_change + right_change

def build_movement_list(movements):
    if not movements:
        return None
    
    head = ListNode(movements[0][0], movements[0][1])
    current = head
    
    for movement_type, quantity in movements[1:]:
        current.next = ListNode(movement_type, quantity)
        current = current.next
    
    return head

# Build the movement list
movements = [
    ('IN', 150),
    ('OUT', 75),
    ('IN', 200),
    ('OUT', 50),
    ('IN', 125),
    ('OUT', 100),
    ('IN', 300),
    ('OUT', 25)
]

movement_list = build_movement_list(movements)
final_inventory_change = process_movements(movement_list)
print(f'Result: {final_inventory_change}')