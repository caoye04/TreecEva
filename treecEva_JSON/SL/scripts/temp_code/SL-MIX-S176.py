import heapq
import base64
from collections import deque

def call_tracker(func):
    calls = []
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        calls.append(result)
        return result
    wrapper.calls = calls
    return wrapper

class ResourcePool:
    def __init__(self, resources):
        self.resources = resources
        self.active = []
    
    def __enter__(self):
        self.active = list(self.resources)
        return self.active
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.active.clear()

@call_tracker
def encode_message(msg):
    return base64.b64encode(msg.encode()).decode()

@call_tracker
def decode_message(encoded_msg):
    return base64.b64decode(encoded_msg).decode()

messages = ['alpha', 'beta', 'gamma', 'delta']
priorities = [3, 1, 4, 2]
heap = list(zip(priorities, messages))
heapq.heapify(heap)

processing_stack = []
output_queue = deque()

with ResourcePool([1, 2, 3]) as pool:
    while heap:
        priority, msg = heapq.heappop(heap)
        encoded = encode_message(msg)
        processing_stack.append((priority, encoded))
    
    while processing_stack:
        priority, encoded = processing_stack.pop()
        decoded = decode_message(encoded)
        output_queue.appendleft((priority, decoded))
    
    checksum_components = []
    while output_queue:
        priority, text = output_queue.popleft()
        text_hash = hash(text) % 1000
        checksum_components.append(text_hash ^ priority)
    
    final_checksum = sum(checksum_components) & 0xFF

print(f"Result: {final_checksum}")