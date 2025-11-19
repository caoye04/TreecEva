from functools import reduce

def simulate_circuit(initial_signal):
    # Stage 1: Apply mask using bitwise AND
    masked_signal = initial_signal & 0xFF  # Keep only lower 8 bits
    
    # Stage 2: XOR with a pattern
    xor_pattern = 0b10101010
    xored_signal = masked_signal ^ xor_pattern
    
    # Stage 3: Left shift by 2 positions
    shifted_signal = xored_signal << 2
    
    # Stage 4: Apply another mask
    second_mask = 0x3FF  # Keep only lower 10 bits
    masked_shifted = shifted_signal & second_mask
    
    # Stage 5: Combine with original using OR
    combined_signal = masked_shifted | (initial_signal & 0xF00)
    
    return combined_signal

def process_signals(signals):
    # Apply simulation to each signal and collect results
    simulated = list(map(simulate_circuit, signals))
    
    # Filter out signals that are above threshold after simulation
    threshold = 500
    filtered_signals = list(filter(lambda x: x <= threshold, simulated))
    
    # Reduce using XOR to get final combined value
    if filtered_signals:
        final_value = reduce(lambda a, b: a ^ b, filtered_signals)
    else:
        final_value = 0
    
    return final_value

# Main execution
input_signals = [123, 456, 789, 234, 567]
processed_signal = process_signals(input_signals)
print(f"Result: {processed_signal}")