import math

# System telemetry simulation for distributed node health analysis
def generate_telemetry_data(base_id, node_count):
    data = {}
    for i in range(node_count):
        node_id = f'{base_id}-{i:02d}'
        raw_signal = (i ** 2 + 3 * i + 7) % 11
        normalized = math.sin(raw_signal / 3.0)
        status_flag = int(abs(normalized * 100)) % 4
        data[node_id] = {
            'signal': raw_signal,
            'norm': round(normalized, 4),
            'flag': status_flag,
            'active': status_flag in [0, 1]
        }
    return data

# Irrelevant helper - looks important but unused in critical path
def compute_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Decoy function that simulates calibration but does nothing useful
def calibrate_sensors(log_data, threshold=0.75):
    calibrated = {}
    for k, v in log_data.items():
        adj_norm = v['norm'] * 0.9 if abs(v['norm']) > threshold else v['norm'] * 1.1
        calibrated[k] = {**v, 'adjusted': round(adj_norm, 4)}
    # This function is called but its result discarded
    return calibrated

# Core diagnostic engine
def extract_diagnostic_keys(telemetry):
    flags = [v['flag'] for v in telemetry.values()]
    actives = [k for k, v in telemetry.items() if v['active']]
    inactive_count = len(telemetry) - len(actives)
    
    # Real computation begins here
    pattern_sum = sum(flags[i] * (i + 1) for i in range(len(flags)))
    shift_factor = (pattern_sum % 7) + 1
    
    # Transform active node IDs into numeric signatures
    base_values = []
    for node in actives:
        suffix = int(node.split('-')[1])
        base_values.append((suffix * shift_factor) % 13)
    
    return base_values, actives, inactive_count, shift_factor

# Set operations used meaningfully
def detect_anomalies(values, reference_pool):
    current_set = set(values)
    known_issues = {5, 7, 9, 11}
    potential_risks = {2, 4, 8, 10}
    
    confirmed = current_set & known_issues
    suspected = current_set & potential_risks
    
    # Distractor: complex but irrelevant scoring
    risk_score = 0
    for val in suspected:
        risk_score += val * 3
    for val in confirmed:
        risk_score += val * 7
    
    # Actual relevant output
    return len(confirmed) > 0, len(suspected), risk_score  # risk_score is ignored later

# Main analyzer with red herrings and distractions
def analyze_fault_pattern(signature, active_list):
    # Extraneous transformations
    transformed = [((x ** 2 + 2 * x + 1) % 17) for x in signature]
    filtered = [x for x in transformed if x % 2 == 1]  # keep only odds
    
    # Fake checksum that looks important
    fake_checksum = 0
    for idx, val in enumerate(filtered):
        fake_checksum += val * (idx + 1) * (-1) ** idx
    fake_checksum = abs(fake_checksum) % 1000
    
    # Real logic: count unique modulo clusters
    clusters = {}
    for val in filtered:
        key = val % 5
        clusters[key] = clusters.get(key, 0) + 1
    
    # Secondary distraction: string-based encoding of node names
    encoded_names = []
    for name in active_list:
        enc = sum(ord(c) - 96 for c in name.lower() if c.isalpha())
        encoded_names.append(enc % 19)
    
    # Combine cluster distribution with encoded name hash
    name_hash = sum(encoded_names) % 11
    cluster_score = sum(v * (k + 1) for k, v in clusters.items())
    
    # Final computation - this is the actual answer
    intermediate = (cluster_score * 2) + (name_hash * 3) + (len(filtered) * 5)
    final_diagnostic = (intermediate ^ 987) & 1023  # Bitwise mix with mask
    
    # Dead code branch - never executed but looks relevant
    if False:
        backup = 0
        for c in clusters:
            backup += c * 123
        final_diagnostic = min(final_diagnostic, backup)
    
    return final_diagnostic

# Initialization sequence with misleading comments
node_telemetry = generate_telemetry_data('SYSX', 12)

discarded_calibration = calibrate_sensors(node_telemetry, threshold=0.85)  # Result not used

# Extract core diagnostic elements
diag_keys, active_nodes, inactive_node_count, shift = extract_diagnostic_keys(node_telemetry)

# Anomaly detection - partially used, partially ignored
has_critical, suspect_count, score_risk = detect_anomalies(diag_keys, list(range(1, 15)))

# String manipulation decoy
node_string = ''.join([nid.split('-')[1] for nid in active_nodes])
temp_value = int(node_string[:2]) * len(node_string) if len(node_string) >= 2 else 0

# Build system signature using multiple sources (some irrelevant)
system_signature = []
for i, key in enumerate(diag_keys):
    # Mix position, value, and external factors
    mixed = key ^ (i * shift) ^ suspect_count
    system_signature.append(mixed)

# Critical execution point
final_diagnostic = analyze_fault_pattern(system_signature, active_nodes)

# Output required result
print(f"Result: {final_diagnostic}")