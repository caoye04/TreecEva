import itertools

# Simulated sensor array diagnostics with noise filtering and weighted analysis
def analyze_sensor_group(readings):
    baseline = sum(readings) / len(readings)
    filtered = [r for r in readings if abs(r - baseline) < 15]
    variance = sum((x - baseline) ** 2 for x in filtered) / len(filtered) if filtered else 0
    return {'baseline': baseline, 'variance': variance, 'stability': variance < 25}

# Irrelevant helper - dead code path (decoy)
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log(count / total) for count in freq.values())
    return entropy

# Data transformation pipeline with red herrings
def transform_sequence(raw_data):
    shifted = [(x * 3 + 7) % 101 for x in raw_data]
    paired = list(itertools.combinations(shifted, 2))
    sums = [a + b for a, b in paired if (a + b) % 7 == 0]
    # Below line computes something irrelevant to final result
    avg_sum = sum(sums) / len(sums) if sums else 0
    return shifted  # Only this matters

# Core processing with misleading intermediate steps
def evaluate_system_health(sensor_data):
    processed = []
    temp_records = []
    for i, group in enumerate(sensor_data):
        result = analyze_sensor_group(group)
        processed.append(result)
        # Decoy accumulation (never used later)
        temp_records.append(f"SensorGroup-{i}: {result['baseline']:.2f}")
    
    # Real logic: extract baselines
    baselines = [p['baseline'] for p in processed]
    
    # Fake complexity: generate all permutations (unused)
    _ = list(itertools.permutations(baselines[:4])) if len(baselines) >= 4 else []
    
    # Normalization step (actually used)
    normalized = [round(b / max(baselines) * 100, 2) for b in baselines]
    return normalized

# Final aggregation with critical computation obscured among distractions
def aggregate_metrics(metrics, weight_map):
    # Misleading initialization block
    initial_score = sum(metrics) * 0.87
    adjustment_factor = 1.0
    
    # Generate fake report strings (distractor)
    reports = [f"[REPORT] Node-{i}: {val}" for i, val in enumerate(metrics)]
    
    # Real weighted sum
    weighted_sum = sum(metrics[i] * weight_map.get(f'node_{i}', 1.0) for i in range(len(metrics)))
    
    # Use of itertools.chain to obscure flow (some distraction)
    flat_chain = list(itertools.chain([weighted_sum], [initial_score]))
    
    # Additional decoy logic
    if any(x > 90 for x in metrics):
        adjustment_factor *= 0.95
    if len(metrics) > 5:
        adjustment_factor *= 1.05  # Never reached here
    
    # Critical result calculation
    final_value = weighted_sum * adjustment_factor
    
    # Dead branch based on impossible condition (red herring)
    impossible_state = False
    if impossible_state and final_value < 0:
        final_value -= 1000  # Unreachable
    
    return round(final_value, 4)

# --- Main execution with layered interference ---
if __name__ == "__main__":
    # Raw input data (simulated sensor clusters)
    raw_input_stream = [12, 45, 67, 23, 89, 34, 56]
    
    # Apply transformation (only transformed values matter)
    cleaned_nodes = transform_sequence(raw_input_stream)
    
    # Split into groups for analysis (7 groups of 3, overlapping)
    sensor_arrays = [
        cleaned_nodes[i:i+3] for i in range(0, len(cleaned_nodes), 3)
    ]
    
    # Evaluate health across sensor network
    health_metrics = evaluate_system_health(sensor_arrays)
    
    # Weight configuration (critical for final answer)
    node_weights = {
        'node_0': 0.9,
        'node_1': 1.2,
        'node_2': 1.5,
        'node_3': 0.8,
        'node_4': 1.0  # Others default to 1.0
    }
    
    # Decoy: unused alternative weighting
    alt_weights = {f'node_{i}': 1.1 for i in range(10)}
    
    # Key statement
    final_diagnostic = aggregate_metrics(health_metrics, node_weights)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")