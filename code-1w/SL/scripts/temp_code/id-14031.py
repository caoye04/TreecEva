def analyze_system_state(inputs):
    state_flags = {}
    temp_accumulator = 0
    
    for i, val in enumerate(inputs):
        if i % 2 == 0:
            temp_accumulator += val ** 2
        else:
            temp_accumulator -= val

    normalized_val = temp_accumulator / len(inputs) if inputs else 0

    intermediate_results = []
    for x in inputs:
        shifted = (x << 1) & 7  # Bitwise: left shift and mask
        intermediate_results.append(shifted)

    # Irrelevant transformation
    dummy_map = {i: x ^ 3 for i, x in enumerate(intermediate_results)}
    unused_sum = sum(dummy_map.values()) * 0.1

    return temp_accumulator


def transform_sequence(seq):
    paired = zip(seq[::2], seq[1::2])
    transformed = []
    for a, b in paired:
        transformed.append(a + b * 2)
    
    # Dead code path - never used
    if len(transformed) > 100:
        transformed = [x for x in transformed if x % 2 == 0]
        
    return transformed


def calculate_net_flux(data):
    base_total = 0
    adjustment_factor = 1.5
    
    index_offset = 0
    for idx, item in enumerate(data):
        if idx % 3 == 0:
            base_total += item * adjustment_factor
        elif idx % 3 == 1:
            base_total += item // 2
        else:
            base_total -= item & 5  # Bitwise AND with constant

    # Simulate auxiliary tracking (unused)
    status_log = {}
    for step in range(3):
        status_log[f'step_{step}'] = base_total + step * 2

    final_adjustment = len(data) % 4
    return int(base_total - final_adjustment)

# Main execution
raw_input_stream = [12, 7, 3, 9, 4, 8, 2]

initial_diagnostic = analyze_system_state(raw_input_stream)
dummy_tracker = [x for x in raw_input_stream if x > 5]
processed_data = transform_sequence(raw_input_stream)

# Key computation point
final_flux = calculate_net_flux(processed_data)

print(f"Result: {final_flux}")