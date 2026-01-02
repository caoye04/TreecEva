from itertools import combinations

# System health monitoring simulation with multi-metric evaluation
def generate_metrics(base_load, fluctuation_factor):
    raw_metrics = []
    for i in range(5):
        load = base_load + (i * fluctuation_factor)
        temp = 40 + (load * 0.5) + (i % 3)
        latency = 10 + (load ** 0.8)
        cpu_cycles = int(1e6 * (load / 10))
        power_draw = (temp * 2.1) + (latency * 0.75)
        raw_metrics.append({
            'node': i,
            'load': round(load, 2),
            'temperature': round(temp, 2),
            'latency_ms': round(latency, 2),
            'cycles': cpu_cycles,
            'power_watts': round(power_draw, 2)
        })
    return raw_metrics

# Irrelevant helper: calculates theoretical bandwidth (not used in final logic)
def estimate_bandwidth(n_nodes, freq_ghz=2.5):
    total_links = n_nodes * (n_nodes - 1) // 2
    bw_per_link = freq_ghz * 8  # GB/s
    return total_links * bw_per_link

# Core evaluation logic
def analyze_stability(metrics):
    deviations = []n    reference_load = metrics[0]['load']
    for m in metrics:
        diff = abs(m['temperature'] - (40 + reference_load * 0.5))
        deviations.append(diff)
    avg_deviation = sum(deviations) / len(deviations)
    return avg_deviation < 5.0

# Secondary filter based on latency trends
def check_latency_surge(metrics):
    surges = 0
    for i in range(1, len(metrics)):
        if metrics[i]['latency_ms'] > 1.5 * metrics[i-1]['latency_ms']:
            surges += 1
    return surges <= 1

# Main scoring function
def compute_efficiency_score(metrics):
    total_efficiency = 0
    for m in metrics:
        efficiency = m['load'] / (m['power_watts'] * m['latency_ms'])
        total_efficiency += efficiency
    return round(total_efficiency * 100, 2)

# Decision engine using multiple criteria
def evaluate_performance(data, config_thresholds):
    # Step 1: Filter valid nodes based on temperature threshold
    temp_filtered = [d for d in data if d['temperature'] <= config_thresholds['max_temp']]
    
    # Step 2: Stability analysis
    stable_system = analyze_stability(data)
    
    # Step 3: Latency behavior check
    clean_latency = check_latency_surge(data)
    
    # Step 4: Efficiency baseline
    base_score = compute_efficiency_score(temp_filtered)
    
    # Step 5: Apply bonuses/penalties
    penalty = 0
    if not stable_system:
        penalty += 15
    if not clean_latency:
        penalty += 10
    
    # Misleading intermediate calculation (dead-end)
    phantom_risk = 0
    for combo in combinations(data, 2):
        delta = abs(combo[0]['load'] - combo[1]['load'])
        if delta > 8.0:
            phantom_risk += 1  # Not actually used
    # Additional red herring
    calibration_offset = sum([int(str(d['node']) + '1') for d in data]) % 7
    
    final_raw = base_score - penalty
    
    # Final clamping to valid range
    final_score = max(10, min(100, int(final_raw)))
    return final_score

# Simulation parameters
base_workload = 12.0
noise = 3.5
thresholds = {
    'max_temp': 75.0,
    'min_load': 5.0
}

# Generate system telemetry
metric_data = generate_metrics(base_workload, noise)

# Extraneous computation: network resilience score (unused)
node_count = len(metric_data)
network_resilience = estimate_bandwidth(node_count, freq_ghz=3.0)
resilience_grade = chr(ord('A') + min(5, int(network_resilience // 20)))

# Critical execution point
final_score = evaluate_performance(metric_data, thresholds)
print(f"Result: {final_score}")