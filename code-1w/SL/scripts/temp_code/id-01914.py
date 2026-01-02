from collections import defaultdict, Counter
import itertools

# Simulated sensor data processing pipeline for environmental monitoring

# Raw sensor inputs (simulated)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
timestamps = list(range(100, 110))
raw_data_stream = [
    (sid, ts, (ord(sid[1]) * 100 + ts) % 73) for sid in sensor_ids for ts in timestamps
]

# Irrelevant auxiliary mapping (distractor)
legacy_mapping = {s: f'L-{i}' for i, s in enumerate(sensor_ids)}

# Data aggregation by sensor
aggregated = defaultdict(list)
for sid, ts, val in raw_data_stream:
    aggregated[sid].append(val)

# Compute rolling averages (unused red herring)
rolling_averages = {}
for sid, readings in aggregated.items():
    rolling_averages[sid] = [
        sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)
    ]

# Threshold filtering based on dynamic criteria
base_threshold = 37
adaptive_factor = len(aggregated) * 0.8
trigger_level = base_threshold + int(adaptive_factor)

filtered_metrics = []
for sid, readings in aggregated.items():
    for val in readings:
        if val > trigger_level and val % 2 == 1:  # Only odd values above threshold
            filtered_metrics.append(val)

# Misleading statistical summary (dead path)
summary_stats = {}
for k, v in aggregated.items():
    summary_stats[k] = {
        'min': min(v),
        'max': max(v),
        'range': max(v) - min(v),
        'mode': Counter(v).most_common(1)[0][0]
    }

# Unused complex transformation chain (decoy logic)
def transform_sequence(seq):
    shifted = [(x >> 1) ^ 3 for x in seq]
    grouped = [sum(group) for k, group in itertools.groupby(shifted, key=lambda x: x % 4)]
    return [g * 2 for g in grouped if g > 5]

transformed_output = transform_sequence([10, 20, 30, 40])  # Never used

# Real analysis function operating on filtered_metrics
def analyze_readings(data):
    if not data:
        return -1
    
    # Count frequency of high-value readings
    freq = Counter(data)
    most_freq_val = freq.most_common(1)[0][1]
    
    # Apply bit manipulation for diagnostic signature
    signature = 0
    for val in set(data):
        signature ^= (val << 2) | (val & 3)
    
    # Secondary filter: only values appearing more than once
    multiples = [v for v, cnt in freq.items() if cnt > 1]
    multiplier = len(multiples) if multiples else 1
    
    # Core calculation: weighted diagnostic index
    base_score = sum(freq.values())
    adjustment = sum(1 for x in data if x > 50) - sum(1 for x in data if x < 45)
    
    # Final composite result
    diagnostic_index = (base_score * 17) + (adjustment * 5) + (signature % 23)
    return diagnostic_index * multiplier

# Critical execution point
final_diagnostic = analyze_readings(filtered_metrics)

# Output result
print(f"Result: {final_diagnostic}")