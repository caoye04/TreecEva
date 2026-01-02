from collections import defaultdict, Counter

# Simulated sensor data processing pipeline for a distributed system health monitor
def process_node_readings(raw_readings):
    processed = []
    temp_buffer = []
    cumulative_noise = 0

    for entry in raw_readings:
        node_id = entry['id']
        timestamp = entry['ts']
        power_draw = entry['power']
        thermal_flux = entry['temp']
        signal_jitter = entry.get('jitter', 0)

        # Irrelevant noise accumulation (red herring)
        cumulative_noise += signal_jitter * 0.03
        if cumulative_noise > 5:
            cumulative_noise *= 0.8

        # Real processing: detect anomalies
        anomaly_score = 0
        if power_draw > 90:
            anomaly_score += 2
        if thermal_flux > 75:
            anomaly_score += 3
        if signal_jitter > 100:
            anomaly_score += 1

        # Distractor: unused transformation
        normalized_flux = round((thermal_flux / 100) ** 0.5, 4)
        adjusted_power = power_draw * (1 + min(signal_jitter, 50) / 200)

        temp_buffer.append(normalized_flux)  # Unused

        processed.append({
            'node': node_id,
            'score': anomaly_score,
            'critical': anomaly_score >= 4,
            'timestamp': timestamp
        })

    return processed


def generate_timing_profile(nodes):
    profile = defaultdict(float)
    checkpoint_tags = ['init', 'diag', 'io', 'net', 'final']

    for i, node in enumerate(nodes):
        base_delay = len(node['node']) * 0.15
        penalty = node['score'] * 0.07

        # Meaningful metric: timing per phase
        for j, tag in enumerate(checkpoint_tags):
            delay = base_delay + penalty + (j * 0.02) * (i % 2)
            profile[tag] += delay

        # Dead code path: never accessed later
        if i == len(nodes) - 1:
            backup_entry = {k: v * 1.1 for k, v in profile.items()}
            for k in backup_entry:
                backup_entry[k] -= 0.05

    # Another distractor: irrelevant scaling
    scaled = [profile[t] * 1.05 for t in checkpoint_tags]
    offset_value = sum(scaled) * 0.01  # Unused

    return dict(profile)

# Legacy compatibility layer (unused but looks important)
def deprecated_aggregation(data_list, mode='legacy'):
    if mode == 'legacy':
        return sum(d.get('score', 0) for d in data_list) // len(data_list)
    else:
        return max(d.get('score', 0) for d in data_list)

# Core logic disguised among distractions
def validate_system_integrity(node_list, thresholds):
    stats = Counter()
    diagnostic_key = ''
    entropy_pool = 0.0

    for idx, node in enumerate(node_list):
        stats['total_nodes'] += 1
        if node['critical']:
            stats['unstable'] += 1
            # Fake entropy calculation
            entropy_pool += (idx + 1) * 0.33

        # Fake state tracking
        state_vector = [node['score'] * (i+1) for i in range(4)]
        pivot = state_vector[2] if len(state_vector) > 2 else 0
        if pivot > 5:
            diagnostic_key += 'X'
        else:
            diagnostic_key += 'O'

    # Real logic: determine integrity level
    if stats['unstable'] == 0:
        level = 'STABLE'
    elif stats['unstable'] < 3:
        level = 'CAUTION'
    else:
        level = 'CRITICAL'

    # Unused final key hash
    hashed_key = ''.join([chr(ord(c) ^ 3) for c in diagnostic_key])

    return level, dict(stats)

# Final aggregation with subtle arithmetic chain
def aggregate_metrics(timing_log, system_state):
    base_metric = 0
    adjustment_factor = 1.0

    # Extract meaningful values through indirect means
    phases = ['init', 'diag', 'io', 'net', 'final']
    for i, phase in enumerate(phases):
        if phase in timing_log:
            base_metric += timing_log[phase] * (i + 1) * 10

    # Use system_state indirectly
    unstable_count = system_state.get('unstable', 0)
    total_nodes = system_state.get('total_nodes', 1)

    # Critical formula hidden among distractions
    stability_ratio = (total_nodes - unstable_count) / total_nodes
    adjustment_factor = 2 - stability_ratio  # Inverse relationship

    intermediate = base_metric * adjustment_factor

    # Distractor: complex but unused bit manipulation
    bit_encoded = int(intermediate)
    for _ in range(3):
        bit_encoded = (bit_encoded ^ (bit_encoded >> 4)) & 0xFFFF
    final_checksum = bit_encoded ^ 0xABCD

    # Actual answer computation (non-obvious)
    result = int(intermediate)  # Truncated integer of weighted timing sum

    # Red herring: floating point residue
    residue = intermediate - result
    if residue > 0.5:
        result += 1

    return result

# --- Main Execution ---
if __name__ == '__main__':
    # Input data - realistic sensor readings
    sensor_data = [
        {'id': 'A10', 'ts': 1623456781, 'power': 88, 'temp': 70, 'jitter': 45},
        {'id': 'B20', 'ts': 1623456782, 'power': 95, 'temp': 78, 'jitter': 110},
        {'id': 'C30', 'ts': 1623456783, 'power': 87, 'temp': 72, 'jitter': 30},
        {'id': 'D40', 'ts': 1623456784, 'power': 92, 'temp': 80, 'jitter': 65},
        {'id': 'E50', 'ts': 1623456785, 'power': 85, 'temp': 68, 'jitter': 20}
    ]

    # Step 1: Process raw readings
    analyzed_nodes = process_node_readings(sensor_data)

    # Step 2: Generate timing behavior profile
    timing_profile = generate_timing_profile(analyzed_nodes)

    # Step 3: Validate overall system state
    integrity_level, node_stats = validate_system_integrity(analyzed_nodes, thresholds={'max_unstable': 2})

    # Step 4: Compute final diagnostic metric
    final_diagnostic = aggregate_metrics(timing_profile, node_stats)

    # Output target variable
    print(f"Target result: {final_diagnostic}")