class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ChecksumTracker:
    def __init__(self):
        self.intermediates = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def record(self, value):
        self.intermediates.append(value)

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def divide_and_process(node, tracker):
    if not node:
        return frozenset()
    
    if not node.next:  # Base case: single node
        # Transform node value using logical operations
        transformed = (node.val & 0xF) | ((node.val >> 4) & 0xF) if node.val > 0 else node.val
        tracker.record(transformed)
        return frozenset([transformed])
    
    # Divide the list
    slow = fast = node
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Split into two halves
    prev.next = None
    
    # Conquer: process both halves
    left_set = divide_and_process(node, tracker)
    right_set = divide_and_process(slow, tracker)
    
    # Combine results with set operations
    combined = left_set.union(right_set)
    
    # Apply checksum logic: XOR all elements, then apply mask
    xor_result = 0
    for item in combined:
        xor_result ^= item
    
    masked = xor_result & 0xFF
    tracker.record(masked)
    return frozenset([masked])

# Main execution
message_blocks = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]
head = build_linked_list(message_blocks)

with ChecksumTracker() as tracker:
    result_set = divide_and_process(head, tracker)
    # Final checksum calculation
    checksum_result = sum(tracker.intermediates) % 256

print(f"Result: {checksum_result}")