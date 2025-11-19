import heapq

class TokenNode:
    def __init__(self, token, next_node=None):
        self.token = token
        self.next = next_node

def compute_custom_hash(s):
    hash_val = 0
    for char in s:
        hash_val = (hash_val * 31 + ord(char)) & 0xFFFFFFFF
    return hash_val

tokens = ['alpha', 'beta', 'gamma', 'delta']
head = None
for token in reversed(tokens):
    head = TokenNode(token, head)

priority_queue = []
current = head
index = 0
while current:
    h = compute_custom_hash(current.token)
    masked_h = h & 0xFF
    shifted = masked_h << (index % 6)
    heapq.heappush(priority_queue, (shifted ^ 0xAA))
    current = current.next
    index += 1

aggregate_score = 0
while priority_queue:
    val = heapq.heappop(priority_queue)
    transformed = (val ^ 0x55) & 0xFF
    aggregate_score += (transformed * (aggregate_score & 0xF)) + 1

print(f"Result: {aggregate_score}")