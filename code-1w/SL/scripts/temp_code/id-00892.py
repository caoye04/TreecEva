from collections import defaultdict, Counter
import math

def analyze_sequence(seq):
    # Irrelevant helper function (dead code path)
    return sum(x ** 2 for x in seq if x > 0)

def generate_report(data):
    # Unused reporting function (distractor)
    report = defaultdict(int)
    for item in data:
        report['entries'] += 1
        report['total'] += item
    return dict(report)

def filter_outliers(values, limit=3):
    # Misleading preprocessing step with no impact on final result
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= limit * std_dev]

def compute_checksum(sequence):
    # Bit manipulation red herring
    checksum = 0
    for val in sequence:
        checksum ^= int(val * 10) & 0xFF
    return checksum

def evaluate_stability(readings):
    # Complex but irrelevant stability analysis
    if len(readings) < 2:
        return False
    trend = all(readings[i] <= readings[i+1] for i in range(len(readings)-1))
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings)
    return trend and variance < 100

# Simulated sensor log data (real input source)
raw_logs = [
    [12.4, 13.1, 11.7, 14.2, 9.8],
    [10.3, 11.0, 10.8, 12.1, 11.4],
    [13.5, 14.0, 13.8, 14.1, 13.6],
    [9.9, 10.1, 9.7, 10.3, 10.0]
]

# System configuration parameters (mix of relevant and irrelevant)
system_mode = 'diagnostic'
activation_key = 'ALPHA-7'
calibration_factor = 0.98
system_threshold = 10.5  # Used in final decision
sampling_rate = 50  # Red herring
log_compression = True  # Dead flag

# Data transformation pipeline
processed_buffers = []
for log_entry in raw_logs:
    # Normalize each log segment
    normalized = [x * calibration_factor for x in log_entry]
    processed_buffers.append(normalized)

# Aggregate all readings into a flat list
flattened_data = [item for sublist in processed_buffers for item in sublist]

# Irrelevant statistical summaries
mean_reading = sum(flattened_data) / len(flattened_data)
max_reading = max(flattened_data)
min_reading = min(flattened_data)
reading_range = max_reading - min_reading

# Misleading intermediate diagnostics
dynamic_weighting = sum(math.sin(x) for x in flattened_data[:10])
scaling_exponent = math.log(abs(dynamic_weighting) + 1, 2) if dynamic_weighting != 0 else 0

# Key distraction: complex bit manipulation with decoy output
data_signature = 0
for val in flattened_data[::2]:
    data_signature += int(val) << 1
    data_signature ^= data_signature >> 2

temp_adjustment = (data_signature & 0xFFFF) % 7

# Simulate conditional processing branches (only one matters)
primary_metric = 0
secondary_metric = 0

if system_mode == 'diagnostic':
    # Real computation branch
    count_above = sum(1 for x in flattened_data if x > system_threshold)
    total_valid = len([x for x in flattened_data if x > 0])
    ratio = count_above / total_valid if total_valid > 0 else 0
    
    # Core logic hidden among distractions
    base_score = ratio * 100
    adjustment = 3.7  # Hardcoded correction factor
    
    if count_above % 2 == 0:
        adjustment -= 1.2
    else:
        adjustment += 0.8
    
    primary_metric = base_score + adjustment
else:
    # Dead branch
    primary_metric = sum(flattened_data) // 10

# Secondary path with fake dependency
if activation_key.startswith('BETA'):
    secondary_metric = sum(1 for x in flattened_data if x < 10) * 2.5
else:
    # This runs but doesn't contribute
    dummy = [x for x in flattened_data if x % 1 < 0.5]
    secondary_metric = len(dummy) * 0.7

# String-based validation (distractor)
key_segments = activation_key.split('-')
if len(key_segments) == 2 and key_segments[0] == 'ALPHA':
    version_code = ord(key_segments[1][0]) - ord('0')
else:
    version_code = 0

# Hidden accumulator using string methods
debug_trace = "sensor_health_check_complete_v7"
version_digit = int(debug_trace[-1]) if debug_trace[-1].isdigit() else 1

# Critical function that determines final answer
def process_metrics(readings, threshold):
    # Count how many readings exceed threshold
    exceeding = [r for r in readings if r > threshold]
    count_exceed = len(exceeding)
    
    # Apply non-linear transformation
    transformed = sum(math.sqrt(x) for x in exceeding) if exceeding else 0
    
    # Combine with weighted count
    weight = 4.3 if len(readings) > 15 else 3.9
    raw_value = count_exceed * weight + transformed
    
    # Final adjustment using modulo arithmetic
    modifier = (version_digit * 2 + temp_adjustment) % 5
    return raw_value + modifier

# Execute key statement
temp_adjustment += 1  # Side effect before final call
temp_adjustment %= 4   # Normalization

final_diagnostic = process_metrics(flattened_data, system_threshold)

# Print result as required
print(f"Result: {final_diagnostic}")