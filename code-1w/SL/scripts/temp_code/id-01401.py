from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
data_packets = [
    {'id': 101, 'readings': [1.2, 1.5, 1.3, 1.7], 'status': 'OK', 'timestamp': 1623456780},
    {'id': 102, 'readings': [2.1, 1.9, 2.3, 2.0], 'status': 'OK', 'timestamp': 1623456785},
    {'id': 103, 'readings': [0.1, 0.05, 0.2, 0.15], 'status': 'ERROR', 'timestamp': 1623456790},
    {'id': 104, 'readings': [3.0, 3.1, 2.9, 3.2], 'status': 'OK', 'timestamp': 1623456795}
]

# Irrelevant auxiliary mapping (distractor)
status_codes = {'OK': 200, 'WARNING': 300, 'ERROR': 500, 'CRITICAL': 600}
diagnostic_map = defaultdict(lambda: 'UNKNOWN')
for code, desc in status_codes.items():
    diagnostic_map[code] = desc

# Misleading transformation chain (dead path)
def legacy_transform(x):
    return x * 1.05 + 0.5

def apply_filter(readings):
    # Real processing: smooth using moving average
    filtered = []
    for i in range(len(readings)):
        window = readings[max(0, i-1):min(i+2, len(readings))]
        filtered.append(sum(window) / len(window))
    return filtered

# Decoy function that looks important but isn't used in main flow
def deprecated_analysis(data):
    counts = Counter([len(p['readings']) for p in data])
    return sum(k * v for k, v in counts.items())

# Auxiliary statistical functions
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

# Signal normalization (used)
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    std_dev = math.sqrt(variance) if variance > 0 else 1.0
    return [(x - mean_val) / std_dev for x in signal]

# Data preprocessor with red herring logic
processed_data = []
error_count = 0
legacy_aggregate = 0.0  # Distractor accumulator

for packet in data_packets:
    if packet['status'] != 'OK':
        error_count += 1
        continue  # Skip bad packets

    raw_readings = packet['readings']
    
    # Apply real filter
    smoothed = apply_filter(raw_readings)
    
    # Compute irrelevant legacy metric (distraction)
    temp_legacy = [legacy_transform(x) for x in smoothed]
    legacy_aggregate += sum(temp_legacy)  # Accumulates meaningless value
    
    # Normalize the cleaned signal
    normalized = normalize_signal(smoothed)
    
    # Attach derived metadata (some fields unused later)
    processed_packet = {
        'packet_id': packet['id'],
        'cleaned': normalized,
        'magnitude': max(normalized) - min(normalized),
        'entropy': compute_entropy([abs(x) for x in normalized]),
        'timestamp': packet['timestamp']
    }
    processed_data.append(processed_packet)

# Unused aggregation (misleading intermediate result)
total_entropy = sum(p['entropy'] for p in processed_data)
avg_magnitude = sum(p['magnitude'] for p in processed_data) / len(processed_data)

# Core analysis function combining multiple concepts
def analyze_signal(data_list):
    # Extract all magnitudes
    magnitudes = [p['magnitude'] for p in data_list]
    
    # Use lambda for dynamic thresholding (actual logic)
    threshold_func = lambda mags: sum(mags) / len(mags) + 0.5
    dynamic_threshold = threshold_func(magnitudes)
    
    # Count how many exceed dynamic threshold
    count_above = sum(1 for m in magnitudes if m > dynamic_threshold)
    
    # Compute weighted score based on position (more recent = higher weight)
    weights = [math.exp(i * 0.1) for i in range(len(data_list))]
    weighted_sum = sum(m * w for m, w in zip(magnitudes, weights))
    
    # Final diagnostic combines count and weighted trend
    base_score = count_above * 100
    trend_adjustment = int(weighted_sum * 10)  # Amplify for integer effect
    
    # Dead branch: never taken due to data, but looks relevant
    if any(p['magnitude'] < 0 for p in data_list):
        base_score -= 50  # This will not execute
    
    # Real final computation
    final_score = base_score + trend_adjustment
    
    # Additional distraction: unused set operation
    unique_weights = set(weights)
    redundant_calc = len(unique_weights) * 7  # Computed but ignored
    
    return final_score

# Execute key statement
temp_debug = deprecated_analysis(data_packets)  # Red herring call
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")