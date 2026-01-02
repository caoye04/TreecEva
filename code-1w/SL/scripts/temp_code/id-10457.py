from collections import defaultdict

# Simulate sensor readings with timestamps
timestamps = [100, 101, 102, 103, 104, 105, 106, 107]
raw_readings = [23.5, 24.1, 23.9, 24.0, 25.2, 25.8, 26.1, 25.9]

# Misleading auxiliary data (distractor)
system_flags = [0x0A, 0x0C, 0x08, 0x0F, 0x0B, 0x09, 0x0D, 0x0E]
flag_analysis = defaultdict(int)
for flag in system_flags:
    flag_analysis[flag & 0x07] += 1

# Process valid sensor data
processed_data = []
base_threshold = 24.0
adjustment_factor = 0.25

for i, reading in enumerate(raw_readings):
    if reading >= base_threshold:
        adjusted = reading - adjustment_factor
        processed_data.append(adjusted)

# Secondary filtering based on index parity (semi-relevant)
even_index_values = [v for i, v in enumerate(processed_data) if i % 2 == 0]

# Calculate moving average of processed data (not used in final result - distractor)
moving_avg = []
window_size = 2
for i in range(len(processed_data) - window_size + 1):
    window = processed_data[i:i + window_size]
    moving_avg.append(sum(window) / len(window))

# Noise correction factor from bitwise analysis (distractor)
total_noise = 0
for val in raw_readings:
    shifted = int(val * 10) ^ 0xFF
    total_noise += (shifted & 0x0F)

# Core calculation function
def calculate_stability_index(data):
    diffs = []
    for a, b in zip(data, data[1:]):
        diffs.append(abs(a - b))
    return sum(diffs) / len(diffs) if diffs else 0.0

# Auxiliary statistic (not directly used)
mean_value = sum(processed_data) / len(processed_data) if processed_data else 0

# Main scoring logic
def calculate_final_score(data):
    if not data:
        return 0
    
    # Step 1: Base score from sum
    base_score = sum(x * 10 for x in data)
    
    # Step 2: Apply stability penalty
    stability = calculate_stability_index(data)
    penalty = int(stability * 20)
    
    # Step 3: Adjust using modular pattern
    length_mod = len(data) % 4
    if length_mod > 0:
        base_score = base_score // length_mod
    
    # Step 4: Final adjustment using index sum
    index_weight = sum(i * i for i in range(len(data)))
    final = base_score - penalty + (index_weight % 25)
    
    return final

# Execute main computation
intermediate_flag = sum(system_flags) % 100  # Red herring
normalization_constant = 1.0  # Unused parameter (distractor)

final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")