from collections import deque
import math

def encode_char(c):
    ascii_val = ord(c)
    return float(ascii_val) * 0.75 + 12.5

def process_signal(signal_chars):
    # Encode characters
    encoded_values = [encode_char(c) for c in signal_chars]
    
    # Initialize data structures
    buffer_queue = deque()
    reversal_stack = []
    
    # Distribute values between queue and stack
    for i, val in enumerate(encoded_values):
        if i % 2 == 0:
            buffer_queue.append(val)
        else:
            reversal_stack.append(val)
    
    # Perform stack reversal
    reversed_values = []
    while reversal_stack:
        reversed_values.append(reversal_stack.pop())
    
    # Process buffered values with reversed values
    processed_results = []
    while buffer_queue:
        buf_val = buffer_queue.popleft()
        if reversed_values:
            rev_val = reversed_values.pop(0)
            # Arithmetic computation combining values
            combined = (buf_val * 1.5 - rev_val) / 2.0
            processed_results.append(combined)
        else:
            processed_results.append(buf_val * 0.5)
    
    # Final aggregation using floating point operations
    aggregated_sum = sum(processed_results)
    normalized_value = aggregated_sum / len(processed_results)
    
    # Apply logarithmic scaling
    if normalized_value > 0:
        final_signal_strength = math.log(normalized_value) * 10
    else:
        final_signal_strength = 0.0
    
    return final_signal_strength

# Signal processing
input_signal = "PYTH"
final_signal_strength = process_signal(input_signal)
print(f"Result: {final_signal_strength}")