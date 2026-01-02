import itertools

# Simulated sensor data processing with noise filtering and pattern analysis
def generate_sensor_stream(base_signal, noise_level=0.1):
    return [x + noise_level * (i % 3 - 1) for i, x in enumerate(base_signal)]

# Irrelevant helper: computes moving average but not used in final path
def moving_average(data, window=3):
    return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]

# Distraction function: calculates entropy but unused
def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    return -sum((count/total) * (count/total).__log__() for count in counts.values())

# Transform data using bit manipulation and arithmetic shifts (relevant)
def apply_fourier_mask(data):
    masked = []
    for i, val in enumerate(data):
        shifted = (val * 100) >> 2
        masked.append(int(shifted ^ (i & 7)))
    return masked

# Unused decoy function that looks important
def normalize_range(data, min_val=0, max_val=1):
    actual_min, actual_max = min(data), max(data)
    return [(x - actual_min) / (actual_max - actual_min) for x in data]

# Core transformation: applies conditional logic and list comprehension (used)
def refine_readings(data, tolerance=5):
    adjusted = [
        x + (1 if (x & 1) else -1) * 0.5
        for x in data
        if abs(x - round(x)) < tolerance
    ]
    # Dead code branch — never executed due to tolerance > 1
    if tolerance < 0.1:
        adjusted = [round(x, 2) for x in adjusted]
    return adjusted

# Main analysis function (critical path)
def analyze_pattern(seq, limit):
    score = 0
    for i, group in enumerate(itertools.groupby(seq, key=lambda x: x > limit)):
        length = len(list(group[1]))
        if group[0]:  # Only above-threshold segments
            score += length * (i + 1)
    return score if score > 0 else 117

# Decoy statistical summary (never called)
def summarize_statistics(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return {'mean': mean_val, 'variance': variance}

# Initialization of various irrelevant parameters
sampling_rate = 44100
calibration_offset = 0.003
buffer_size = 1024
unused_flag = False
scaling_factor = 1.0

# Generate base signal (real input)
signal_template = [0.1, 0.3, 0.6, 0.8, 1.0, 0.9, 0.5, 0.2, 0.1]
sensor_data = generate_sensor_stream(signal_template * 5, noise_level=0.05)

# Apply relevant transformation chain
temp_filtered = [round(x, 1) for x in sensor_data]  # Clean small floating point errors
transformed_data = apply_fourier_mask(temp_filtered)

# Red herring: this creates a variable that looks important but is unused
denoised_spectrum = moving_average(transformed_data, window=2) if len(transformed_data) > 2 else transformed_data

# Final refinement step (modifies data before analysis)
refined_data = refine_readings(transformed_data, tolerance=10)

# Threshold determined via dummy logic
threshold = sum(refined_data[:5]) // len(refined_data[:5]) if refined_data else 0

# Critical execution point
filtration_score = analyze_pattern(refined_data, threshold)

# Print result as required
print(f"Result: {filtration_score}")