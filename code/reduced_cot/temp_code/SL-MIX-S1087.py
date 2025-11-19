def process_audio_filter(stages, initial_values):
    if stages <= 0:
        return initial_values[0] if initial_values else 0
    
    # Compute transformed values using list comprehension and bitwise operations
    transformed = [((val << 1) & 0xFF) | (val >> 2) for val in initial_values]
    
    # Apply recursive filter with logical conditions
    if stages % 2 == 0:
        next_values = [
            (transformed[i] + transformed[(i+1) % len(transformed)]) & 0xFF
            for i in range(len(transformed))
            if transformed[i] > 0x40
        ]
    else:
        next_values = [
            (transformed[i] ^ transformed[(i+2) % len(transformed)]) & 0xFF
            for i in range(len(transformed))
            if (transformed[i] & 0xF0) != 0
        ]
    
    # Recursive call with modified parameters
    return process_audio_filter(stages - 1, next_values)

# Initialize filter parameters
filter_stages = 4
initial_signal = [0x15, 0x3C, 0x7A, 0xB6, 0xE9]

# Process through all filter stages
processed_signal = process_audio_filter(filter_stages, initial_signal)

# Calculate final signal strength with floating point operations
signal_components = [((x & 0xF) * 1.5) + ((x >> 4) * 0.75) for x in [processed_signal]]
final_signal_strength = int(sum(signal_components) * 2) & 0xFF

print(f"Result: {final_signal_strength}")