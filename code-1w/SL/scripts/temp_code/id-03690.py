import math

# System telemetry simulation for distributed node analysis
def generate_telemetry(nodes):
    data = {}
    for i in range(nodes):
        base_load = (i * 17) % 13
        fluctuation = abs(math.sin(i + 0.5)) * 10
        data[f'node_{i}'] = {
            'load': round(base_load + fluctuation, 3),
            'temp': 40 + ((i * 97) % 19),
            'uptime': (i + 1) * 1000,
            'errors': (i * 5) % 7
        }
    return data

# Irrelevant diagnostic function (decoy)
def analyze_stability(telemetry):
    total_variance = 0.0
    for node, metrics in telemetry.items():
        if 'load' in metrics:
            total_variance += metrics['load'] ** 0.5
    return round(total_variance / len(telemetry), 4)

# Auxiliary transformation (partially relevant but misleading)
def normalize_loads(telemetry):
    loads = [v['load'] for k, v in telemetry.items()]
    mean_load = sum(loads) / len(loads)
    normalized = [(load - mean_load) * 1.5 for load in loads]  # arbitrary scaling
    return normalized

# Core processing logic
def filter_high_risk_nodes(telemetry, threshold_temp=55, max_error_rate=5):
    risky = []
    for node_id, attrs in telemetry.items():
        temp_flag = attrs['temp'] > threshold_temp
        error_flag = attrs['errors'] >= max_error_rate
        load_index = int(attrs['load'] // 1) % 10
        # Bit manipulation red herring
        encoded_risk = (load_index << 2) ^ 7 | int(temp_flag)
        if temp_flag or error_flag:
            risky.append({
                'id': node_id,
                'risk_code': encoded_risk,
                'priority': 1 if error_flag else 2
            })
    return risky

# Decoy aggregation (unused path)
def aggregate_diagnostics(telemetry):
    uptime_total = sum(v['uptime'] for v in telemetry.values())
    avg_temp = sum(v['temp'] for v in telemetry.values()) / len(telemetry)
    error_sum = sum(v['errors'] for v in telemetry.values())
    return {
        'total_uptime': uptime_total,
        'mean_temp': round(avg_temp, 2),
        'total_errors': error_sum
    }

# Real key computation chain
def compute_efficiency_score(telemetry):
    scores = []
    for metrics in telemetry.values():
        raw_score = (metrics['load'] * 0.6) + (metrics['temp'] * 0.1)
        adjusted = raw_score / (1 + metrics['errors'])
        scores.append(adjusted)
    efficiency = sum(scores) / len(scores)
    return round(efficiency, 4)

# Conditional preprocessing with slicing distraction
def extract_critical_windows(log_series, window_size=3):
    if len(log_series) < window_size * 2:
        return log_series
    # Slicing operation (irrelevant to final result)
    first_chunk = log_series[:window_size]
    last_chunk = log_series[-window_size:]
    combined = first_chunk + last_chunk
    return sorted(combined, reverse=True)

# Main metric processor combining multiple concepts
def process_metrics(raw_logs, thresholds):
    # Step 1: Extract node identifiers
    node_ids = list(raw_logs.keys())
    n_nodes = len(node_ids)
    
    # Step 2: Compute baseline efficiency
    base_efficiency = compute_efficiency_score(raw_logs)
    
    # Step 3: Apply threshold filtering using dictionary lookup
    filtered_count = 0
    for node_id in node_ids:
        node = raw_logs[node_id]
        if node['load'] > thresholds['load'] or node['temp'] > thresholds['temp']:
            filtered_count += 1
    
    # Step 4: Generate risk-adjusted weight
    adjustment_factor = 1.0
    if filtered_count > n_nodes * 0.4:
        adjustment_factor = 0.85
    elif filtered_count == 0:
        adjustment_factor = 1.1
    
    # Step 5: Use set operations to identify anomaly patterns (distractor)
    all_error_states = {raw_logs[n]['errors'] for n in node_ids}
    common_failures = all_error_states & {0, 1, 2}  # intersection with expected
    unexpected_issues = all_error_states - {0, 1, 2, 3, 4}
    severity_penalty = len(unexpected_issues) * 0.05
    
    # Step 6: Conditional expression based on uptime distribution
    uptimes = [raw_logs[n]['uptime'] for n in node_ids]
    median_uptime = sorted(uptimes)[len(uptimes)//2]
    age_bonus = 0.02 if median_uptime > 2500 else -0.01
    
    # Step 7: Final composition using weighted components
    primary_metric = base_efficiency * adjustment_factor
    secondary_correction = (severity_penalty + age_bonus) * 100
    
    # Step 8: Final diagnostic score
    final_diagnostic = round(primary_metric - secondary_correction, 4)
    
    # Irrelevant print statements (simulating debugging noise)
    # print(f'Debug: Adjustment factor = {adjustment_factor}')
    # print(f'Debug: Severity penalty impact = {severity_penalty}')
    
    return final_diagnostic

# Simulate system data
telemetry_data = generate_telemetry(nodes=12)

# Define threshold policy
system_thresholds = {
    'load': 8.5,
    'temp': 55
}

# Execute main processing pipeline
interim_analysis = normalize_loads(telemetry_data)
analyze_stability(telemetry_data)  # dead call - no assignment
aggregate_diagnostics(telemetry_data)  # dead call

# Critical execution point
final_diagnostic = process_metrics(telemetry_data, system_thresholds)

# Output result
print(f"Target result: {final_diagnostic}")