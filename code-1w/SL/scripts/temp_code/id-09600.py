from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion with noise
raw_readings = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]

# Irrelevant statistical summary (distractor)
distractor_stats = {
    'mean': sum(raw_readings) / len(raw_readings),
    'variance': sum((x - sum(raw_readings)/len(raw_readings))**2 for x in raw_readings) / len(raw_readings),
    'skew': 0
}

# Data transformation pipeline
filtered_noise = [x for x in raw_readings if x > 2]
shifted_data = [(x * 2 + 1) % 11 for x in filtered_noise]

# Frequency analysis (partially relevant)
frequency_count = Counter(shifted_data)
mode_value = frequency_count.most_common(1)[0][0]

# Decoy pattern detection (dead path)
def detect_anomaly(seq):
    return sum(1 for i in range(len(seq)-1) if seq[i] > seq[i+1]) % 7

anomaly_score = detect_anomaly(shifted_data)  # Unused downstream

# Transform into grouped phases
phases = defaultdict(list)
for idx, val in enumerate(shifted_data):
    phase_key = idx % 4
    phases[phase_key].append(val)

# Apply phase-specific smoothing (irrelevant but plausible)
smoothed_phases = {}
for k, values in phases.items():
    smoothed = [math.ceil(sum(values[:i+1]) / (i+1)) for i in range(len(values))]
    smoothed_phases[k] = smoothed

# Generate control checksum (misleading intermediate)
checksum = 0
for k in sorted(smoothed_phases):
    for val in smoothed_phases[k]:
        checksum = (checksum * 31 + val) % 10007

temp_adjustment = (checksum ^ mode_value) % 13  # Nowhere used

# Core logic: pattern analysis based on frequency and distribution
transformed_data = []
for k in sorted(phases.keys()):
    segment = phases[k]
    segment_freq = Counter(segment)
    weighted_sum = sum(v * segment_freq[v] ** 1.5 for v in segment_freq)
    transformed_data.append(int(weighted_sum))

# Threshold map generation (red herring version)
threshold_map = {}
for i in range(6):
    threshold_map[i] = int(math.log(1 + i * i) * 10) if i > 0 else 5

# Another decoy structure
lookup_matrix = [[i*j + 2 for j in range(5)] for i in range(5)]
device_calibration = sum(lookup_matrix[i][i] for i in range(5))  # Not used

# Critical function with embedded logic chain
def analyze_pattern(data_seq, thresholds):
    accumulator = 0
    for i, val in enumerate(data_seq):
        # Conditional accumulation with nested logic
        if i in thresholds:
            bound = thresholds[i]
            if val > bound:
                accumulator += val * (i + 1)
            elif val == bound:
                accumulator -= i
            else:
                accumulator += val // (i + 1) if i != 0 else 0
        else:
            # Fallthrough case with bit manipulation distraction
            temp = val ^ i
            temp = temp & (temp - 1)  # Clear lowest set bit
            accumulator += bin(temp).count('1')
    
    # Final adjustment using string operations (plausible but specific)
    acc_str = str(accumulator)
    digit_counts = Counter(acc_str)
    entropy_like = sum(d * math.log(d) for d in digit_counts.values() if d > 0)
    
    # Only the integer part matters in this context
    final_score = int(accumulator + round(entropy_like))
    
    return final_score

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

# Output required format
print(f"Target result: {final_diagnostic}")