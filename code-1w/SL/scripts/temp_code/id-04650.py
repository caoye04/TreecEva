import math

def collect_sensor_data():
    # Simulated sensor readings (some relevant, some red herrings)
    return {
        'temp_c': 37.5,
        'pressure_kpa': 101.3,
        'vibration_hz': 55.2,
        'humidity_pct': 45.0,
        'co2_ppm': 420,
        'o2_pct': 20.9,
        'flow_rate_lpm': 12.8,
        'voltage_v': 3.3
    }

def compute_checksum(data):
    # Irrelevant cryptographic checksum (distractor)
    chk = 0
    for val in data.values():
        chk ^= int(val * 10) % 256
    return chk

def normalize_readings(raw):
    # Normalize relevant metrics only
    normalized = {}
    for k, v in raw.items():
        if k in ['temp_c', 'vibration_hz', 'humidity_pct']:
            normalized[k] = round(v / max(raw.values()), 4)
    return normalized

def evaluate_stability(profile):
    # Complex stability logic with nested conditions (partially relevant)
    score = 0
    if profile['temp_c'] > 0.3:
        score += 2
        if profile['vibration_hz'] > 0.4:
            score += 3
            if profile['humidity_pct'] < 0.6:
                score *= 1.5
    return score

def filter_anomalies(logs):
    # Dead code path - never used in final computation
    anomalies = []
    for k, v in logs.items():
        if v > 100 or v < 0:
            anomalies.append(k)
    return anomalies

def derive_envelope(values):
    # Misleading signal processing function (not used)
    envelope = []
    for i in range(1, len(values)):
        diff = abs(values[i] - values[i-1])
        envelope.append(math.sin(diff) * math.log(diff + 1))
    return envelope

def calculate_entropy(seq):
    # Unused complexity: information theory distraction
    freq = {}
    for x in seq:
        freq[x] = freq.get(x, 0) + 1
    entropy = 0.0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

def aggregate_diagnostics(norm):
    # Core transformation: tuple-based metric packing
    metrics = (
        norm['temp_c'] * 100,
        norm['vibration_hz'] * 100,
        norm['humidity_pct'] * 100
    )
    base_score = sum(metrics) / len(metrics)
    adjustment = (metrics[0] - metrics[2]) * 0.01
    return base_score + adjustment

def apply_thresholds(result, limits):
    # Conditional expression usage (required feature)
    status = 'critical' if result > limits['high'] else ('elevated' if result > limits['medium'] else 'normal')
    correction = 10.0 if status == 'critical' else (5.0 if status == 'elevated' else 0.0)
    return result - correction, status

def analyze_metrics(diag_set, criteria):
    # Final analysis with dictionary dispatch (required feature)
    processed = {}
    temp_val = diag_set['temp_c']
    vib_val = diag_set['vibration_hz']
    hum_val = diag_set['humidity_pct']

    # Nested conditional logic with red herring branches
    if temp_val > 0.25:
        processed['thermal'] = temp_val * 1.2
        if vib_val > 0.4:
            processed['mechanical'] = vib_val * 1.5
            if hum_val < 0.7:
                processed['environmental'] = hum_val * 0.8
            else:
                processed['environmental'] = hum_val * 0.5  # unused branch
        else:
            processed['mechanical'] = vib_val * 0.6  # dead path
    else:
        processed['thermal'] = temp_val * 0.8  # not triggered

    # Key calculation embedded in distractions
    raw_index = (processed.get('thermal', 0) + 
                 processed.get('mechanical', 0) + 
                 processed.get('environmental', 0))

    # Final adjustment using min/max/average pattern (suggested paradigm)
    components = [processed[k] for k in ['thermal', 'mechanical', 'environmental'] if k in processed]
    if components:
        avg_comp = sum(components) / len(components)
        peak_comp = max(components)
        adjusted_index = (avg_comp * 0.7) + (peak_comp * 0.3)
    else:
        adjusted_index = raw_index

    # Apply threshold logic to get final diagnostic value
    final_value, _ = apply_thresholds(adjusted_index * 2, criteria)
    return final_value

# Main execution with irrelevant setup
sensor_log = collect_sensor_data()
checksum = compute_checksum(sensor_log)  # Distractor variable
anomaly_list = filter_anomalies(sensor_log)  # Unused list
signal_envelope = derive_envelope(list(sensor_log.values()))  # Dead processing
entropy_metric = calculate_entropy([int(v) for v in sensor_log.values()])  # Red herring

# Relevant data flow begins here
normalized_profile = normalize_readings(sensor_log)
system_score = evaluate_stability(normalized_profile)  # Intermediate but unused
consensus_diagnostic = aggregate_diagnostics(normalized_profile)  # Distractor result

# Critical dictionary construction (required)
thresholds = {
    'low': 30.0,
    'medium': 50.0,
    'high': 70.0
}

diagnostics = {
    'temp_c': normalized_profile['temp_c'],
    'vibration_hz': normalized_profile['vibration_hz'],
    'humidity_pct': normalized_profile['humidity_pct']
}

# Key statement
final_diagnostic = analyze_metrics(diagnostics, thresholds)
print(f"Result: {final_diagnostic}")