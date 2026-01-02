import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [1.2, 3.7, 2.5, 8.9, 4.6, 7.1, 6.3, 9.0, 5.4, 3.3, 8.8, 1.1, 7.7]
    offset = 0.5
    adjusted = [x + offset for x in raw]
    return adjusted

def is_spike(val, prev, threshold=1.5):
    return abs(val - prev) > threshold

# Irrelevant helper (distractor)
def smooth_signal(data):
    if len(data) < 3:
        return data
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        window_avg = (data[i-1] + data[i] + data[i+1]) / 3
        smoothed.append(window_avg)
    smoothed.append(data[-1])
    return smoothed  # Never used

def detect_anomalies(sequence):
    flags = []
    for i in range(1, len(sequence)):
        if sequence[i] > 7.0 and is_spike(sequence[i], sequence[i-1]):
            flags.append(i)
    # Dead code path (misleading)
    temp_result = sum([sequence[j]**2 for j in flags if j % 2 == 0])
    temp_result *= 0.0  # Neutralized
    return flags

# Complex filtering with slicing
def filter_by_range(data, low=4.0, high=8.5):
    sorted_data = sorted(data)
    mid_slice = sorted_data[2:-2]  # Remove extremes using slicing
    return [x for x in mid_slice if low <= x <= high]

# Red herring function (not part of critical path)
def compute_entropy(vals):
    total = sum(vals)
    probs = [v / total for v in vals]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 4)

# Core logic disguised among distractions
def analyze_pattern(seq, limit):
    accumulated = 0
    factor = 1.0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            accumulated += val * 1.1
        else:
            accumulated -= val * 0.9
    # Introduce bit manipulation red herring
    binary_tag = bin(hash('diagnostic'))
    tag_value = len(binary_tag)
    # Decoy transformation
    decoy_shift = tag_value << 2
    decoy_shift %= 100
    # Actual answer computation
    base_score = abs(accumulated)
    adjustment = math.sin(math.pi * len(seq) / 4)
    final_score = base_score + adjustment + decoy_shift * 0.0  # Ignore decoy
    return int(round(final_score))

# Main execution with multiple irrelevant steps
readings = collect_readings()
spike_indices = detect_anomalies(readings)

# Unused sorting variant (distraction)
sorted_asc = sorted(readings)
sorted_desc = sorted(readings, reverse=True)

# Use only middle portion via slicing
working_set = readings[1:-1]

# Apply filter to get relevant diagnostic window
filtered_sequence = filter_by_range(working_set, low=4.2, high=8.7)

# Dummy statistical check (irrelevant)
mean_val = sum(filtered_sequence) / len(filtered_sequence)
variance = sum((x - mean_val)**2 for x in filtered_sequence) / len(filtered_sequence)

threshold = 5.5

# Critical statement
final_diagnostic = analyze_pattern(filtered_sequence, threshold)

# Another decoy: matrix-like structure (unused)
grid = [[i + j for j in range(3)] for i in range(3)]

# Print required result
print(f"Result: {final_diagnostic}")