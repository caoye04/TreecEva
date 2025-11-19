from functools import reduce

def process_signal(initial_state, signal_value):
    states = {0, 1, 2}
    current_state = initial_state
    processed_signal = signal_value
    
    # State machine processing loop
    for i in range(5):
        if current_state == 0:
            processed_signal = processed_signal ^ (i << 1)
            current_state = 1 if processed_signal > 30 else 2
        elif current_state == 1:
            mask = reduce(lambda x, y: x | y, [1 << j for j in range(3) if j != i % 3], 0)
            processed_signal = (processed_signal & mask) >> 1
            current_state = 0 if processed_signal < 10 else 2
        else:  # current_state == 2
            processed_signal = (processed_signal + (i * 3)) & 0xFF
            comparison_result = processed_signal >= 50
            current_state = 1 if comparison_result else 0
            
        # Early termination condition
        if processed_signal == 0:
            break
    
    return processed_signal

# Initialize parameters
initial_conditions = [(1, 42), (2, 15), (0, 100)]
current_state, signal_value = initial_conditions[0]

# Apply signal processing
intermediate_result = process_signal(current_state, signal_value)

# Final transformation using set operations
active_bits = frozenset([i for i in range(8) if (intermediate_result >> i) & 1])
toggle_positions = {0, 2, 4, 6}
final_mask = reduce(lambda acc, pos: acc ^ (1 << pos), active_bits.intersection(toggle_positions), 0)
processed_signal = intermediate_result ^ final_mask

print(f"Result: {processed_signal}")