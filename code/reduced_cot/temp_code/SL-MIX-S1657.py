from collections import deque
from functools import reduce

def apply_window_weight(pos, total_samples):
    # Hamming window function
    import math
    return 0.54 - 0.46 * math.cos(2 * math.pi * pos / (total_samples - 1))

def process_audio_samples(raw_samples, window_size):
    window_buffer = deque(maxlen=window_size)
    weighted_sum = 0.0
    
    for idx, sample in enumerate(raw_samples):
        window_buffer.append(sample)
        
        # Only process when window is full
        if len(window_buffer) == window_size:
            # Apply weights based on position in window
            weights = [apply_window_weight(i, window_size) for i in range(window_size)]
            weighted_values = [samp * weight for samp, weight in zip(window_buffer, weights)]
            current_window_sum = sum(weighted_values)
            
            # Update weighted sum using modular arithmetic to prevent overflow
            weighted_sum = (weighted_sum + current_window_sum) % 997
        
        # Early termination condition based on signal characteristics
        if idx > 5 and abs(sample) < 0.01:
            break_condition = True if reduce(lambda x, y: x and y, [abs(s) < 0.1 for s in list(window_buffer)[-3:]]) else False
            weighted_sum = weighted_sum * 2 if break_condition else weighted_sum
    
    # Final normalization and adjustment
    final_adjustment = 1.5 if weighted_sum > 500 else 0.8
    processed_signal_strength = int(weighted_sum * final_adjustment) % 1009
    
    return processed_signal_strength

# Audio samples from a digital signal
audio_data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.05, 0.02, 0.01, 0.005]
window_length = 5

result = process_audio_samples(audio_data, window_length)
print(f"Result: {result}")