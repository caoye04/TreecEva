import math

# System health monitoring simulation with heavy distractions
def analyze_workload(data, threshold=75):
    if not data:
        return 0
    avg_load = sum(data) / len(data)
    peak = max(data)
    stability_score = (100 - avg_load) * (1 + (peak - avg_load) / 10)
    return stability_score

def generate_report(snapshot):
    critical_count = len([x for x in snapshot if x > 90])
    warning_count = len([x for x in snapshot if 75 <= x <= 90])
    return {'critical': critical_count, 'warnings': warning_count}

def encrypt_key(key_str):
    # Irrelevant cryptographic distraction
    shifted = ''.join(chr((ord(c) - ord('a') + 7) % 26 + ord('a')) for c in key_str)
    return shifted[::-1]

def legacy_checksum(items):
    # Unused legacy function (dead code path)
    chk = 0
    for i, item in enumerate(items):
        chk ^= (item + i) % 256
    return chk

def transform_readings(raw):
    # Core transformation: apply logarithmic scaling and offset
    processed = []
    for val in raw:
        if val > 0:
            transformed = math.log(val) * 10 + 3
            processed.append(round(transformed, 2))
        else:
            processed.append(0)
    return processed

def evaluate_redundancy(nodes):
    active = [n for n in nodes if n['status'] == 'active']
    backup = [n for n in nodes if n['status'] == 'standby']
    ratio = len(active) / (len(backup) + 1)
    return ratio > 0.5

# Unused simulation function (distractor)
def simulate_failure_mode(state_vector):
    temp = state_vector.copy()
    for i in range(len(temp)):
        temp[i] = (temp[i] * 17 + 13) % 101
    return [t * 0.9 for t in temp]

# Lambda for dynamic thresholding (relevant but obscured)
dynamic_filter = lambda x, base: x > (base * 1.15)

# Main processing pipeline
raw_sensor_data = [144, 25, 81, 4, 169, 64, 9, 100]

# Distractor variables
encryption_key = 'nxvrcan'
decoded_token = encrypt_key(encryption_key)  # Irrelevant transformation

config = {
    'version': '3.7.1',
    'mode': 'diagnostic',
    'threshold': 60,
    'debug': False,
    'retries': 3
}

# Simulated node cluster (partially relevant)
node_cluster = [
    {'id': 'A1', 'status': 'active', 'load': 68},
    {'id': 'B2', 'status': 'standby', 'load': 0},
    {'id': 'C3', 'status': 'active', 'load': 83},
    {'id': 'D4', 'status': 'standby', 'load': 0}
]

# Step 1: Transform raw sensor readings using log scale
transformed_readings = transform_readings(raw_sensor_data)

# Step 2: Filter based on dynamic lambda condition
filtered_diagnostics = [x for x in transformed_readings if dynamic_filter(x, config['threshold'])]

# Step 3: Compute entropy-like measure from filtered data
entropy_proxy = 0
for val in filtered_diagnostics:
    if val > 0:
        entropy_proxy -= (val / 100) * math.log(val / 100)

# Step 4: Generate auxiliary metrics
snapshot_summary = generate_report([node['load'] for node in node_cluster if node['status'] == 'active'])
system_stability = analyze_workload([node['load'] for node in node_cluster if node['load'] > 0], config['threshold'])

# Step 5: Combine into composite data structure
composite_metrics = {
    'readings': transformed_readings,
    'filtered': filtered_diagnostics,
    'entropy': round(entropy_proxy, 4),
    'stability': round(system_stability, 2),
    'summary': snapshot_summary,
    'timestamp': '2023-11-05T14:32:00Z',
    'node_ratio_valid': evaluate_redundancy(node_cluster)
}

# Step 6: Apply final transformation using higher-order logic
scaling_factor = 2.5 if composite_metrics['node_ratio_valid'] else 1.8
adjusted_entropy = composite_metrics['entropy'] * scaling_factor

# Step 7: Process through diagnostic engine
process_metrics = lambda data, cfg: (
    int(
        (sum(data['filtered']) + data['stability']) * 
        (data['summary']['warnings'] + 1) + 
        adjusted_entropy
    )
)

# Critical execution point
final_diagnostic = process_metrics(composite_metrics, config)

# Final irrelevant computation (red herring)
temporal_hash = 0
for c in config['version']:
    if c.isdigit():
        temporal_hash = (temporal_hash * 13 + int(c)) % 97

print(f"Result: {final_diagnostic}")