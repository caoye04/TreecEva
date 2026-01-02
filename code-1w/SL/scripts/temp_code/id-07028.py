import itertools

# System health monitoring simulation with layered diagnostics
def monitor_subsystem(sensor_data, threshold_map):
    active_alarms = []
    for key, readings in sensor_data.items():
        baseline = sum(readings[:3]) / 3
        volatility = max(readings) - min(readings)
        if volatility > threshold_map.get(key, 10):
            active_alarms.append(f'{key}_unstable')
        status_flag = 1 if baseline > 50 else 0
        masked_flag = status_flag << 2
    return active_alarms

# Irrelevant helper - decoy function
def calculate_footprint(elements):
    footprint = 0
    for e in elements:
        if isinstance(e, str):
            footprint += len(e) * 3
    return footprint

# Core transformation pipeline
def transform_stream(raw_sequence, mode='strict'):
    shifted_values = [x * 1.5 + 2 for x in raw_sequence]
    filtered = list(filter(lambda z: z > 15, shifted_values))
    paired = list(itertools.zip_longest(filtered, [100, 200, 300], fillvalue=0))
    processed = [a + b for a, b in paired if a is not None]
    return processed

# Red herring computation branch
def legacy_compatibility_check(config_set):
    compatibility_score = 0
    for conf in config_set:
        compatibility_score += hash(conf) % 7
    temp_adjustment = compatibility_score * 0.1
    normalized = abs(temp_adjustment) % 1
    return normalized > 0.5

# Main diagnostic aggregator
def aggregate_metrics(chains, reports):
    flat_chain = [item for sublist in chains for item in sublist]
    checksum = sum(flat_chain) * 0.01
    report_summary = {}
    for r in reports:
        prefix = r.split('_')[0]
        report_summary[prefix] = report_summary.get(prefix, 0) + 1
    
    # Critical distraction block - irrelevant transformations
    intermediate_cache = {}
    for i in range(3):
        intermediate_cache[f'layer_{i}'] = [j ** (i+1) for j in range(5)]
    temp_result = [sum(v) for v in intermediate_cache.values()]
    dummy_offset = max(temp_result) // 10
    
    # Actual answer derivation path
    trigger_events = len([x for x in flat_chain if x > 40])
    scaling_factor = 1 + (len(reports) * 0.5)
    base_metric = checksum * scaling_factor
    adjustment = trigger_events * 10
    final_diagnostic = int(base_metric + adjustment - dummy_offset)  # Final assignment
    return final_diagnostic

# Simulated input data
sensor_inputs = {
    'temp_core': [45, 52, 60, 65, 70],
    'pressure_a': [30, 32, 31, 95, 40],
    'flow_rate': [20, 25, 23, 27, 85]
}
threshholds = {'temp_core': 8, 'pressure_a': 50, 'flow_rate': 50}

# Generate alarms (unused but plausible)
alerts = monitor_subsystem(sensor_inputs, threshholds)

# Processing chain generation (relevant)
data_stream = list(range(8, 16))
processing_chain = [
    transform_stream(data_stream, mode='strict'),
    transform_stream([x * 2 for x in data_stream if x % 2 == 0])
]

# Decoy configuration set
configurations = ['MODE_X', 'LEGACY_R', 'SECURE_T']
legacy_flag = legacy_compatibility_check(configurations)

# Diagnostic tags (relevant)
diagnostics = alerts + ['timing_issue', 'sync_loss', 'retry_exhausted', 'timeout_retry']

# Final aggregation - key execution point
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

print(f"Result: {final_diagnostic}")