import math

def analyze_signal(pattern):
    if len(pattern) < 3:
        return 0
    magnitude = sum(x ** 2 for x in pattern)
    norm = math.sqrt(magnitude)
    normalized = [x / norm for x in pattern]
    return sum(math.sin(x) for x in normalized)


def compute_entropy(sequence):
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)


def decode_payload(payload_str):
    chunks = payload_str.split('|')
    filtered = [c for c in chunks if c.startswith('DAT')]
    values = []
    for chunk in filtered:
        try:
            num = int(chunk[3:])
            values.append(num)
        except ValueError:
            continue
    return values if values else [0]


def validate_checksum(data_list):
    if not data_list:
        return False
    checksum = sum(d % 7 for d in data_list)
    return checksum % 5 == 0


def transform_coordinates(coord_list):
    # Irrelevant geometric transformation (dead path)
    result = []
    for x, y in coord_list:
        rotated_x = x * math.cos(math.pi / 4) - y * math.sin(math.pi / 4)
        rotated_y = x * math.sin(math.pi / 4) + y * math.cos(math.pi / 4)
        result.append((rotated_x, rotated_y))
    return result


def aggregate_diagnostics(metrics_dict):
    # Real computation: weighted average of specific fields
    weights = {'latency': 0.3, 'jitter': 0.2, 'bandwidth': 0.5}
    score = 0.0
    for key, weight in weights.items():
        if key in metrics_dict:
            score += metrics_dict[key] * weight
    
    # Distractor: unused complex logic
    outliers = [k for k, v in metrics_dict.items() if v > 90]
    correction_factor = len(outliers) * 0.1
    
    return score  # correction_factor not applied


def process_logs(raw_log):
    lines = raw_log.strip().split('\n')
    timestamps = []
    events = []
    for line in lines:
        parts = line.split(' ', 2)
        if len(parts) == 3:
            ts_str, level, msg = parts
            timestamps.append(int(ts_str))
            events.append(msg.lower())
    event_summary = {ev: events.count(ev) for ev in set(events)}
    avg_gap = sum(timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))) / (len(timestamps) - 1) if len(timestamps) > 1 else 0
    return {'gaps': avg_gap, 'count': len(timestamps), 'summary': event_summary}


def evaluate_circuit(voltage, resistance, temperature=25):
    # Physics-based distraction
    base_current = voltage / (resistance + 1e-9)
    temp_factor = 1 + (temperature - 25) * 0.003
    adjusted_current = base_current * temp_factor
    power = voltage * adjusted_current
    return {'current': adjusted_current, 'power': power}


def main_pipeline(input_str, config_map):
    # Parse input
    payload_values = decode_payload(input_str)
    
    # Irrelevant signal analysis
    signal_pattern = [payload_values[i] % 10 for i in range(len(payload_values)) if i % 2 == 0]
    signal_score = analyze_signal(signal_pattern)
    
    # Validate structure
    is_valid = validate_checksum(payload_values)
    
    # Generate dummy coordinates from data (distraction)
    coords = [(payload_values[i], payload_values[i+1]) for i in range(0, len(payload_values)-1, 2)]
    transformed_coords = transform_coordinates(coords)
    
    # Compute entropy of digits (semi-relevant)
    digit_seq = []
    for val in payload_values:
        digit_seq.extend([int(d) for d in str(abs(val))])
    entropy = compute_entropy(digit_seq)
    
    # Build log-like structure from string fragments (red herring)
    fake_log = "\n".join([
        f"100000{i} INFO System initialized with code {v}" for i, v in enumerate(payload_values[:3])
    ])
    log_analysis = process_logs(fake_log)
    
    # Real metric construction
    metrics = {
        'latency': config_map.get('base_delay', 40) + payload_values[-1] % 20,
        'jitter': 100 - entropy * 10,
        'bandwidth': 80 if is_valid else 60
    }
    
    # Evaluate circuit with irrelevant parameters (decoy)
    circuit_diag = evaluate_circuit(5.0, 1000.0, 35)
    
    # Final aggregation (this is where answer comes from)
    final_diagnostic = aggregate_diagnostics(metrics)
    
    # Unused but misleading variable
    final_diagnostic_adjusted = final_diagnostic * (1 + signal_score * 0.01)
    
    return final_diagnostic

# Simulated system data
log_data = "DAT123|CHK77|DAT456|META|DAT789"
system_state = {
    'base_delay': 45,
    'mode': 'high_throughput',
    'threshold': 85,
    'debug': True,
    'nodes': ["A1", "B2", "C3"]
}

# Key execution point
final_diagnostic = process_metrics(log_data, system_state)

# Renamed function to match call
def process_metrics(data, state):
    return main_pipeline(data, state)

print(f"Result: {final_diagnostic}")