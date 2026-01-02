import math

# Simulated system metrics for performance evaluation
timestamps = [1623456780, 1623456781, 1623456782, 1623456783, 1623456784]
raw_readings = [127, 133, 129, 136, 131]

# Irrelevant signal processing functions (dead code path)
def apply_filter(signal):
    return [x * 0.9 + 10 for x in signal]

def compute_fft(data):
    return [complex(math.sin(x / 10), math.cos(x / 10)) for x in data]

# Unused auxiliary variables (distractors)
baseline_offset = 0.0034
normalization_factor = sum([math.exp(-0.1 * i) for i in range(10)])
scaling_matrix = [[1.0 if i == j else 0.1 for j in range(3)] for i in range(3)]

# Configuration dictionary with red herring keys
benchmark_config = {
    'version': '2.1-alpha',
    'thresholds': {
        'critical': 135,
        'warning': 130,
        'optimal': 125
    },
    'weights': {
        'accuracy': 0.6,
        'latency': 0.3,
        'throughput': 0.1
    },
    'deprecated_mode': True,
    'calibration_data': [0.1, 0.2, 0.3],  # unused
    'debug_trace': None
}

# Metrics log containing actual relevant data
metrics_log = [
    {'time': 1623456780, 'value': 127, 'type': 'sensor_A'},
    {'time': 1623456781, 'value': 133, 'type': 'sensor_A'},
    {'time': 1623456782, 'value': 129, 'type': 'sensor_A'},
    {'time': 1623456783, 'value': 136, 'type': 'sensor_A'},
    {'time': 1623456784, 'value': 131, 'type': 'sensor_A'}
]

# Decoy function that looks important but is never called
def analyze_trend(dataset):
    trend_score = 0
    for i in range(1, len(dataset)):
        if dataset[i] > dataset[i-1]:
            trend_score += 0.5
        elif dataset[i] < dataset[i-1]:
            trend_score -= 0.3
    return round(trend_score, 4)

# Auxiliary calculation with misleading intermediate result
hypothetical_gain = 0
for val in raw_readings:
    if val > 130:
        hypothetical_gain += math.log(val - 125)
hypothetical_gain = round(hypothetical_gain, 2)  # This is NOT used later

# Real processing begins here
valid_entries = [entry for entry in metrics_log if entry['type'] == 'sensor_A']
values_only = [entry['value'] for entry in valid_entries]

# Bit manipulation for checksum (appears complex but is part of real logic)
def compute_checksum(vals):
    checksum = 0
    for v in vals:
        checksum ^= v  # XOR into checksum
        checksum = (checksum << 1) & 0xFF | (checksum >> 7)  # 8-bit rotate left
    return checksum % 100

# Scoring function combining multiple concepts
def evaluate_performance(log, config):
    # Extract thresholds
    warn, crit = config['thresholds']['warning'], config['thresholds']['critical']
    
    # Count occurrences in zones
    counts = {
        'optimal': len([v for v in values_only if v <= warn]),
        'elevated': len([v for v in values_only if warn < v <= crit]),
        'critical': len([v for v in values_only if v > crit])
    }
    
    # Conditional expression scoring
    base_score = 100 if counts['critical'] == 0 else 60 - counts['critical'] * 5
    
    # Apply bonus/penalty using dictionary mapping
    penalty_map = {'optimal': 0, 'elevated': -2, 'critical': -8}
    adjustment = sum(counts[zone] * penalty_map[zone] for zone in counts)
    
    # Incorporate checksum as tiebreaker (bit manipulation)
    integrity_key = compute_checksum(values_only)
    final_modifier = (integrity_key % 7) - 3  # ranges from -3 to 3
    
    # Final score calculation
    score = base_score + adjustment + final_modifier
    
    # Additional distraction: unused transformation
    normalized_vals = [round((v - min(values_only)) / (max(values_only) - min(values_only)), 3) for v in values_only]
    
    return int(score)

# Key execution point
final_score = evaluate_performance(metrics_log, benchmark_config)

# Print result
print(f"Target result: {final_score}")