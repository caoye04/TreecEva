import math

# Simulated sensor array data (irrelevant in part)
sensor_ids = [f'SEN-{i}' for i in range(1, 20)]
activation_log = {sid: False for sid in sensor_ids}

def generate_baseline(n):
    return [math.sin(i * 0.1) + 0.5 for i in range(n)]

def corrupt_signal(data, factor=0.1):
    return [x + factor * math.cos(x * 10) for x in data]  # Distraction

def filter_outliers(data, limit=3):
    mean_val = sum(data) / len(data)
    stdev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= limit * stdev]

# Irrelevant transformation chain
temp_snapshot = generate_baseline(50)
corrupted = corrupt_signal(temp_snapshot, 0.15)
filtered_snapshot = filter_outliers(corrupted)

# Core signal processing (relevant)
raw_input_signal = [i * i - 3 * i + 2 for i in range(1, 101)]  # Quadratic signal

# Noise injection and masking (partially irrelevant)
mask_sequence = [(i % 7 == 0) - (i % 5 == 0) for i in range(100)]
masked_signal = [raw_input_signal[i] if mask_sequence[i] >= 0 else 0 for i in range(100)]

# Redundant smoothing pass
smoothed = []
for i in range(len(masked_signal)):
    window = masked_signal[max(0, i-2):min(i+3, len(masked_signal))]
    smoothed.append(sum(window) / len(window))

# Decoy analysis function
def evaluate_coherence(signal):
    if not signal:
        return 0.0
    diffs = [abs(signal[i] - signal[i-1]) for i in range(1, len(signal))]
    return sum(diffs) / len(diffs) if diffs else 0.0

def compute_entropy(signal):
    from collections import Counter
    counts = Counter([round(x, 1) for x in signal])
    total = sum(counts.values())
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

# Unused entropy result (distractor)
entropy_diagnostic = compute_entropy(smoothed)

# Threshold mapping for diagnostic levels (critical)
threshold_map = {
    'level_1': 10,
    'level_2': 25,
    'level_3': 40,
    'level_4': 60
}

# Signal processor with conditional logic and list comprehension
processed_data = [
    x * 1.5 if x > threshold_map['level_2'] else \
    (x * 0.8 if x > threshold_map['level_1'] else x * 0.5)
    for x in smoothed if x > 0
]

# Early exit simulation (red herring)
if len(processed_data) < 50:
    final_diagnostic = -999
else:
    # Real computation path
    avg_power = sum(x ** 2 for x in processed_data) / len(processed_data)
    peak_value = max(processed_data)
    
    # Conditional expression with nested logic
    safety_factor = 1.0 if peak_value < 70 else (0.85 if peak_value < 85 else 0.6)
    
    # Diagnostic based on power and thresholds
    base_score = avg_power * safety_factor
    
    # Multiple comparisons and adjustment steps
    adjustment = 0
    if base_score > threshold_map['level_4']:
        adjustment += 12
    elif base_score > threshold_map['level_3']:
        adjustment += 8
    elif base_score > threshold_map['level_2']:
        adjustment += 5
    else:
        adjustment += 2
    
    # Final transformation using dictionary lookup and arithmetic
    modifier = {
        2: 0.9,
        5: 1.1,
        8: 1.25,
        12: 1.4
    }[adjustment]
    
    # Key statement
    final_diagnostic = int(base_score * modifier)

Result: {final_diagnostic}