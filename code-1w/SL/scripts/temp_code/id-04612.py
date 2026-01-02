import numpy as np

# Simulated sensor data processing with diagnostic flags
def process_sensor_readings(raw_data, threshold=0.75):
    normalized = [x / max(raw_data) for x in raw_data]
    anomalies = [i for i, x in enumerate(normalized) if x > threshold]
    filtered = [x for x in normalized if x <= threshold]
    return filtered, anomalies

# Irrelevant helper: text parsing (red herring)
def parse_log_entry(entry):
    parts = entry.strip().split('|')
    timestamp = parts[0] if len(parts) > 0 else ''
    level = parts[1].strip() if len(parts) > 1 else 'INFO'
    message = '|'.join(parts[2:]) if len(parts) > 2 else ''
    category = 'SYSTEM' if 'sys' in message.lower() else 'USER'
    return {'ts': timestamp, 'lvl': level, 'msg': message, 'cat': category}

# Core algorithm: signal integrity evaluation
signal_chain = [18, 36, 54, 72, 90, 108, 126, 144]
baseline_offset = 12
adjusted_signal = [val - baseline_offset for val in signal_chain]

# Apply modular transformation and bit masking (relevant)
modular_mapped = [val % 17 for val in adjusted_signal]
decoy_mapped = [val % 13 for val in adjusted_signal]  # distractor
masked_values = [val & 0b1111 for val in modular_mapped]  # keep lower 4 bits

# Signal segmentation and windowing
window_size = 4
signal_windows = [masked_values[i:i+window_size] for i in range(0, len(masked_values), window_size)]

# Compute window metrics with list comprehension and slicing
window_metrics = []
for window in signal_windows:
    if len(window) == window_size:
        avg = sum(window) / len(window)
        peak = max(window)
        stability = peak - avg
        window_metrics.append((avg, peak, stability))

# Aggregate diagnostics (this part is critical)
aggregate_metrics = [round(m[0] * m[2], 3) for m in window_metrics]  # avg * stability

# System state matrix - simulated health indicators (cross-reference)
system_state = np.array([
    [1, 0, aggregate_metrics[0] if len(aggregate_metrics) > 0 else 0.0, 1],
    [0, 1, 0.5, 0],
    [aggregate_metrics[1] if len(aggregate_metrics) > 1 else 0.2, 0, 1, 0],
    [1, 1, 0, aggregate_metrics[0] if len(aggregate_metrics) > 0 else 0.1]
])

# Red herring: unused recursive function
def calculate_entropy(data, depth=0):
    if depth > 3 or len(data) == 0:
        return 0.0
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid+1:]
    p_left = len(left) / len(data) if data else 0
    return -p_left * np.log(p_left + 1e-9) + calculate_entropy(right, depth+1)

# Another decoy variable set
temporal_weights = [0.1 * (i+1) for i in range(6)]
weight_map = {i: w for i, w in enumerate(temporal_weights)}
weighted_sum = sum(weight_map.get(i, 0) * i for i in range(4))

# Correction factor derived from modular arithmetic on signal length
correction_factor = (len(signal_chain) ** 2) % 11

# Final diagnostic computation — KEY STATEMENT
final_diagnostic = aggregate_metrics[-1] + system_state.sum() * correction_factor

# Print result for evaluation
print(f"Result: {final_diagnostic}")