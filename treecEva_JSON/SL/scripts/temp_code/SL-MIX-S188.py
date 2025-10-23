import heapq
from collections import deque

class TokenStream:
    def __init__(self, tokens):
        self.tokens = deque(tokens)
    
    def get_next(self):
        return self.tokens.popleft() if self.tokens else None

def hash_token(token):
    return hash(token) % 1000

def process_stream(token_list):
    stream = TokenStream(token_list)
    frequency_map = {}
    unique_hashes = frozenset()
    priority_queue = []
    
    while True:
        token = stream.get_next()
        if token is None:
            break
            
        # Update frequency map
        frequency_map[token] = frequency_map.get(token, 0) + 1
        
        # Add hash to unique set (frozenset is immutable, so we recreate)
        unique_hashes = unique_hashes.union({hash_token(token)})
    
    # Build priority queue with negative frequencies (min-heap simulation)
    for token, freq in frequency_map.items():
        heapq.heappush(priority_queue, (-freq, token))
    
    # Dictionary comprehension for token transformation mapping
    transform_map = {token: f"TRANSFORMED_{token}" for token, _ in priority_queue[:3]}
    
    # Calculate priority sum based on top 3 frequencies
    priority_sum = 0
    count = 0
    temp_queue = []
    
    while priority_queue and count < 3:
        neg_freq, token = heapq.heappop(priority_queue)
        priority_sum += (-neg_freq)  # Convert back to positive
        temp_queue.append((neg_freq, token))
        count += 1
    
    # Restore queue
    for item in temp_queue:
        heapq.heappush(priority_queue, item)
    
    return priority_sum

# Execution point Y
token_sequence = ['IF', 'VAR', 'IF', 'LOOP', 'VAR', 'IF', 'FUNC', 'LOOP', 'VAR', 'IF']
priority_sum = process_stream(token_sequence)
print(f"Result: {priority_sum}")