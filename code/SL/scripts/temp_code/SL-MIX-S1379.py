from collections import deque
import math

def signal_transform(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return math.floor(result * 100) if result > 0 else 0
    return wrapper

@signal_transform
def calculate_intensity(value, factor=1.5):
    return math.log(value) * factor

# Initialize packet data and processing queue
packet_data = [10, 20, 30, 40, 50]
processing_queue = deque(maxlen=3)
signal_window = deque([5, 15, 25], maxlen=3)
processed_signal_strength = 0

for idx, packet in enumerate(packet_data):
    # Apply logical filtering
    if packet >= 20 and (packet % 10 == 0):
        adjusted_packet = packet + (idx * 2)
        processing_queue.append(adjusted_packet)
    
    # Window-based processing using stack-like behavior
    if len(signal_window) == signal_window.maxlen:
        popped = signal_window.popleft()
        if popped > 10 or idx == len(packet_data) - 1:
            signal_window.append(packet)
    else:
        signal_window.append(packet)
    
    # Calculate intensity when queue is full
    if len(processing_queue) == processing_queue.maxlen:
        window_sum = sum(list(processing_queue)[-2:])
        intensity = calculate_intensity(window_sum / 2)
        processed_signal_strength += intensity
        processing_queue.clear()

# Final adjustment based on remaining signals
if signal_window:
    max_val = max(signal_window)
    processed_signal_strength ^= max_val

print(f"Result: {processed_signal_strength}")