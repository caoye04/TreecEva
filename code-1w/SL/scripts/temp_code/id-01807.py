from collections import defaultdict, Counter
import math

# Simulated sensor data feed (realistic domain: health monitoring system)
data_stream = [72, 75, 73, 70, 68, 120, 74, 76, 77, 71, 69, 73, 75, 135, 78, 74, 72, 70, 68, 80]

def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        end = i + 1
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Irrelevant preprocessing: signal smoothing (distraction)
filtered_data = smooth_signal(data_stream)

# Decoy function: looks important but unused in final calculation
def compute_heart_rate_variability(rri_intervals):
    mean_rr = sum(rri_intervals) / len(rri_intervals)
    squared_diffs = [(rr - mean_rr)**2 for rr in rri_intervals]
    return math.sqrt(sum(squared_diffs) / len(squared_diffs)) if squared_diffs else 0

# Another decoy: frequency domain distraction
def spectral_power_band(data, low, high):
    # Simulating FFT bins (not actually computed)
    return sum(x ** 2 for x in data if low < x < high) * 0.01

# Real processing begins: categorize readings
normal_range = (65, 100)
elevated_range = (100, 120)
critical_range = (120, 200)

# Distractor counters (used nowhere critical)
decoys = {
    'spurious_alerts': 0,
    'recovered_nodes': [],
    'checksum': 0
}

temp_log = []
for val in data_stream:
    if val > 110:
        temp_log.append('ALERT')
        decoys['spurious_alerts'] += 1
    elif val < 70:
        temp_log.append('LOW')
    else:
        temp_log.append('OK')

class DataProcessor:
    def __init__(self, base_offset=0):
        self.offset = base_offset
        self.cache = defaultdict(int)
        self.timestamp = 1000

    def integrate(self, values):
        result = []
        for v in values:
            adjusted = v + self.offset
            self.cache[v] += 1
            result.append(adjusted)
        return result

# Unused processor instance (red herring)
processor = DataProcessor(base_offset=-5)
offset_data = processor.integrate(data_stream)

# Core logic disguised among distractions
abnormal_count = 0
outlier_flags = []
for reading in data_stream:
    if reading > 100:
        abnormal_count += 1
        outlier_flags.append(reading)

# Secondary metric with misleading name
system_load = len([x for x in data_stream if x > 90])

# Bit manipulation decoy (looks complex but irrelevant)
def encrypt_key(sequence):
    acc = 0
    for num in sequence[:5]:
        acc ^= (num << 2) | (num >> 1)
    return acc & 0xFFFF

key_cipher = encrypt_key(data_stream)

# Real threshold logic buried here
thresholds = {
    'warning': 105,
    'critical': 125
}

health_data = {
    'readings': data_stream,
    'stats': {
        'mean': sum(data_stream) / len(data_stream),
        'max_val': max(data_stream),
        'min_val': min(data_stream)
    },
    'flags': {
        'high_warning': sum(1 for x in data_stream if x > thresholds['warning']),
        'critical_spike': any(x > thresholds['critical'] for x in data_stream)
    }
}

# Lambda-based transformation (meets requirement)
transform = lambda x: x * 0.95 if x > 100 else x * 1.02
transformed_readings = [transform(x) for x in data_stream]

# Set operations (meets requirement): find unique high values
raw_set = set(data_stream)
warning_set = {x for x in raw_set if x > thresholds['warning']}
critical_set = {x for x in raw_set if x > thresholds['critical']}
ambiguous_set = warning_set - critical_set

# Cross-structure correlation (distractor)
correlation_score = len(critical_set) * 10 + len(ambiguous_set) * 3

# Dead code path (never executed)
if False:
    decoys['checksum'] = sum(decoys.values())
    raise RuntimeError("Legacy fault")

# Actual analysis function (core logic)
def analyze_metrics(data, limits):
    readings = data['readings']
    mean_val = data['stats']['mean']
    
    # Logic steps:
    # 1. Count how many exceed warning threshold
    warnings = sum(1 for x in readings if x > limits['warning'])
    # 2. Check if any exceed critical
    has_critical = any(x > limits['critical'] for x in readings)
    # 3. Calculate weighted risk score
    risk_weight = warnings * 17
    if has_critical:
        risk_weight += 23
    # 4. Apply decay factor based on mean
    if mean_val < 85:
        risk_weight -= 5
    # 5. Use set difference to adjust score
    high_only = len(warning_set - critical_set)
    risk_weight += high_only * 7
    # 6. Use Counter to find most frequent abnormal reading
    abnormal_vals = [x for x in readings if x > limits['warning']]
    if abnormal_vals:
        freq_dist = Counter(abnormal_vals)
        mode_val = freq_dist.most_common(1)[0][0]
        # 7. Adjust by modal distance from critical
        risk_weight += abs(mode_val - limits['critical'])
    # 8. Final adjustment using integer division
    final_score = risk_weight // 2
    return final_score

# Key execution point
final_diagnostic = analyze_metrics(health_data, thresholds)

# Output required format
print(f"Target result: {final_diagnostic}")