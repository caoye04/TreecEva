import math

# Irrelevant helper function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

# Misleading performance metric that isn't used
def legacy_scorer(data):
    return sum(d * 0.7 for d in data) % 997

# Core system: Evaluate system performance based on weighted metrics
def evaluate_performance(metrics, weights):
    # Step 1: Filter valid metrics (non-zero and positive)
    valid_metrics = {k: v for k, v in metrics.items() if v > 0}
    
    # Step 2: Apply exponential decay to older metrics (simulated with square root)
    decayed = {k: math.sqrt(v) for k, v in valid_metrics.items()}
    
    # Step 3: Normalize weights to sum to 1.0
    total_weight = sum(weights.values())
    normalized_weights = {k: w / total_weight for k, w in weights.items()}
    
    # Step 4: Compute weighted sum of decayed metrics
    weighted_sum = 0.0
    for key in decayed:
        if key in normalized_weights:
            weighted_sum += decayed[key] * normalized_weights[key]
    
    # Step 5: Apply non-linear boost if all metrics exceed threshold
    if all(v > 1.0 for v in valid_metrics.values()):
        weighted_sum *= 1.25
    
    # Step 6: Cap score at 100.0 for stability
    capped_score = min(weighted_sum, 100.0)
    
    # Step 7: Add bonus only if specific keys are present (red herring condition)
    bonus_keys = ['latency', 'throughput', 'accuracy']
    missing_keys = [k for k in bonus_keys if k not in valid_metrics]
    if len(missing_keys) == 0:
        capped_score += 5.0  # Bonus for full metric coverage
    
    # Step 8: Final adjustment using bit manipulation (obscure but deterministic)
    # Simulate low-level tuning: use lower 8 bits of int(capped_score * 100)
    raw_value = int(capped_score * 100)
    adjusted_value = (raw_value & 0xFF)  # Keep only last 8 bits
    final_value = adjusted_value / 100.0  # Convert back to decimal
    
    return final_value

# --- Distractor Variables and Irrelevant Data ---

# Fake dataset for unrelated analysis
historical_logs = [
    {'timestamp': 1623456789, 'event': 'login', 'user_id': 1001},
    {'timestamp': 1623456820, 'event': 'query', 'user_id': 1002}
]

# Unused weight configurations (misleading)
alt_weights_v1 = {'accuracy': 0.6, 'latency': 0.2, 'memory': 0.2}
alt_weights_v2 = {'throughput': 0.5, 'energy': 0.3, 'cost': 0.2}

# Simulated telemetry stream (not used in calculation)
current_telemetry = {
    'cpu_temp': 72.3,
    'disk_usage_pct': 67,
    'network_latency_ms': 45
}

# Decoy metrics with invalid values (filtered out)
invalid_metrics = {
    'accuracy': -0.1,
    'latency': 0.0,
    'throughput': 1200
}

# --- Actual Input Data Used in Computation ---
metrics = {
    'accuracy': 0.95,
    'latency': 150,
    'throughput': 850,
    'memory': 480
}

weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.2,
    'memory': 0.1
}

# --- Execution Point of Interest ---
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")