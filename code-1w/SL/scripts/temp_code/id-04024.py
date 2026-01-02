import math

# Simulated network node diagnostic system
def analyze_node(node_data, threshold=0.75):
    signal_strength = node_data.get('signal', 0)
    error_rate = node_data.get('errors', 1)
    uptime_ratio = node_data.get('uptime', 0) / 86400

    # Irrelevant computation (distractor)
    hypothetical_bandwidth = (signal_strength * 1000) / (error_rate + 1e-5)
    normalized_jitter = abs(math.sin(signal_strength)) * uptime_ratio

    if uptime_ratio < 0.5:
        return False

    # Core logic: node is stable if signal is strong and errors are low
    stability_score = signal_strength * (1 - error_rate) * uptime_ratio
    return stability_score > threshold

# Decoy function – looks related but never called in critical path
def evaluate_cluster_health(nodes):
    total_load = sum(n.get('load', 0) for n in nodes)
    avg_response = sum(n.get('response_time', 0) for n in nodes) / len(nodes)
    return total_load < 500 and avg_response < 150

# Data transformation pipeline with red herrings
def transform_logs(raw_entries):
    cleaned = []
    for entry in raw_entries:
        if 'corrupted' in entry or len(entry) < 3:
            continue
        # Use slicing and string methods (required feature)
        processed = {k.strip().lower(): v for k, v in entry.items()}
        processed['source'] = processed['source'][::-1].upper()  # Reverse string
        processed['tags'] = [t.upper().replace('_', '-') for t in processed.get('tags', [])]
        cleaned.append(processed)
    return cleaned

# Recursive aggregation function (required paradigm)
def recursive_sum(data_list, index=0):
    if index >= len(data_list):
        return 0
    current = data_list[index].get('diagnostic_value', 0)
    # Irrelevant recursion side calculation
    bonus = 1 if current > 50 else 0.5
    return current + bonus + recursive_sum(data_list, index + 1)

# Set-based interference function (distractor)
def compute_coverage(zones_configured, zones_active):
    expected = set(zones_configured)
    actual = set(zones_active)
    missing = expected - actual
    redundant = actual - expected
    return {
        'coverage': len(actual & expected) / len(expected) if expected else 0,
        'missing_zones': list(missing),
        'extra_zones': list(redundant)
    }

# Real aggregation logic obscured among distractions
def aggregate_metrics(nodes):
    valid_nodes = [node for node in nodes if analyze_node(node)]

    # Extract values using slicing on sorted list (required feature)
    scores = sorted([n['signal'] * (1 - n['errors']) for n in valid_nodes])
    mid_range = scores[len(scores)//4 : 3*len(scores)//4]  # Central 50%

    if not mid_range:
        return 0.0

    # Compute trimmed average (resistant to outliers)
    trimmed_avg = sum(mid_range) / len(mid_range)

    # Dead code path – looks important but unused
    peak_moment = None
    for i, val in enumerate(mid_range):
        if val == max(mid_range):
            peak_moment = i
            break

    # Hidden bit manipulation distractor
    magic_offset = 0
    for val in mid_range[:3]:
        shifted = int(val * 10) & 0xFF  # Bitwise AND as distraction
        magic_offset ^= shifted  # XOR accumulation (unused)

    # Final result based on statistical center
    final_score = round(trimmed_avg * 100, 4)  # Scale and round

    # This line contains the key assignment
    final_diagnostic = final_score
    return final_diagnostic

# --- MAIN EXECUTION WITH DISTRACTING SETUP ---
if __name__ == "__main__":

    # Simulated input data with misleading fields
    network_nodes = [
        {'signal': 0.81, 'errors': 0.1, 'uptime': 70000, 'load': 45, 'response_time': 120, 'diagnostic_value': 67},
        {'signal': 0.92, 'errors': 0.05, 'uptime': 80000, 'load': 67, 'response_time': 95, 'diagnostic_value': 88},
        {'signal': 0.45, 'errors': 0.3, 'uptime': 30000, 'load': 200, 'response_time': 250, 'diagnostic_value': 23},  # unstable
        {'signal': 0.73, 'errors': 0.2, 'uptime': 77000, 'load': 89, 'response_time': 140, 'diagnostic_value': 59},
        {'signal': 0.88, 'errors': 0.08, 'uptime': 86000, 'load': 54, 'response_time': 110, 'diagnostic_value': 80}
    ]

    # Unused dataset (red herring)
    legacy_system_logs = [
        {'src': 'srv1', 'corrupted': True, 'data_len': 12},
        {'src': 'gw2', 'timestamp': '2023-09-12', 'data_len': 45}
    ]

    # Distractor variables
    baseline_calibration = [0.77, 0.83, 0.69, 0.74]
    system_wide_gain = math.log(1 + sum(baseline_calibration))
    active_zones = ['A1', 'B2', 'C3', 'D4']
    configured_zones = ['A1', 'B2', 'C3', 'E5']

    # Transform logs (useless here)
    transformed = transform_logs(legacy_system_logs)

    # Call coverage (dead end)
    coverage_report = compute_coverage(configured_zones, active_zones)

    # Real work begins here
    total_diagnostic_sum = recursive_sum(network_nodes)

    # Key execution point
    final_diagnostic = aggregate_metrics(network_nodes)

    # Output required format
    print(f"Target result: {final_diagnostic}")