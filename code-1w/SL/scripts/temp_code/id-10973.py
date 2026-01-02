def transform_signal(raw_values, scaling_factor=1.5):
    # Irrelevant transformation used nowhere
    return [x * scaling_factor for x in raw_values if x > 0]

# Simulated sensor array data (some valid, some decoy)
sensor_a_readings = [12, -5, 8, 0, 21, 33, -44, 18]
sensor_b_readings = [9, 14, 6, 25, 11, 30, 7, 22]
sensor_c_readings = [3, 8, 13, 18, 23, 28, 33, 38]  # Arithmetic progression - red herring

# Unused signal processing functions
def apply_filter(data, mode='lowpass'):
    return [x for i, x in enumerate(data) if i % 2 == 0]

def compute_envelope(signal):
    return max(signal) - min(signal)

# Real processing begins here
raw_data = sensor_a_readings[:6]  # Slice: [12, -5, 8, 0, 21, 33]
offset = 5
calibrated = [x + offset for x in raw_data]  # [17, 0, 13, 5, 26, 38]

def normalize(readings):
    min_val, max_val = min(readings), max(readings)
    if min_val == max_val:
        return [0.5] * len(readings)
    return [(x - min_val) / (max_val - min_val) for x in readings]

normalized_data = normalize(calibrated)  # Transformed to [0.421, 0.0, 0.342, 0.105, 0.578, 1.0]

def segment_signal(signal, parts=3):
    size = len(signal)
    step = size // parts
    return [signal[i:i+step] for i in range(0, size, step)]

segments = segment_signal(normalized_data, 3)  # [[0.421, 0.0], [0.342, 0.105], [0.578, 1.0]]

# Decoy clustering logic (never called)
def cluster_anomalies(data_list, eps=0.5):
    clusters = {}
    for i, val in enumerate(data_list):
        assigned = False
        for key in clusters:
            if abs(val - key) < eps:
                clusters[key].append(val)
                assigned = True
                break
        if not assigned:
            clusters[val] = [val]
    return clusters

# Threshold configuration map (used later)
threshold_map = {
    'critical': 0.9,
    'warning': 0.6,
    'normal': 0.3
}

# Auxiliary counting function with early returns
def count_exceedances(values, ref_map):
    above_critical = 0
    above_warning = 0
    for v in values:
        if v > ref_map['critical']:
            above_critical += 1
        elif v > ref_map['warning']:
            above_warning += 1
    return above_critical * 100 + above_warning * 10

# Data reconstruction via slicing and filtering
reconstructed = []
for seg in segments:
    if len(seg) > 1:
        reconstructed.extend(seg[1:])  # Takes [0.0, 0.105, 1.0]

# Misleading entropy calculation (unused)
import math
def compute_entropy(arr):
    from collections import Counter
    counts = Counter([round(x, 1) for x in arr])
    total = sum(counts.values())
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# This function looks complex but is unused
def generate_synthetic_data(base, depth=2):
    result = base[:]
    for _ in range(depth):
        result = [result[i] + result[-i-1] for i in range(len(result))]
    return result

# Processed data that feeds into final analysis
processed_data = [round(x * 1000) for x in reconstructed]  # [0.0 -> 0, 0.105 -> 105, 1.0 -> 1000] => [0, 105, 1000]

# Final diagnostic engine
def analyze_readings(readings, limits):
    total_impulse = 0
    spike_count = 0
    for val in readings:
        if val > 500:
            spike_count += 1
        if val % 25 == 0 and val > 0:  # Divisible by 25 and positive
            total_impulse += val // 10
    
    # Secondary check: presence of high-magnitude events
    critical_events = [v for v in readings if v > limits['critical'] * 1000]
    event_bonus = len(critical_events) * 50
    
    # Tertiary: pattern detection in digit sums
    digit_sum = sum(int(d) for num in readings for d in str(abs(num)))
    if digit_sum > 20:
        event_bonus += 25
    
    return spike_count * 100 + total_impulse + event_bonus

final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")