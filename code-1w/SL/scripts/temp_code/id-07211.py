import math

# System health monitoring simulation with data transformation and diagnostic logic

def collect_sensor_readings():
    return {
        'temp': [23.4, 24.1, 25.0, 26.8, 22.9],
        'pressure': [101.3, 102.1, 99.7, 100.5, 103.2],
        'vibration': [0.05, 0.07, 0.04, 0.12, 0.09]
    }

def apply_calibration(data, factor=1.02):
    calibrated = {}
    for key, values in data.items():
        # Irrelevant scaling (distraction)
        offset = 0.1 if key == 'temp' else 0
        calibrated[key] = [(v * factor) + offset for v in values]
    return calibrated

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0
    probs = [(v / total) for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def transform_data_packet(packet):
    # Complex transformation with red herring operations
    temp_stats = {
        'mean': sum(packet['temp']) / len(packet['temp']),
        'range': max(packet['temp']) - min(packet['temp']),
        'entropy': compute_entropy([int(x) for x in packet['temp']])
    }

    pressure_stats = {
        'mean': sum(packet['pressure']) / len(packet['pressure']),
        'stdev': (sum((x - sum(packet['pressure'])/len(packet['pressure']))**2 
                     for x in packet['pressure']) / len(packet['pressure'])) ** 0.5,
        'trend': packet['pressure'][-1] - packet['pressure'][0]
    }

    vibration_alerts = [v > 0.1 for v in packet['vibration']]
    spike_count = sum(vibration_alerts)  # Distractor metric

    # Dummy transformation chain
    processed_values = list(map(lambda x: round(x * 1.01, 2), packet['temp']))
    checksum = sum(int(str(int(v)).zfill(2)[-2]) for v in processed_values) * 1.07

    # Real transformation used later
    normalized_vibration = [v / 0.15 for v in packet['vibration']]
    energy_estimate = sum([v**2 for v in normalized_vibration])

    # Dead code path — never accessed
    def analyze_pattern(seq):
        return all(abs(seq[i] - seq[i-1]) < 1 for i in range(1, len(seq)))

    return {
        'thermal_load': temp_stats['mean'] * 1.8 + 32,
        'pressure_stability': 100 - (pressure_stats['stdev'] * 10),
        'energy_index': energy_estimate,
        'anomaly_score': spike_count * checksum,
        'baseline_shift': temp_stats['range'],
        'calibration_offset': checksum  # Misleading value
    }

def evaluate_system_risk(metrics):
    # Unused risk evaluation function (decoy)
    score = 0
    if metrics['thermal_load'] > 75:
        score += 3
    if metrics['pressure_stability'] < 85:
        score += 4
    return 'CRITICAL' if score >= 5 else 'STABLE'

def aggregate_diagnostics(diag_list):
    cumulative = 0
    weights = [0.3, 0.5, 0.2]
    for i, d in enumerate(diag_list):
        cumulative += d['energy_index'] * weights[i % 3]
    return cumulative

def generate_synthetic_sample(count):
    # Irrelevant synthetic data generator (dead path)
    return [{'dummy_metric': (i * 1.7) % 50} for i in range(count)]

def filter_outliers(data, threshold=2.5):
    # Unused filtering logic (distractor)
    mean_val = sum(data) / len(data)
    stdev = (sum((x - mean_val)**2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * stdev]

def process_metrics(metrics, config):
    base = 0
    if config['mode'] == 'diagnostic':
        base += metrics['energy_index'] * config['gain']
        base -= metrics['baseline_shift'] * 1.5
        if metrics['pressure_stability'] > 90:
            adjustment = math.sin(math.pi / 6)
            base *= (1 + adjustment)
        else:
            base *= 0.9
    elif config['mode'] == 'emergency':
        base = 1000  # Unused branch
    return int(round(base))

# Main execution flow with mixed concerns
raw_data = collect_sensor_readings()

# Apply irrelevant calibration (only partially used)
decoy_data = apply_calibration(raw_data, factor=1.05)

data_packs = [transform_data_packet(raw_data)]

# Generate unused synthetic samples (red herring)
synthetic_pool = generate_synthetic_sample(10)

# Aggregate from single item (misleading complexity)
diagnostic_list = data_packs
composite_energy = aggregate_diagnostics(diagnostic_list)

# Configuration with misleading fields
config = {
    'mode': 'diagnostic',
    'gain': 2.1,
    'timeout': 300,
    'retries': 3,
    'threshold_set': 'strict',
    'debug_mode': False
}

# Key statement: final diagnostic computation
final_diagnostic = process_metrics(data_packs[0], config)

print(f"Result: {final_diagnostic}")