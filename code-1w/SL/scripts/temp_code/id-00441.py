from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation for environmental monitoring system
def collect_sensor_data(nodes):
    readings = defaultdict(list)
    for node_id, data in nodes.items():
        if data['status'] == 'active':
            readings[data['zone']].append(data['reading'])
    return readings

def filter_anomalies(readings, threshold=2.5):
    filtered = {}
    for zone, vals in readings.items():
        mean_val = sum(vals) / len(vals)
        std_val = (sum((x - mean_val) ** 2 for x in vals) / len(vals)) ** 0.5
        filtered[zone] = [v for v in vals if abs(v - mean_val) / std_val <= threshold]
    return filtered

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def derive_impact_factor(zone_data):
    # Irrelevant complexity: computes a derived metric not used in final result
    impact = {}
    for zone, data in zone_data.items():
        sorted_vals = sorted(set(data))
        if len(sorted_vals) > 1:
            impact[zone] = (sorted_vals[-1] - sorted_vals[0]) / sorted_vals[0]
        else:
            impact[zone] = 0.0
    return impact

def assess_stability(entropies):
    # Dead function: never called in execution path
    stability = {}
    for zone, entropy in entropies.items():
        stability[zone] = 1 / (1 + entropy)
    return stability

def calculate_baseline_adjustment(raw_outcomes):
    # Decoy computation: looks important but unused
    base_shift = sum(raw_outcomes) / len(raw_outcomes)
    adjusted = [x - base_shift for x in raw_outcomes]
    return sum(abs(a) for a in adjusted)

def evaluate_performance(weights, outcomes):
    weighted_sum = 0.0
    for i, outcome in enumerate(outcomes):
        if i % 2 == 0:
            weighted_sum += outcome * weights.get(f'metric_{i}', 1.0)
        else:
            weighted_sum += outcome * weights.get(f'metric_{i}', 0.5)
    penalty = 0
    for val in outcomes:
        if val < 0:
            penalty += 1
    return int(weighted_sum - penalty * 2)

# Main execution flow
if __name__ == '__main__':
    # Simulated input data from distributed sensors
    network_nodes = {
        'N001': {'status': 'active', 'zone': 'A', 'reading': 12.4},
        'N002': {'status': 'inactive', 'zone': 'A', 'reading': 15.1},
        'N003': {'status': 'active', 'zone': 'B', 'reading': 8.7},
        'N004': {'status': 'active', 'zone': 'B', 'reading': 9.2},
        'N005': {'status': 'active', 'zone': 'C', 'reading': 25.3},
        'N006': {'status': 'active', 'zone': 'A', 'reading': 11.9},
        'N007': {'status': 'active', 'zone': 'C', 'reading': 24.8},
        'N008': {'status': 'active', 'zone': 'B', 'reading': 8.9}
    }

    # Step 1: Collect active node readings by zone
    raw_readings = collect_sensor_data(network_nodes)
    
    # Step 2: Filter out statistical outliers
    cleaned_readings = filter_anomalies(raw_readings)
    
    # Step 3: Compute information-theoretic entropy per zone (red herring)
    zone_entropies = {}
    for zone, data in cleaned_readings.items():
        rounded_data = [round(x) for x in data]
        zone_entropies[zone] = compute_entropy(rounded_data)
    
    # Step 4: Derive impact factor (computationally intensive but irrelevant)
    impact_by_zone = derive_impact_factor(cleaned_readings)
    
    # Step 5: Simulate diagnostic scan (dead code path trigger)
    diagnostics_enabled = False
    if diagnostics_enabled:
        stability_metrics = assess_stability(zone_entropies)  # Never executed
    
    # Step 6: Prepare metrics for final evaluation
    metric_weights = {
        'metric_0': 1.8,
        'metric_1': 0.5,
        'metric_2': 2.1,
        'metric_3': 0.9,
        'metric_4': 1.2
    }
    
    # Step 7: Generate raw outcomes based on cleaned data statistics
    raw_outcomes = []
    for zone in ['A', 'B', 'C']:
        if zone in cleaned_readings:
            values = cleaned_readings[zone]
            raw_outcomes.append(int(sum(values) / len(values)))  # Mean rounded down
    
    # Step 8: Introduce deliberate decoy transformation
    baseline_penalty = calculate_baseline_adjustment(raw_outcomes)  # Computed but unused
    
    # Step 9: Core evaluation logic (answer depends only on this)
    final_score = evaluate_performance(metric_weights, raw_outcomes)
    
    # Output result
    print(f"Result: {final_score}")