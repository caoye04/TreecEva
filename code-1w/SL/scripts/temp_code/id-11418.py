from collections import defaultdict, Counter
import math

# Simulated system telemetry data
current_readings = [87, 94, 65, 72, 91, 88, 77, 63, 95, 82]
operation_cycles = 17
maintenance_flag = False
baseline_offset = 3.14159
diagnostic_mode = True

# Irrelevant signal processing (dead path)
def apply_fourier_transform(signal):
    transformed = []
    for i in range(len(signal)):
        val = 0
        for j in range(len(signal)):
            val += signal[j] * math.cos(2 * math.pi * i * j / len(signal))
        transformed.append(val)
    return transformed

# Unused helper function (decoy)
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return entropy

# Misleading intermediate calculation (red herring)
temp_anomaly_score = 0
for reading in current_readings:
    if reading < 70:
        temp_anomaly_score += (70 - reading) * 1.5
    elif reading > 90:
        temp_anomaly_score += (reading - 90) * 0.8

# Unused normalization attempt
normalized_readings = [round((x - min(current_readings)) / (max(current_readings) - min(current_readings)) * 100) for x in current_readings]

# Core health analysis logic (relevant path)
def evaluate_stability_metric(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    return round(avg - std_dev, 3)

def generate_threshold_map(cycles, offset):
    # Complex mapping with irrelevant trigonometric noise
    thresholds = defaultdict(float)
    for i in range(1, 6):
        raw_val = cycles * (i ** 0.5) + offset
        noise = math.sin(i) * math.cos(cycles % 10)
        thresholds[f'sensor_group_{i}'] = abs(raw_val + noise)
    # Override with actual required values (critical)
    thresholds['sensor_group_1'] = 85.0
    thresholds['sensor_group_2'] = 76.5
    thresholds['sensor_group_3'] = 70.0
    thresholds['sensor_group_4'] = 80.2
    thresholds['sensor_group_5'] = 92.1
    return thresholds

# Data aggregation with distractor keys
system_metrics = {
    'primary': current_readings,
    'backup': [0]*len(current_readings),  # unused
    'timestamp': '2023-11-05T14:30:00Z',
    'version': 'v2.3.1-alpha',
    'stability_index': evaluate_stability_metric(current_readings),
    'diagnostics_active': diagnostic_mode,
    'legacy_mode': False,
    'anomaly_buffer': temp_anomaly_score,  # red herring
    'cycle_count': operation_cycles
}

threshold_map = generate_threshold_map(operation_cycles, baseline_offset)

# Secondary irrelevant computation chain
event_log = []
for cycle in range(1, operation_cycles + 1):
    event_type = "REBOOT" if cycle % 7 == 0 else "HEALTH_CHECK"
    event_log.append(f"Cycle{cycle}:{event_type}")
log_summary = Counter([event.split(':')[1] for event in event_log])

# Core decision logic with nested conditions and distractors
def analyze_health_status(metrics, thresholds):
    primary_data = metrics['primary']
    stability = metrics['stability_index']
    cycle_count = metrics['cycle_count']
    score = 0
    
    # Real evaluation logic (interleaved with decoys)
    group_keys = [f'sensor_group_{i}' for i in range(1, 6)]
    expected_baseline = sum(thresholds[k] for k in group_keys) / len(group_keys)
    
    # Actual scoring mechanism
    if stability > 75.0:
        score += 25
    if cycle_count > 10:
        score += 10
    
    # Critical conditional check (hidden in noise)
    high_performers = [r for r in primary_data if r >= 85]
    if len(high_performers) >= 4:
        bonus = len(high_performers) * 3
        score += bonus
    
    # Distractor logic using irrelevant variables
    if metrics.get('legacy_mode'):
        score -= 20
    if metrics['diagnostics_active']:
        # Misleading compensation
        dummy_adjustment = sum(1 for x in primary_data if x < 70) * 2
        score += 5  # Fixed diagnostic bonus, not dependent on dummy
    
    # Final override condition (easily missed)
    avg_primary = sum(primary_data) / len(primary_data)
    if avg_primary >= 80.0 and stability >= 78.0:
        score = int(avg_primary) + int(stability // 1)  # deterministic override
    
    # Dead code branch (never reached due to override)
    if score > 100:
        score = 99
        
    return score

# Execute main analysis
final_diagnostic = analyze_health_status(system_metrics, threshold_map)
print(f"Result: {final_diagnostic}")