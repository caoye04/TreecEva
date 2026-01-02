from collections import defaultdict, Counter

# Simulated system log analysis with diagnostic scoring

def analyze_frequency(patterns):
    freq_map = defaultdict(int)
    for p in patterns:
        freq_map[p] += 1
    return freq_map

def compute_entropy(values):
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * __import__('math').log2(prob)
    return round(entropy, 6)

def extract_signals(raw_data):
    signals = []
    for i, val in enumerate(raw_data):
        if i % 3 == 0 and val > 50:
            signals.append('HIGH')
        elif val < 10:
            signals.append('LOW')
        else:
            signals.append('NORMAL')
    return signals

def dummy_transform(x):
    # Dead function - never used
    return (x ** 2 + 3 * x + 1) % 100

def evaluate_stability(readings):
    trend = []
    for i in range(1, len(readings)):
        trend.append(1 if readings[i] >= readings[i-1] else 0)
    runs = 1
    for i in range(1, len(trend)):
        if trend[i] != trend[i-1]:
            runs += 1
    return runs > len(trend) // 2

# Irrelevant signal processing chain
raw_signals = [85, 12, 67, 90, 5, 44, 77, 23, 58, 91, 4, 33]
noise_filter = list(map(lambda x: x + 1 if x % 2 == 0 else x - 1, raw_signals))
filtered = [x for x in noise_filter if x not in [13, 24, 45]]

# Real data path
log_entries = [
    {'id': 'SYS_001', 'load': 88, 'errors': 2, 'region': 'NA'},
    {'id': 'SYS_002', 'load': 45, 'errors': 0, 'region': 'EU'},
    {'id': 'SYS_003', 'load': 92, 'errors': 5, 'region': 'NA'},
    {'id': 'SYS_004', 'load': 55, 'errors': 1, 'region': 'AS'},
    {'id': 'SYS_005', 'load': 77, 'errors': 0, 'region': 'EU'},
    {'id': 'SYS_006', 'load': 81, 'errors': 3, 'region': 'NA'}
]

system_thresholds = {
    'critical_load': 85,
    'max_errors': 4,
    'priority_regions': ['NA', 'EU']
}

# Distractor: unused complex structure
historical_trends = {
    'weekly': defaultdict(lambda: 0),
    'monthly': Counter()
}
for entry in log_entries:
    region = entry['region']
    historical_trends['weekly'][region] += entry['load']
    historical_trends['monthly'].update([region])

# Secondary distractor computation
char_counter = Counter()
for entry in log_entries:
    for char in entry['id']:
        if char.isalpha():
            char_counter[char] += 1

# Real logic begins here
high_load_count = 0
error_risk_score = 0.0
region_bonus = 0

for entry in log_entries:
    if entry['load'] > system_thresholds['critical_load']:
        high_load_count += 1
    if entry['errors'] > system_thresholds['max_errors']:
        error_risk_score += 1.5
    if entry['region'] in system_thresholds['priority_regions']:
        region_bonus += 0.8

# Intermediate metrics
base_score = high_load_count * 10
adjusted_risk = error_risk_score * 2.5
geographic_factor = region_bonus * 3

# Simulated calibration offset (distractor)
calibration_log = []
for i, (k, v) in enumerate(analyze_frequency(['A','B','A','C','B','A']).items()):
    calibration_log.append(f"{k}:{v}")

# Real transformation
entropic_weight = compute_entropy([base_score, adjusted_risk, geographic_factor])
signal_pattern = extract_signals([entry['load'] for entry in log_entries])
signal_freq = analyze_frequency(signal_pattern)

# Misleading aggregation
phantom_score = 0
for sig, cnt in signal_freq.items():
    if sig == 'HIGH':
        phantom_score += cnt * 2.1
    elif sig == 'LOW':
        phantom_score -= cnt * 1.3

# Final decision logic
primary_diagnostic = base_score + adjusted_risk
if entropic_weight > 1.0:
    primary_diagnostic += geographic_factor

# Critical red herring: complex but unused calculation
temporal_weights = []
for i, entry in enumerate(log_entries):
    weight = (i + 1) * entry['load'] / (entry['errors'] + 1)
    temporal_weights.append(weight)

aggregated_weight = sum(temporal_weights) / len(temporal_weights) if temporal_weights else 0
deceptive_index = aggregated_weight * entropic_weight

# Final processing function
def process_metrics(entries, thresholds):
    score = 0
    critical_count = 0
    for e in entries:
        if e['load'] > thresholds['critical_load']:
            score += 15
            critical_count += 1
        if e['errors'] > thresholds['max_errors']:
            score += 10
    if critical_count >= 2:
        score += 25  # escalation bonus
    return score

# This variable contains the real answer
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")