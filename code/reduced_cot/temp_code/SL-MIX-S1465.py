import heapq
import math
from collections import deque

def process_cosmic_signals(frequency_data):
    signal_queue = deque(frequency_data)
    signal_stack = []
    priority_heap = []
    
    # Phase 1: Queue to Stack transformation with bitwise operations
    while signal_queue:
        freq = signal_queue.popleft()
        transformed_freq = freq ^ (freq << 1) & 0xFF
        signal_stack.append(transformed_freq)
    
    # Phase 2: Stack to Heap with logarithmic scaling
    while signal_stack:
        val = signal_stack.pop()
        if val > 0:
            scaled_val = int(math.log(val) * 100) if val > 1 else 0
            heapq.heappush(priority_heap, scaled_val)
    
    # Phase 3: Recursive heap processing
    def recursive_processor(heap, depth=0):
        if not heap or depth >= 3:
            return 0
        min_val = heapq.heappop(heap)
        if min_val % 2 == 0:
            return min_val + recursive_processor(heap, depth + 1)
        else:
            heapq.heappush(heap, min_val * 2)
            return recursive_processor(heap, depth + 1)
    
    return recursive_processor(priority_heap)

cosmic_frequencies = [12, 28, 9, 45, 33, 16]
cosmic_signature = process_cosmic_signals(cosmic_frequencies)
print(f"Result: {cosmic_signature}")