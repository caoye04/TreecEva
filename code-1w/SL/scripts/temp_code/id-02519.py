def analyze_system_load(inputs):
    # Irrelevant function - dead code path
    temp = 0
    for x in inputs:
        temp += x % 7
    return temp * 2


def validate_checksum(data):
    # Another decoy function with misleading intermediate result
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) & 0xF
    return checksum == 15


def transform_dataset(raw):
    # Unused transformation logic - distractor
    processed = [x * 2 + 1 for x in raw if x % 3 != 0]
    sorted_processed = sorted(processed, reverse=True)
    return [y >> 1 for y in sorted_processed]


def compute_entropy(values):
    # Seemingly relevant but unused advanced calculation
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * (prob).bit_length()
    return round(entropy, 4)


def filter_outliers(data, threshold=100):
    # Called once but only used to set a red herring variable
    filtered = [x for x in data if abs(x) < threshold]
    outlier_count = len(data) - len(filtered)  # Distractor variable
    return filtered

# Global configuration - some irrelevant constants
MAX_CAPACITY = 500
BASE_OFFSET = 23
SCALE_FACTOR = 17  # Never actually used in final computation

# Simulated monitoring metrics (mixed data types)
metrics = {
    'cpu_load': [85, 90, 92, 88, 95],
    'memory_usage': [450, 480, 470, 460, 490],
    'disk_reads': [120, 115, 130, 125, 118],
    'network_latency': [40, 45, 50, 42, 48]
}

benchmark_data = {
    'thresholds': {
        'critical': 90,
        'warning': 75
    },
    'weights': {
        'performance': 0.6,
        'stability': 0.4
    },
    'calibration': [1, -1, 2, -2, 3]
}

# Secondary data structures - potential distractions
historical_trends = set()
for val in metrics['cpu_load']:
    historical_trends.add(val // 5)

active_alerts = set(['high_cpu', 'normal_memory'])
alert_suppression = set(['disk_spikes'])

# Initialize key variables
baseline_ref = sum(benchmark_data['calibration']) * BASE_OFFSET  # = 5 * 23 = 115

# Compute performance score using cpu and memory
load_values = metrics['cpu_load'] + metrics['memory_usage']
cleaned_load = filter_outliers(load_values, threshold=MAX_CAPACITY)

# Extract critical thresholds
crit_thresh = benchmark_data['thresholds']['critical']
warn_thresh = benchmark_data['thresholds']['warning']

# Count violations
critical_violations = 0
for val in cleaned_load:
    if val >= crit_thresh:
        critical_violations += 1

# Stability metric based on variation
variation = 0
for i in range(1, len(metrics['cpu_load'])):
    variation += abs(metrics['cpu_load'][i] - metrics['cpu_load'][i-1])

avg_variation = variation / (len(metrics['cpu_load']) - 1)

# Apply stability penalty
stability_score = 100 - min(avg_variation, 50)

# Performance score based on critical violations
raw_performance = 100 - (critical_violations * 10)

# Weighted combination
weighted_performance = raw_performance * benchmark_data['weights']['performance']
stability_component = stability_score * benchmark_data['weights']['stability']

intermediate_result = weighted_performance + stability_component  # This gets overwritten below

# Complex correction factor using dictionary lookup and set operations
correction_map = {i: i*2 for i in range(1, 11)}
applicable_corrections = set(correction_map.keys()) & set([critical_violations, avg_variation, baseline_ref])

if applicable_corrections:
    correction_factor = max(applicable_corrections) * 0.5
else:
    correction_factor = 1.0

# Final adjustment using bitwise manipulation and integer division
raw_final = int(intermediate_result)  # Was 88.0 -> 88
adjusted = (raw_final << 1)  # 88 << 1 = 176
adjusted = adjusted ^ 42  # 176 XOR 42 = 138
adjusted = adjusted // 3  # 138 // 3 = 46

final_score = adjusted + int(correction_factor)  # 46 + 0.5? No — correction_factor from max(...) where applicable_corrections = {2} → 2*0.5=1.0 → int(1.0)=1 → final_score = 47

Result: {final_score}