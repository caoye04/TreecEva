from functools import reduce

def analyze_waveform(amplitude_values):
    transformations = [
        lambda x: x * 2 if x % 3 == 0 else x,
        lambda x: x + 5 if x % 3 == 1 else x,
        lambda x: x - 3 if x % 3 == 2 else x
    ]
    
    # Apply transformations greedily based on maximizing signal strength
    processed_values = []
    for val in amplitude_values:
        best_transform = max(transformations, key=lambda f: f(val))
        processed_values.append(best_transform(val))
    
    # Calculate cumulative signal strength using modular arithmetic
    cumulative_strength = 0
    for i, val in enumerate(processed_values):
        cumulative_strength = (cumulative_strength + val * (i + 1)) % 1000
    
    return cumulative_strength

# Audio waveform amplitude measurements
waveform_data = [14, 27, 8, 33, 19, 42, 5, 36]

# Process the waveform data
processed_signal_strength = analyze_waveform(waveform_data)
print(f"Result: {processed_signal_strength}")