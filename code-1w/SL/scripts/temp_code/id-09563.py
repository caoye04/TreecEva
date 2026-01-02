from collections import defaultdict, Counter

# System health monitoring simulation with red herrings and complex logic

def simulate_sensor_noise(data, factor=1.03):
    return [x * factor + 1.5 for x in data]  # Distractor function - not used in critical path

def deprecated_checksum(seq):
    return sum(seq) % 17  # Unused legacy function (dead code)

def evaluate_stability(ring_buffer, tolerance=0.05):
    if len(ring_buffer) < 2:
        return False
    return abs(ring_buffer[-1] - ring_buffer[-2]) < tolerance

def accumulate_diagnostics(log_entries):
    diagnostics = defaultdict(float)
    severity_map = {'INFO': 1, 'WARN': 2, 'ERROR': 4}
    for entry in log_entries:
        level = entry.get('level', 'INFO')
        diagnostics['total_events'] += 1
        diagnostics['risk_score'] += severity_map.get(level, 1)
    return diagnostics  # Computation partially used but not decisive

def recursive_filter(values, depth=0):
    if depth >= 3 or not values:
        return [v for v in values if v > 0]  # Early termination
    return recursive_filter([v - 0.1 for v in values], depth + 1)

def compute_entropy(sequence):
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return entropy  # Red herring: looks important but unused in final result

def analyze_metrics(state, limits):
    # Core logic embedded within distractions
    temp_history = state.get('temperatures', [])
    pressure_seq = state.get('pressures', [])
    
    # Irrelevant preprocessing
    normalized_temps = [t / 100 for t in temp_history if t > 0]
    filtered_pressures = [p for p in pressure_seq if p > limits['pressure']['min']]
    
    # Real computation begins
    temp_avg = sum(temp_history) / len(temp_history) if temp_history else 0
    pressure_avg = sum(pressure_seq) / len(pressure_seq) if pressure_seq else 0
    
    # Key intermediate: correlation proxy
    if len(temp_history) == len(pressure_seq) and len(temp_history) > 0:
        cov = sum((temp_history[i] - temp_avg) * (pressure_seq[i] - pressure_avg) 
                  for i in range(len(temp_history)))
        var_t = sum((t - temp_avg) ** 2 for t in temp_history) or 1
        correlation = cov / (var_t ** 0.5 * (sum((p - pressure_avg)**2 for p in pressure_seq)**0.5))
    else:
        correlation = 0.0
    
    # Misleading branch
    if temp_avg > limits['temperature']['max']:
        base_risk = 80
    elif pressure_avg < limits['pressure']['min']:
        base_risk = 60
    else:
        base_risk = 20
    
    # Critical logic buried here
    trend_consistency = 0
    for i in range(1, len(temp_history)):
        if (temp_history[i] - temp_history[i-1]) > 0 == (pressure_seq[i] - pressure_seq[i-1]) > 0:
            trend_consistency += 1
    
    consistency_ratio = trend_consistency / (len(temp_history) - 1) if len(temp_history) > 1 else 0
    
    # Final calculation (depends on consistency_ratio and base_risk)
    adjustment = int(consistency_ratio * 40)
    final_risk = base_risk - adjustment
    
    # Answer-determining transformation
    final_diagnostic = abs(final_risk - 7) * 10  # Deterministic outcome
    
    return final_diagnostic

# Simulated system state (real input)
system_state = {
    'temperatures': [85, 90, 95, 100, 105],
    'pressures': [110, 108, 106, 104, 102],
    'vibration': [0.1, 0.2, 0.15],  # Unused field
    'uptime_hours': 127.5  # Irrelevant data
}

# Threshold definitions
thresholds = {
    'temperature': {'min': 70, 'max': 100},
    'pressure': {'min': 100, 'max': 120}
}

# Decoy data structures
diag_log = [
    {'timestamp': 'T1', 'level': 'INFO', 'msg': 'OK'},
    {'timestamp': 'T2', 'level': 'WARN', 'msg': 'Advisory'}
]

ring_buf = [0.5, 0.49, 0.51, 0.5]

# Unused statistical transform
entropy_value = compute_entropy(['A', 'B', 'A', 'C', 'B', 'A'])

# Main execution path obscured by noise
raw_sens = [80, 82, 81]
simulate_sensor_noise(raw_sens)

# Actual key call
final_diagnostic = analyze_metrics(system_state, thresholds)

# Print required output
print(f"Target result: {final_diagnostic}")