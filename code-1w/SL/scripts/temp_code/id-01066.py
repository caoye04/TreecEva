from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant readings
data_stream = [
    (1, [23.5, 24.1, 23.9, 25.0, 23.5]),
    (2, [19.2, 18.8, 19.0, 19.2, 18.7]),
    (3, [31.4, 32.0, 31.8, 31.4, 31.6]),
    (4, [17.3, 17.5, 17.2, 17.3, 17.4]),
    (5, [27.8, 28.1, 27.9, 27.8, 28.0])
]

# Irrelevant calibration map for unused sensors
sensor_calib = defaultdict(lambda: 1.0)
for i in range(1, 10):
    sensor_calib[i] = 0.98 + (i % 4) * 0.01

# Noise filter that's over-engineered but only partially used
def filter_noise(readings):
    filtered = []
    for val in readings:
        if abs(val - sum(readings) / len(readings)) < 0.6:
            filtered.append(val)
    return filtered if len(filtered) > 2 else readings[:3]

# Secondary metric that looks important but isn't used in final result
entropy_counter = Counter()
for sid, reads in data_stream:
    rounded = [round(r) for r in reads]
    for r in rounded:
        entropy_counter[r] += 1

# Core transformation pipeline
processed = {}
for sensor_id, readings in data_stream:
    clean_reads = filter_noise(readings)
    base_avg = sum(clean_reads) / len(clean_reads)
    
    # Apply fake correction (never actually used)
    corrected = [r * sensor_calib[sensor_id] for r in clean_reads]
    
    # Compute stability score (used later)
    variance = sum((r - base_avg) ** 2 for r in clean_reads) / len(clean_reads)
    stability = math.exp(-variance / 10.0)
    
    processed[sensor_id] = {
        'baseline': base_avg,
        'stability': stability,
        'quality_flag': len(clean_reads) == len(readings),
        'corrected_avg': sum(corrected) / len(corrected)  # Distractor field
    }

# Simulate diagnostic trace (dead code path)
def analyze_trend(data):
    trends = []
    for i in range(1, len(data)):
        prev = data[i-1][1][0]
        curr = data[i][1][0]
        trends.append(1 if curr > prev else -1)
    return sum(trends)

_ = analyze_trend(data_stream)  # Unused result

# Weight assignment with misleading prioritization
weights = {}
total_stability = sum(p['stability'] for p in processed.values())
for sid, p in processed.items():
    raw_weight = p['stability'] / total_stability if total_stability > 0 else 0.2
    weights[sid] = raw_weight * (1.05 if p['quality_flag'] else 0.95)

# Aggregate baseline with stability-weighted average
weighted_sum = 0
weight_total = 0
for sid, p in processed.items():
    weighted_sum += p['baseline'] * weights[sid]
    weight_total += weights[sid]

# Final computation - this is where the answer comes from
final_score = round(weighted_sum / weight_total, 4) if weight_total > 0 else 0.0

# Decoy calculation using corrected values (looks official but unused)
fake_aggregate = 0
for sid in sorted(processed.keys(), reverse=True):
    fake_aggregate += processed[sid]['corrected_avg']
fake_aggregate /= len(processed)

# Output the actual target result
print(f"Result: {final_score}")