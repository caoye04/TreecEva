import math

# Simulated sensor data preprocessing pipeline for environmental monitoring system
def collect_readings():
    raw_samples = [127, 255, 192, 64, 31, 88, 144, 201]
    offset = 10
    scaled = [x - offset for x in raw_samples]
    return scaled

# Irrelevant auxiliary function - dead code path (distractor)
def analyze_spectral(data):
    fft_buffer = [complex(x, 0) for x in data]
    result = []
    for i in range(len(fft_buffer)):
        angle = math.pi * i / len(fft_buffer)
        rotated = fft_buffer[i] * complex(math.cos(angle), math.sin(angle))
        result.append(abs(rotated))
    return result

# Data transformation with bit manipulation and filtering
def transform_readings(raw_values, mode='adaptive'):
    filtered = []
    shift_key = 2
    mask = 0xFF >> 2

    for val in raw_values:
        if val < 0:
            continue
        shifted = (val << shift_key) & mask
        if shifted % 3 == 0:
            shifted = shifted ^ 0x0A
        filtered.append(shifted)

    # Extra transformation layer (only some values used later)
    extended_features = []
    for x in filtered:
        extended_features.append((x ** 2 + 1) | 5)
        extended_features.append(int(math.sqrt(max(x, 1))) & 7)

    return filtered  # Only filtered is actually used

# Baseline configuration with nested structure
def get_config():
    return {
        'threshold': 45,
        'gain': 1.25,
        'flags': { 'debug': False, 'safe_mode': True },
        'weights': [0.8, 1.0, 1.1, 0.9],
        'limit': 200
    }

# Core processing logic with lambda-based reducers
def process_metrics(data, config):
    threshold = config['threshold']
    gain = config['gain']
    limit = config['limit']

    # Filter valid measurements
    valid = [x for x in data if x > threshold and x < limit]

    # Compute derived metrics (some are red herrings)
    avg_val = sum(valid) / len(valid) if valid else 0
    max_val = max(valid) if valid else 0
    min_val = min(valid) if valid else float('inf')

    # Distractor: unused statistical measures
    variance_proxy = sum((x - avg_val) ** 2 for x in valid) / len(valid) if valid else 0
    entropy_like = -sum((x / sum(valid)) * math.log(x / sum(valid)) for x in valid if x > 0) if valid else 0

    # Use lambda for dynamic aggregation
    aggregators = {
        'sum': lambda v: sum(v),
        'weighted': lambda v: sum(x * gain for x in v)
    }

    raw_sum = aggregators['sum'](valid)
    adjusted_sum = aggregators['weighted'](valid)

    # Set operations to deduplicate and filter (distractor usage)
    unique_caps = set([min(x, 100) for x in valid])
    control_set = {90, 95, 100}
    overlap_count = len(unique_caps & control_set)

    # Final diagnostic calculation (this is the actual answer path)
    diagnostic_score = int((adjusted_sum - raw_sum) * 2.5) + overlap_count

    # Unused intermediate results (misleading)
    complexity_metric = len(valid) * overlap_count + int(variance_proxy)
    stability_index = (max_val - min_val) / (avg_val + 1e-8)

    return diagnostic_score

# Secondary helper with no side effects (distractor)
def generate_report_snapshot(metrics):
    timestamp = "2023-11-05T14:30:00Z"
    tags = {"type": "diagnostic", "version": "2.1"}
    return f"Report-{hash(timestamp) % 1000}-{tags['version'].replace('.', '')}"

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect sensor readings
    sensor_data = collect_readings()
    
    # Step 2: Transform data using bit manipulation
    transformed_data = transform_readings(sensor_data)
    
    # Step 3: Load configuration
    baseline_config = get_config()
    
    # Step 4: Process metrics (key statement)
    final_diagnostic = process_metrics(transformed_data, baseline_config)
    
    # Print result
    print(f"Result: {final_diagnostic}")