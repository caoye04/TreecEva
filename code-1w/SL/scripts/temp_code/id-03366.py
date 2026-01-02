from collections import defaultdict, Counter
import math

# Simulated sensor data stream (irrelevant for final result but adds complexity)
sensor_readings = [150, 200, 175, 180, 190, 210, 160, 170, 185, 195]
noise_filter = [x for x in sensor_readings if 160 <= x <= 200]
avg_filtered = sum(noise_filter) / len(noise_filter) if noise_filter else 0
decoy_aggregate = round(avg_filtered * 1.05, 2)

# Health monitoring system with multiple components (only some are relevant)
def analyze_trend(data):
    if len(data) < 3:
        return 0
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
        elif data[i] < data[i-1]:
            trend_score -= 1
    return trend_score

# Irrelevant diagnostic function (dead code path)
def legacy_diagnostic(seq):
    total = 0
    for val in seq:
        if val % 2 == 0:
            total += val // 2
        else:
            total += val * 3
    return total

# Core processing logic (partially relevant)
def extract_features(values):
    features = defaultdict(float)
    features['mean'] = sum(values) / len(values)
    features['variance'] = sum((x - features['mean'])**2 for x in values) / len(values)
    features['skew'] = sum(((x - features['mean']) / (features['variance']**0.5 + 1e-8))**3 for x in values) / len(values)
    features['peaks'] = len([i for i in range(1, len(values)-1) if values[i] > values[i-1] and values[i] > values[i+1]])
    return features

# Decoy transformation chain
transform_chain = ['raw', 'filtered', 'normalized', 'enhanced']
processing_log = {stage: False for stage in transform_chain}
processing_log['raw'] = True

# Real-time anomaly detection (distractor module)
class AnomalyDetector:
    def __init__(self, window=3, threshold=0.85):
        self.window = window
        self.threshold = threshold
        self.buffer = []
    
    def check(self, value):
        self.buffer.append(value)
        if len(self.buffer) > self.window:
            self.buffer.pop(0)
        if len(self.buffer) < self.window:
            return False
        avg = sum(self.buffer) / len(self.buffer)
        variance = sum((x - avg)**2 for x in self.buffer) / len(self.buffer)
        z_score = abs(value - avg) / (variance**0.5 + 1e-8)
        return z_score > self.threshold

# Unused detector instance (misleading object)
anomaly_detector = AnomalyDetector(threshold=0.75)
for val in sensor_readings[:5]:
    anomaly_detector.check(val)  # Results discarded

# Critical data structures (some fields used, others not)
health_data = {
    'vital_sequence': [45, 52, 48, 55, 51, 49, 53],
    'timestamp_cycle': list(range(7)),
    'mode_flags': [True, False, True, True, False, True, False],
    'auxiliary': [0.1, 0.3, 0.2, 0.4, 0.35, 0.25, 0.15]
}

thresholds = {
    'baseline': 50,
    'tolerance': 5,
    'decay_factor': 0.9,
    'limit_override': 60
}

# Complex preprocessing with red herring operations
temp_store = []
for idx, val in enumerate(health_data['vital_sequence']):
    adjusted = val
    if health_data['mode_flags'][idx]:
        adjusted = max(adjusted, thresholds['baseline'] - thresholds['tolerance'])
    if idx % 2 == 0:
        adjusted = int(adjusted * thresholds['decay_factor'])  # Misleading modification
    temp_store.append(adjusted)

# Shadow copy with bit manipulation distraction
bitwise_shadow = 0
for val in health_data['vital_sequence']:
    bitwise_shadow ^= val << 1
    bitwise_shadow |= (val & 7)

# Actual feature extraction (uses original data despite prior modifications)
extracted = extract_features(health_data['vital_sequence'])

# Irrelevant statistical summary
descriptive_stats = {
    'range': max(health_data['vital_sequence']) - min(health_data['vital_sequence']),
    'median': sorted(health_data['vital_sequence'])[len(health_data['vital_sequence'])//2],
    'mode_count': Counter(health_data['vital_sequence']).most_common(1)[0][1]
}

# Core decision logic buried in complexity
def process_metrics(data_dict, config):
    sequence = data_dict['vital_sequence']
    base = config['baseline']
    tol = config['tolerance']
    
    # Step 1: Count how many values exceed baseline + tolerance
    above_threshold = len([x for x in sequence if x > base + tol])
    
    # Step 2: Analyze trend direction using helper
    trend = analyze_trend(sequence)
    
    # Step 3: Apply modular arithmetic weighting
    weighted_trend = (above_threshold * 3 + trend) % 7
    
    # Step 4: Use slicing to get middle segment
    mid_segment = sequence[2:5]  # Elements at indices 2,3,4
    
    # Step 5: Calculate midpoint average
    mid_avg = sum(mid_segment) / len(mid_segment)
    
    # Step 6: Normalize against baseline
    normalized_mid = mid_avg - base
    
    # Step 7: Combine with weighted trend using min/max logic
    combined = max(normalized_mid, 1) * min(weighted_trend, 5)
    
    # Step 8: Final adjustment using tuple unpacking and conditional
    multiplier, offset = (1.5, 2) if len(sequence) >= 7 else (1.2, 1)
    final_score = (combined * multiplier) + offset
    
    # Step 9: Round to nearest integer (key step)
    return round(final_score)

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)

# Red herring output (unused)
summary_tuple = (decoy_aggregate, bitwise_shadow, descriptive_stats['mode_count'])

# Correct output
print(f"Result: {final_diagnostic}")