def analyze_system_load(inputs):
    # Irrelevant function: simulates system load but unused
    load = sum([x ** 0.5 for x in inputs if x > 10])
    peak = max(inputs) * 0.3
    return load + peak if load < 100 else 0

# Unused data structures as distractors
temp_log = [0.1, 0.4, 0.8, 1.2, 1.6]
system_flags = {'debug': False, 'safe_mode': True, 'override': False}

# Red herring computation
shadow_weight = 17
for i in range(5):
    shadow_weight *= 2
    shadow_weight -= i

# Core metric components
base_metrics = {
    'latency': 42,
    'throughput': 88,
    'accuracy': 94,
    'stability': 76,
    'resource_usage': 33
}

# Misleading transformation (not used in final calculation)
decoy_metrics = {k: v * 1.1 for k, v in base_metrics.items() if v > 50}

# Benchmark weights — only this matters
benchmark_weights = {
    'latency': 0.15,
    'throughput': 0.30,
    'accuracy': 0.35,
    'stability': 0.10,
    'resource_usage': 0.10
}

# Auxiliary function with early returns and distraction
def validate_metric(value, name):
    if name in ['latency', 'resource_usage']:
        return 100 - value  # invert undesirable metrics
    elif value < 0:
        return 0
    elif value > 100:
        return 99  # cap
    return value

# Another decoy function that looks important
def calculate_risk_profile(metrics):
    risk = 0
    for k, v in metrics.items():
        if v < 50:
            risk += 10
    return risk * 1.5

# Critical function: actual answer path
def evaluate_performance(raw, weights):
    adjusted = {}
    for key in raw:
        # Only latency and resource_usage are inverted
        if key == 'latency' or key == 'resource_usage':
            adjusted[key] = 100 - raw[key]
        else:
            adjusted[key] = raw[key]
    
    # Apply weights
    total = 0.0
    for k in weights:
        total += adjusted[k] * weights[k]
    
    # Final nonlinear boost for high performers
    if total > 80:
        total = total * 1.05
    
    return int(total)  # integer result

# Unused recursive helper (distraction)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

# Simulated data ingestion path
raw_input_stream = [12, 45, 67, 89, 23]
_ = analyze_system_load(raw_input_stream)

# Key execution point
metrics = base_metrics
final_score = evaluate_performance(metrics, benchmark_weights)

# Output required format
print(f"Target result: {final_score}")