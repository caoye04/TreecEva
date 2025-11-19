from collections import deque
import itertools

def signal_transformer():
    # Initialize data structures
    frequency_stack = [10, 20, 30]
    packet_queue = deque([1, 2, 3, 4])
    
    # Lambda functions for signal processing
    amplify = lambda x, y: x * y if x > 0 else x + y
    attenuate = lambda x, y: x // y if y != 0 and x >= y else x - y
    
    # Process packets using queue
    while packet_queue:
        packet = packet_queue.popleft()
        if packet % 2 == 0 and frequency_stack:  # Short-circuit evaluation
            freq = frequency_stack.pop()
            adjusted_freq = amplify(freq, packet)
            frequency_stack.append(adjusted_freq)
        elif frequency_stack:
            freq = frequency_stack.pop()
            adjusted_freq = attenuate(freq, packet)
            frequency_stack.append(adjusted_freq)
    
    # Calculate final signal strength
    processed_signal_strength = 0
    while frequency_stack:
        value = frequency_stack.pop()
        processed_signal_strength += value if value > 10 else 0  # Comparison operation
    
    return processed_signal_strength

# Execute the signal processing
result = signal_transformer()
print(f"Result: {result}")