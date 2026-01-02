from collections import defaultdict, Counter
import itertools

# Simulated system telemetry data
telemetry_stream = [
    'ERR@23|CPU:95|MEM:80|DISK:45',
    'OK@24|CPU:60|MEM:70|DISK:50',
    'ERR@25|CPU:90|MEM:85|DISK:30',
    'ERR@26|CPU:98|MEM:88|DISK:20',
    'OK@27|CPU:55|MEM:60|DISK:60'
]

# Irrelevant decoy data (distractor)
decoys = ['X@1|A:1', 'Y@2|B:2', 'Z@3|C:3']
phantom_map = {f'key_{i}': f'value_{i*2}' for i in range(10)}

# Parse raw logs into structured format
def parse_log_entry(entry):
    status_marker, readings = entry.split('|', 1)
    timestamp = int(status_marker.split('@')[1][:2])
    metrics = {}
    for reading in readings.split('|'):
        k, v = reading.split(':')
        metrics[k] = float(v)
    return status_marker.startswith('ERR'), timestamp, metrics

# Distractor function – never called
def legacy_calibrate(data):
    accumulator = 0
    for x in data:
        accumulator += x ** 2 - x
    return accumulator // 2 if accumulator > 0 else 0

# Another decoy: complex but unused transformation
token_chains = [list(itertools.combinations(['a','b','c'], r)) for r in [1,2]]
shadow_weights = defaultdict(lambda: 0.5)
for i in range(5):
    shadow_weights[f'aux_{i}'] = i * 0.33

# Core processing functions
def filter_critical_entries(logs):
    criticals = []
    for entry in logs:
        is_error, ts, data = parse_log_entry(entry)
        if is_error and data['CPU'] > 90:
            criticals.append((ts, data))
    return criticals

def compute_stress_factor(records):
    if not records:
        return 0.0
    cpu_vals = [r[1]['CPU'] for r in records]
    mem_vals = [r[1]['MEM'] for r in records]
    avg_cpu = sum(cpu_vals) / len(cpu_vals)
    avg_mem = sum(mem_vals) / len(mem_vals)
    peak_disk_drop = max([r[1]['DISK'] for r in records]) - min([r[1]['DISK'] for r in records])
    # Complex formula with red herring terms
    stress = (avg_cpu * 0.6 + avg_mem * 0.3) * (1.0 + peak_disk_drop / 100.0)
    adjustment = 0
    for val in cpu_vals:
        if val > 95:
            adjustment += 2.5  # bonus per severe spike
    return round(stress + adjustment, 4)

def detect_pattern_sequence(entries):
    # Use string method as required
    raw = ''.join(e[:3] for e in entries)
    count_err = raw.count('ERR')
    count_ok = raw.count('OK')
    ratio = count_err / (count_ok + 1)
    # Real pattern: at least 3 ERRs with OK gaps?
    tokens = raw.split('OK')
    has_long_burst = any(len(t) >= 6 for t in tokens)  # 'ERRERRERR' = 9 chars
    return ratio > 1.0 and has_long_burst

# Main analysis pipeline
def process_metrics(stream, thresholds):
    # Unrelated counter (distractor)
    char_counter = Counter(itertools.chain.from_iterable(stream))
    temp_bias = sum(char_counter.values()) / len(char_counter) if char_counter else 0

    filtered_records = filter_critical_entries(stream)
    base_stress = compute_stress_factor(filtered_records)

    # Dead code path — only runs if impossible condition met
    diagnostic_codes = []
    for i, (_, m) in enumerate(filtered_records):
        code = 0
        if m['MEM'] > thresholds['MEM']:
            code |= 1
        if m['DISK'] < thresholds['DISK']:
            code |= 2
        if i % 2 == 0:
            code |= 4
        diagnostic_codes.append(code)
    
    # Key computation
    pattern_flag = detect_pattern_sequence(stream)
    anomaly_multiplier = 1.75 if pattern_flag else 1.0
    
    # Final integration with distractors
    phantom_sum = sum(int(k[-1]) for k in phantom_map.keys() if 'key_' in k)  # 0+1+...+9 = 45
    decoy_effect = len(decoys) * 0.1  # 0.3
    
    intermediate = base_stress * anomaly_multiplier
    final_score = intermediate - decoy_effect + (temp_bias * 0.01)  # negligible
    
    # Actual answer derived here
    final_diagnostic = int(round(final_score * 100))
    
    # Red herring print (not part of logic)
    debug_snapshot = {"stress": base_stress, "multiplier": anomaly_multiplier}
    
    return final_diagnostic

# Threshold configuration (real parameter)
system_thresholds = {'MEM': 82, 'DISK': 25}

# Execution point
final_diagnostic = process_metrics(telemetry_stream, system_thresholds)
print(f"Target result: {final_diagnostic}")