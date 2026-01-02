from collections import defaultdict
import math

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (100, 23.5), (105, 24.1), (110, 23.9), (115, 25.0), (120, 26.2),
    (125, 25.8), (130, 27.1), (135, 28.3), (140, 27.9), (145, 29.0)
]

# Irrelevant helper: converts timestamp to formatted string (not used in final logic)
def format_timestamp(ts):
    hours = ts // 60
    mins = ts % 60
    return f'{hours:02d}:{mins:02d}'

# Misleading preprocessing: computes moving average but only partially used
def compute_moving_average(data, window=3):
    avg = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        avg.append(sum(x[1] for x in data[start:i+1]) / (i - start + 1))
    return avg

# Extract values above threshold (relevant)
def filter_critical_readings(data, threshold=26.0):
    return [val for _, val in data if val > threshold]

# Transform data: apply logarithmic scaling to high values
scaled_transform = lambda vals: [math.log(v) * 1.5 for v in vals]

# Dead code path: never called
def analyze_trend_pattern(seq):
    increasing = sum(1 for a, b in zip(seq, seq[1:]) if b > a)
    decreasing = sum(1 for a, b in zip(seq, seq[1:]) if b < a)
    return increasing - decreasing

# Main processing pipeline
def preprocess_sensor_data(raw_data):
    # Step 1: Filter critical readings above threshold
    critical_vals = filter_critical_readings(raw_data)
    
    # Step 2: Apply log-based transformation
    transformed = scaled_transform(critical_vals)
    
    # Step 3: Bucket into ranges using defaultdict (semi-relevant)
    buckets = defaultdict(int)
    for v in transformed:
        key = int(v)  # floor value as bucket
        buckets[key] += 1
    
    # Step 4: Compute weighted index (only buckets.keys() used later)
    weight_index = sum(k * freq for k, freq in buckets.items())
    
    # Return full structure even though only part is used
    return {
        'raw_filtered': critical_vals,
        'transformed': transformed,
        'buckets': dict(buckets),
        'weight_index': weight_index,
        'count': len(critical_vals)
    }

# Another distraction: string manipulation unrelated to final score
data_tag = "sensor_v2"
version_code = ''.join([c for c in data_tag if c.isdigit()])
version_multiplier = int(version_code) if version_code else 1

# Process the data
processed_data = preprocess_sensor_data(timestamped_readings)

# Extract bucket keys and sort them (core relevant step)
bucket_keys_sorted = sorted(processed_data['buckets'].keys())

# Perform pairwise difference accumulation (key logic)
diff_accumulator = 0
for i in range(1, len(bucket_keys_sorted)):
    diff = bucket_keys_sorted[i] - bucket_keys_sorted[i-1]
    diff_accumulator += diff * i  # Weight by position

# Secondary signal: use count of critical readings
signal_count = processed_data['count']

# Fake complexity: simulate noise correction (constant offset)
correction_factor = 0.0
for shift in [1, 2]:
    shifted = [k << shift for k in processed_data['buckets'].keys()]
    correction_factor += sum(shifted) * 0.0001  # negligible effect

correction_factor = round(correction_factor, 4)

# Final scoring function
def calculate_final_score(data_dict):
    base = diff_accumulator  # depends on sorted bucket differences
    bonus = signal_count * 2
    penalty = len(data_dict['transformed']) % 3  # small cyclic penalty
    return int(base + bonus - penalty)

# Execute main computation
final_score = calculate_final_score(processed_data)

# Print result as required
print(f"Result: {final_score}")