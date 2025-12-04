import itertools

def calculate_noise_level(frequencies):
    # This calculates the noise level in a communication channel
    noise = 0
    for freq in frequencies:
        if freq % 3 == 0:
            noise += freq * 2
        elif freq % 5 == 0:
            noise -= freq // 2
    return abs(noise)

def calculate_signal_strength(frequencies):
    # Extract only the relevant frequencies and compute strength
    strength = 0
    for i, freq in enumerate(frequencies):
        if i % 2 == 0:  # Only even indices matter for signal strength
            strength += freq
    return strength

def apply_filters(data, threshold):
    # Apply various filters to the frequency data
    filtered = []
    interference_map = {}
    
    # Initialize interference map - not used in final calculation
    for i in range(1, 10):
        interference_map[i] = i * i - 3
    
    # First filter pass - irrelevant for final result
    preliminary = [x for x in data if x > threshold // 2]
    
    # Main filtering logic
    for value in data:
        if value > threshold and value % 2 == 1:
            filtered.append(value)
    
    return filtered

# Main processing logic
raw_frequencies = [15, 7, 22, 11, 30, 9, 18, 27, 13, 21, 16, 25]
sorted_frequencies = sorted(raw_frequencies)

# Calculate potential signal combinations - distraction
potential_combos = list(itertools.combinations(sorted_frequencies[:4], 2))
potential_strength = sum(x[0] + x[1] for x in potential_combos)

# Apply threshold filtering
base_threshold = 10
adjusted_threshold = base_threshold + (len(raw_frequencies) % 5)
filtered_frequencies = apply_filters(raw_frequencies, adjusted_threshold)

# Calculate noise metrics - distraction
noise_level = calculate_noise_level(sorted_frequencies)
modulation_factor = (noise_level % 10) + 1

# This is our main target calculation
actual_signal_strength = calculate_signal_strength(filtered_frequencies)

# Additional processing - not relevant to final answer
if noise_level > 100:
    signal_quality = "Low"
    corrected_signal = actual_signal_strength // 2
elif noise_level > 50:
    signal_quality = "Medium"
    corrected_signal = actual_signal_strength - 5
else:
    signal_quality = "High"
    corrected_signal = actual_signal_strength

# More distractions
complex_metric = [x & modulation_factor for x in filtered_frequencies]
reduced_metric = sum(complex_metric) ^ noise_level

print(f"Result: {actual_signal_strength}")