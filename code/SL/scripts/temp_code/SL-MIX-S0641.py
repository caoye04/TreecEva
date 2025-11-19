import math
from collections import deque

def process_signals():
    signal_queue = deque([12, 7, 23, 45, 8])
    operation_stack = []
    accumulator = 0
    
    # Load operations into stack
    ops = [
        lambda x: math.log(x + 1),
        lambda x: x ** 1.5,
        lambda x: int(x) & 0xFF,
        lambda x: math.exp(x / 10)
    ]
    
    operation_stack.extend(ops)
    
    while signal_queue and operation_stack:
        signal = signal_queue.popleft()
        operation = operation_stack.pop()
        transformed = operation(signal)
        accumulator += transformed
    
    # Apply final correction using remaining signals
    while signal_queue:
        accumulator += math.sqrt(signal_queue.popleft())
    
    return accumulator

# Main execution
final_energy = process_signals()
print(f"Result: {int(final_energy * 1000) // 10}")