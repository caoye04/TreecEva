import collections
import math

def process_signals(initial_queue):
    processed_values = []
    while initial_queue:
        val = initial_queue.popleft()
        # Apply transformation based on parity
        transformed = (val << 1) if val % 2 == 0 else (val >> 1)
        processed_values.append(transformed)
    return processed_values

def calculate_strength(values):
    # Dictionary comprehension for squared values
    squares = {i: v**2 for i, v in enumerate(values)}
    # Sum of squares with alternating signs
    total = sum((-1)**i * s for i, s in squares.items())
    # Ternary operator for threshold application
    adjusted = total if total > 0 else abs(total) + 10
    return adjusted

def simulate_circuit(input_signals):
    signal_queue = collections.deque(input_signals)
    stage1_results = process_signals(signal_queue)
    
    # Nested loop for secondary processing
    enhanced_signals = []
    for base_val in stage1_results:
        sub_vals = [base_val + i for i in range(3)]
        for sv in sub_vals:
            # Bitwise AND with mask
            masked = sv & 0xF  
            enhanced_signals.append(masked)
    
    return calculate_strength(enhanced_signals)

# Initial input signals
input_signals = [7, 2, 9, 4]
final_signal_strength = simulate_circuit(input_signals)
print(f"Result: {final_signal_strength}")