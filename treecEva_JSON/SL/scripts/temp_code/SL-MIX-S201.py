from math import gcd
from functools import reduce

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def compute_lcm_of_list(numbers):
    return reduce(lcm, numbers, 1)

# Batch IDs to process
batch_ids = [15, 21, 25, 28, 33, 35, 39, 49, 51, 55]

# Create linked list from batch IDs
head = None
for id_val in reversed(batch_ids):
    head = ListNode(id_val, head)

# State machine states
STATE_START = 0
STATE_CHECK_COMPOSITE = 1
STATE_CHECK_GCD = 2
STATE_VALID = 3
STATE_INVALID = 4

valid_ids = []
current = head

while current:
    batch_id = current.val
    state = STATE_START
    
    while state != STATE_VALID and state != STATE_INVALID:
        if state == STATE_START:
            # Check if composite (non-prime and > 1)
            if not is_prime(batch_id) and batch_id > 1:
                state = STATE_CHECK_COMPOSITE
            else:
                state = STATE_INVALID
        elif state == STATE_CHECK_COMPOSITE:
            # Check GCD with secret key 42
            if gcd(batch_id, 42) > 1:
                state = STATE_VALID
            else:
                state = STATE_INVALID
    
    if state == STATE_VALID:
        valid_ids.append(batch_id)
    
    current = current.next

# Calculate LCM of valid IDs
final_lcm = compute_lcm_of_list(valid_ids) if valid_ids else 0

print(f"Result: {final_lcm}")