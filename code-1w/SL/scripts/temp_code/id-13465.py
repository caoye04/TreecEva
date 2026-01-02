import math

def preprocess_sensors(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    baseline = sum(filtered) / len(filtered)
    adjusted = [math.log(val) - math.log(baseline) for val in filtered]
    return adjusted

def generate_frequency_map(values):
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    return freq_map

def analyze_pattern(sequence):
    pattern_score = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0 and val > 0:
            pattern_score += math.sqrt(abs(val)) * i
    return pattern_score

def calculate_thermal_response(data_grid):
    flat_data = [item for row in data_grid for item in row]
    
    # Irrelevant preprocessing (distractor)
    sensor_log = preprocess_sensors(flat_data)
    frequency_lookup = generate_frequency_map(flat_data)
    
    # Misleading intermediate calculation (dead path)
    temp_offset = 0
    for k, v in frequency_lookup.items():
        if v > 1:
            temp_offset += math.sin(k)  # Not used later
    
    # Real computation begins
    valid_entries = [x for x in flat_data if x % 2 == 1]  # Only odd values matter
    amplified = [x * (2 ** int(math.log2(x))) for x in valid_entries if x >= 4]
    
    # Use of enumerate and conditional expression
    weighted_sum = 0
    for idx, value in enumerate(amplified):
        multiplier = idx + 1 if value > 10 else 1
        weighted_sum += value * multiplier
    
    # Core result
    thermal_index = sum(amplified) // (len(amplified) or 1)
    
    # Additional distraction: unused recursion
    def recursive_dampen(n):
        if n <= 1:
            return 1
        return n * recursive_dampen(n - 2)
    
    dummy_trace = recursive_dampen(5)  # Computationally irrelevant
    
    # Final answer derived here
    thermal_capacity = thermal_index + len(valid_entries)
    
    # This print is required
    print(f"Result: {thermal_capacity}")
    return thermal_capacity

# Main execution
grid_data = [
    [4, 8, 5],
    [3, 6, 9],
    [7, 4, 2]
]

thermal_capacity = calculate_thermal_response(grid_data)