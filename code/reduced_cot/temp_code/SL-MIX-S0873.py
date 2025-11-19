class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generate_fibonacci_sequence(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

from collections import defaultdict
from itertools import combinations
from functools import reduce
import operator

def validate_access_sequence(head):
    # Extract values from linked list
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    # Count frequency of each value
    freq_map = defaultdict(int)
    for val in values:
        freq_map[val] += 1
    
    # Generate all pairs of distinct values
    unique_values = list(freq_map.keys())
    pairs = list(combinations(unique_values, 2))
    
    # Calculate product of frequencies for each pair
    products = []
    for a, b in pairs:
        products.append(freq_map[a] * freq_map[b])
    
    # If no pairs, return 0
    if not products:
        return 0
    
    # Compute the alternating sum: products[0] - products[1] + products[2] - ...
    alternating_sum = reduce(operator.add, [products[i] if i % 2 == 0 else -products[i] for i in range(len(products))])
    
    return alternating_sum

# Main execution
if __name__ == "__main__":
    # Generate Fibonacci sequence for timestamps
    fib_timestamps = generate_fibonacci_sequence(8)
    
    # Create linked list with repeated timestamps to simulate access pattern
    access_pattern = [fib_timestamps[i%len(fib_timestamps)] for i in range(12)]
    linked_list_head = create_linked_list(access_pattern)
    
    # Validate the access sequence
    final_validation_score = validate_access_sequence(linked_list_head)
    print(f"Result: {final_validation_score}")