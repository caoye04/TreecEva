from functools import reduce

def process_signal_stream(input_stream):
    # Initialize DP table for signal optimization
    dp_table = [0] * (len(input_stream) + 1)
    
    # First pass: Apply bitwise modulation with previous element
    for idx in range(1, len(input_stream)):
        # Bitwise XOR with left shift and modular arithmetic
        modulated_val = ((input_stream[idx-1] << 2) ^ input_stream[idx]) % 17
        input_stream[idx] = modulated_val if modulated_val > 0 else input_stream[idx]
    
    # Second pass: Dynamic programming accumulation with ternary condition
    for i in range(1, len(dp_table)):
        raw_signal = input_stream[i-1]
        dp_table[i] = dp_table[i-1] + (raw_signal if raw_signal % 3 == 0 else -raw_signal)
    
    # Final aggregation using functional reduction
    aggregated = reduce(lambda acc, x: acc ^ (x << 1) if x & 1 else acc | x, input_stream, 0)
    
    # Logical filtering and sorting
    filtered_signals = sorted(filter(lambda s: s > 5 and s < 50, input_stream), reverse=True)
    
    # Compute final modulated signal using multiple operations
    modulated_signal = (dp_table[-1] & 0xFF) ^ (aggregated >> 2) if len(filtered_signals) > 3 else dp_table[-1] | aggregated
    
    return modulated_signal

# Input signal sequence
signals = [7, 14, 3, 9, 15, 6, 12, 8]
final_result = process_signal_stream(signals)
print(f"Result: {final_result}")