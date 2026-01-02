import math

def preprocess_signal(raw_data):
    # Irrelevant preprocessing (dead path)
    filtered = [x * 0.98 for x in raw_data if x > -50]
    return [math.sin(x / 10) for x in filtered]

def compute_checksum(sequence):
    # Distractor function: looks important but unused
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= int(val) ^ i
    return chk

def evaluate_health_index(metrics, profile):
    # Unused health model (red herring)
    base = sum(metrics) / len(metrics)
    adjustment = profile.get('sensitivity', 1.0)
    return base * adjustment ** 2

def decode_bit_pattern(flag):
    # Bit manipulation distractor
    bits = bin(flag)[2:].zfill(8)
    ones = bits.count('1')
    parity = ones % 2
    return parity == 1

def simulate_propagation(values, factor=0.93):
    # Misleading simulation with no effect on result
    result = []
    acc = 0
    for v in values:
        acc += v * factor
        result.append(acc)
    return result

def generate_synthetic_series(n):
    # Dead code path: generates data not used
    series = [1]
    for i in range(1, n):
        series.append(series[i-1] + (i % 3))
    return series

def normalize_readings(readings):
    # Real but indirectly used function
    min_r, max_r = min(readings), max(readings)
    if max_r == min_r:
        return [0.0 for _ in readings]
    return [(r - min_r) / (max_r - min_r) for r in readings]

def aggregate_diagnostics(logs):
    # Complex aggregation that feeds into main logic
    stats = {}
    for entry in logs:
        key = entry['node']
        val = entry['value']
        if key not in stats:
            stats[key] = []
        stats[key].append(val)
    
    averages = {}
    for k, v_list in stats.items():
        averages[k] = sum(v_list) / len(v_list)
    
    return averages

def analyze_system_state(data, limits):
    # Core relevant function with nested logic
    normalized = normalize_readings([v for v in data.values()])
    
    # Apply thresholds per component
    violations = 0
    for i, val in enumerate(normalized):
        if val > limits.get(f'sensor_{i}', 0.85):
            violations += 1
    
    # Map components to categories (dictionary use)
    mapping = {
        'temp': ['sensor_0', 'sensor_2'],
        'pressure': ['sensor_1', 'sensor_3'],
        'flow': ['sensor_4']
    }
    
    category_scores = {k: 0 for k in mapping.keys()}
    
    for category, sensors in mapping.items():
        for s in sensors:
            idx = int(s[-1])
            if idx < len(normalized) and normalized[idx] > 0.75:
                category_scores[category] += 1
    
    # Compute weighted diagnostic score
    weights = {'temp': 1.2, 'pressure': 0.9, 'flow': 1.5}
    composite = 0.0
    for cat, score in category_scores.items():
        weight = weights.get(cat, 1.0)
        composite += score * weight
    
    # Final adjustment based on violation count (key logic)
    if violations >= 3:
        composite *= 1.8
    elif violations == 0:
        composite *= 0.7
    else:
        composite *= 1.1
    
    # Final computation involving bitwise and logical ops
    adj = (violations << 2) | 1  # bit shift and OR
    final_score = composite * adj
    
    # Key variable assignment
    final_diagnostic = int(round(final_score * 100))
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated telemetry data (real input)
    telemetry = {
        'sensor_0': 45.2,
        'sensor_1': 67.8,
        'sensor_2': 89.1,
        'sensor_3': 34.5,
        'sensor_4': 76.3
    }
    
    # Threshold configuration (used in analysis)
    thresholds = {
        'sensor_0': 0.82,
        'sensor_1': 0.78,
        'sensor_2': 0.88,
        'sensor_3': 0.80,
        'sensor_4': 0.75
    }
    
    # Unused synthetic data generation (distractor)
    dummy_sequence = generate_synthetic_series(10)
    checksum = compute_checksum(dummy_sequence)  # dead usage
    
    # Signal processing on irrelevant data
    noise_floor = [-45.1, -43.8, -46.2, -44.0, -42.5]
    processed_noise = preprocess_signal(noise_floor)
    
    # Propagate some values (no impact)
    dummy_prop = simulate_propagation([1.0, 2.0, 3.0])
    
    # Aggregate fake logs (partial red herring)
    fake_logs = [
        {'node': 'A', 'value': 10},
        {'node': 'B', 'value': 15},
        {'node': 'A', 'value': 20}
    ]
    aggregates = aggregate_diagnostics(fake_logs)
    
    # Health evaluation (unused)
    health = evaluate_health_index(list(aggregates.values()), {'sensitivity': 0.9})
    
    # Core call: produces the answer
    final_diagnostic = analyze_system_state(telemetry, thresholds)
    
    # Output result
    print(f"Target result: {final_diagnostic}")