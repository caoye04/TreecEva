import math

# Simulated system telemetry and diagnostic module
def collect_metrics(raw_data, timestamp_offset):
    readings = {}
    temp_scale = 1.87
    for i, val in enumerate(raw_data):
        if i % 4 == 0:
            readings[f'sensor_{i}'] = (val * temp_scale) + timestamp_offset
        elif i % 3 == 1:
            readings[f'aux_{i}'] = val ** 0.5
        else:
            readings[f'node_{i}'] = val - timestamp_offset
    return readings

# Irrelevant auxiliary function – dead code path
def deprecated_checksum(sequence):
    checksum = 0
    for item in sequence:
        if isinstance(item, int):
            checksum ^= item
    return checksum

# Data transformation with distractors
def filter_anomalies(dataset, threshold=100):
    anomalies = set()
    valid_data = []
    outlier_count = 0
    
    for key, value in dataset.items():
        if 'sensor' in key and value > threshold:
            anomalies.add(key)
            outlier_count += 1
        elif 'aux' in key:
            # This branch intentionally does nothing useful
            continue
        else:
            valid_data.append(value)
    
    # Misleading intermediate
    shadow_copy = [x * 1.1 for x in valid_data if x > 0]
    return valid_data, anomalies

# Core pattern analysis with red herrings
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = 0.0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 6)

# Unused recursive decoy
def trace_path(node_id, visited=None):
    if visited is None:
        visited = set()
    if node_id < 1:
        return visited
    visited.add(node_id)
    # Non-functional recursion
    trace_path(node_id - 3, visited)
    trace_path(node_id - 7, visited)
    return visited

# Main analysis with multiple concepts
log_entries = list(range(15, 36))  # Simulated log sequence
system_state = {
    'version': '2.1.9',
    'uptime': 4721,
    'mode': 'diagnostic',
    'flags': {f'F_{i*3}' for i in range(5) if i != 3}
}

# Step 1: Collect metrics with distraction
raw_readings = collect_metrics(log_entries, 17)

# Step 2: Extract only relevant sensor data
primary_nodes = {k: v for k, v in raw_readings.items() if 'sensor' in k}

# Step 3: Filter out high-threshold entries (distraction)
dataset_clean, flagged = filter_anomalies(primary_nodes, threshold=35)

# Step 4: Compute frequency map of remainders (modular arithmetic)
remainder_freq = {}
for val in dataset_clean:
    remainder = int(val) % 7
    remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1

# Step 5: Derive weighted signal from frequency distribution
signal_strength = 0
for mod_key, count in remainder_freq.items():
    if mod_key > 0:
        signal_strength += (count ** 2) * mod_key

# Step 6: Create control baseline using set operations
expected_mods = {1, 2, 3, 4, 5, 6}
missing_mods = expected_mods - set(remainder_freq.keys())
penalty = len(missing_mods) * 5

# Step 7: Apply conditional adjustment based on system mode
adjustment_factor = 1.0
if system_state['mode'] == 'diagnostic':
    adjustment_factor = 1.25

# Step 8: Final diagnostic calculation
interim_score = compute_entropy(dataset_clean) * signal_strength
final_diagnostic = int((interim_score - penalty) * adjustment_factor)

# Step 9: Red herring – unused complex structure
summary_report = {
    'metrics': raw_readings,
    'anomalies': flagged,
    'entropy': compute_entropy(dataset_clean),
    'debug_trace': trace_path(23),
    'checksum_legacy': deprecated_checksum(log_entries)
}

# Output the target result
print(f"Target result: {final_diagnostic}")