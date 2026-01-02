from collections import defaultdict, Counter
import itertools

# Simulated sensor input data (real values)
sensor_readings = [18.2, 22.5, 19.8, 24.1, 20.3, 23.7, 19.0, 21.4]

def preprocess_stream(data):
    # Irrelevant transformation: maps to rounded values (distractor)
    rounded = [round(x) for x in data]
    offset_map = {i: val - 20 for i, val in enumerate(data)}
    return [x for x in data if x > 19.5]  # Only relevant part

# Misleading auxiliary function (dead logic path)
def legacy_normalization(vec):
    mean_val = sum(vec) / len(vec)
    return [3 * (x - mean_val) for x in vec]  # Never used

# Decoy statistical analysis
temporal_weights = [0.8, 1.2, 0.9, 1.1, 1.0, 1.3, 0.7, 1.4]
weighted_sum = sum(a * b for a, b in zip(sensor_readings, temporal_weights))
scaling_factor = weighted_sum / len(sensor_readings)  # Looks important, unused

# Real preprocessing step
filtered_data = preprocess_stream(sensor_readings)

# Complex transformation chain with red herrings
def generate_kernel(size):
    return [0.5 ** i for i in range(size)]

def apply_filter(sequence, kernel):
    padded = [0] * (len(kernel) - 1) + sequence
    result = []
    for i in range(len(sequence)):
        window = padded[i:i+len(kernel)]
        convolved = sum(a * b for a, b in zip(window, kernel))
        result.append(round(convolved, 3))
    return result

kernel_3 = generate_kernel(3)
filtered_data = apply_filter(filtered_data, kernel_3)  # Update filtered_data

# Fake anomaly detection (irrelevant)
anomaly_flags = [abs(x - 20) > 5 for x in sensor_readings]
flag_count = sum(anomaly_flags)
baseline_threshold = 0.75 * len(anomaly_flags)

# Data restructuring with meaningful and irrelevant parts
diagnostic_log = defaultdict(lambda: 'N/A')
diagnostic_log['source'] = 'sensor_array_A'
diagnostic_log['version'] = '3.7.1'

event_timeline = list(enumerate(filtered_data))
interpolation_points = list(itertools.accumulate([1, -1, 2, -2, 3]))  # Unused accumulation

# Critical processing chain
processing_chain = [
    sum(filtered_data),
    max(filtered_data) - min(filtered_data),
    len([x for x in filtered_data if x > 20.0])
]

# Secondary decoy structure
summary_stats = Counter()
summary_stats['high_readings'] = len([x for x in sensor_readings if x > 22])
summary_stats['low_readings'] = len([x for x in sensor_readings if x < 19])

# Use of lambda for obfuscation (looks complex but clear)
aggregation_rules = [
    lambda x: x[0] * 0.6,
    lambda x: x[1] * 1.25,
    lambda x: x[2] * 2.0
]

# Another misleading intermediate calculation
hypothetical_projection = [rule(processing_chain) for rule in aggregation_rules]  # Unused

# Real metric aggregation
variance_proxy = sum((x - sum(filtered_data)/len(filtered_data))**2 for x in filtered_data) / len(filtered_data)

def aggregate_metrics(chain):
    base_score = chain[0]  # Sum of filtered, processed readings
    spread_bonus = chain[1] * 0.8
    frequency_multiplier = chain[2] * 1.5
    return int(base_score + spread_bonus + frequency_multiplier - variance_proxy)

final_diagnostic = aggregate_metrics(processing_chain)
print(f"Result: {final_diagnostic}")