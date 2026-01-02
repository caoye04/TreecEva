from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion (some irrelevant)
temperature_readings = [23.5, 24.1, 22.9, 25.0, 26.3, 24.8]
humidity_readings = [45, 47, 50, 44, 60, 55]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1014]

# Core data for evaluation
event_log = [
    'startup', 'calibration_ok', 'data_sample', 'warning:overheat',
    'data_sample', 'data_sample', 'fault_reset', 'data_sample'
]

# Misleading intermediate variables (distractors)
baseline_offset = sum(temperature_readings) / len(temperature_readings)
compression_ratio = 0.87
normalization_factor = math.log(baseline_offset + 1)
aggregated_power = 0
for i in range(len(pressure_readings)):
    aggregated_power += pressure_readings[i] * (i + 1)

# Data transformation with red herring logic
def analyze_events(log):
    count_map = defaultdict(int)
    for event in log:
        if 'data_' in event:
            count_map['samples'] += 1
        elif 'error' in event or 'fault' in event:
            count_map['failures'] += 1
        elif 'warning' in event:
            count_map['warnings'] += 1
        else:
            count_map['routine'] += 1

    # Dead code path - never used downstream
    if count_map['failures'] == 0:
        recovery_sequence = [x**2 for x in range(count_map['warnings'])]
    else:
        recovery_sequence = []

    return count_map

# Unused helper (distractor)
def validate_checksum(data):
    checksum = 0
    for item in data:
        if isinstance(item, str):
            checksum ^= len(item)
        else:
            checksum ^= int(item)
    return checksum % 17 == 0

# Relevant flag generation
quality_flags = []
for temp in temperature_readings:
    if temp > 25.5:
        quality_flags.append('CRITICAL')
    elif temp > 24.5:
        quality_flags.append('ELEVATED')
    else:
        quality_flags.append('NORMAL')

# Performance metrics with mixed relevance
performance_data = []
event_stats = analyze_events(event_log)
sample_count = event_stats['samples']
warning_count = event_stats['warnings']

for i, flag in enumerate(quality_flags):
    base_metric = temperature_readings[i] * 10
    adjusted = base_metric
    
    # Nested conditional scoring with distractors
    if flag == 'CRITICAL':
        adjusted -= 15
        if i % 2 == 0:
            adjusted += 3  # minor correction
    elif flag == 'ELEVATED':
        adjusted -= 5
        # Irrelevant nested block
        temp_str = f"{temperature_readings[i]:.1f}"
        digits = [int(d) for d in temp_str if d.isdigit()]
        digit_sum = sum(digits)
    else:
        adjusted += 2
    
    performance_data.append(adjusted)

# Decoy calculation chain (never used)
redundant_aggregate = 0
for reading in humidity_readings:
    redundant_aggregate += math.sqrt(reading) * 2.5
redundant_aggregate = round(redundant_aggregate, 2)

# Central processing function with multiple concepts
def process_metrics(flags, metrics):
    score = 100
    penalty_counter = Counter(flags)
    
    # Logical operations and comparisons
    if penalty_counter['CRITICAL'] >= 2:
        score -= 30
    elif penalty_counter['CRITICAL'] == 1:
        score -= 15
    
    if penalty_counter['ELEVATED'] > 3:
        score -= 10
    
    # Bit manipulation red herring
    bit_mask = 0b1010
    masked_value = sample_count & bit_mask
    if masked_value > 4:
        score -= 3
    
    # Mean calculation with filtering
    valid_metrics = [m for m in metrics if m > 200]
    if valid_metrics:
        avg_metric = sum(valid_metrics) / len(valid_metrics)
        if avg_metric < 235:
            score -= 5
    
    # String-based logic distraction
    status_codes = ['OK', 'READY', 'ACTIVE']
    for idx, code in enumerate(status_codes):
        if code == 'ACTIVE' and warning_count > 0:
            score -= 2

    # Final adjustment using enumerate and zip (required features)
    adjustments = [0.5, -1.0, 0.0, 1.5, -0.5, 0.0]
    for i, (val, adj) in enumerate(zip(metrics, adjustments)):
        if i % 2 == 1 and val > 220:
            score += adj  # some positive, some negative

    return int(score)

# Execution point of interest
final_score = process_metrics(quality_flags, performance_data)
print(f"Target result: {final_score}")