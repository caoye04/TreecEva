import math

# Simulated network node performance metrics
def get_node_metrics():
    base_load = 78
    peak_load = 92
    response_time_ms = 45
    packet_loss_rate = 0.03
    jitter = 12.5
    uptime_ratio = 0.987

    # Irrelevant derived values (distractors)
    theoretical_capacity = base_load * 3.5
    latency_penalty = max(0, (jitter - 10) * 1.5)
    downtime_hours = (1 - uptime_ratio) * 720

    return {
        'load': (base_load + peak_load) / 2,
        'latency': response_time_ms + latency_penalty,
        'loss': packet_loss_rate,
        'stability': uptime_ratio - 0.02,
        'throughput': 100 - base_load
    }

# Misleading auxiliary function (dead path)
def calculate_bandwidth_throttle(signal_strength, interference):
    if signal_strength < 30:
        return 10
    elif interference > 75:
        return 25
    else:
        return 5

# Secondary metric generator with red herring logic
def get_security_score():
    auth_attempts = 142
    failed_logins = 7
    encryption_strength = 256
    firewall_rules = 48

    # Complex but irrelevant computation
    risk_factor = (failed_logins / auth_attempts) * 100 if auth_attempts > 0 else 0
    compliance_ratio = firewall_rules / 50
    threat_level = max(0, min(10, risk_factor / 5))

    # This score is never used in final calculation
    return 100 - threat_level * 8

# Core weight configuration (critical)
def get_default_weights():
    return [0.3, 0.25, 0.2, 0.15, 0.1]  # Aligned with metrics order

# Data transformation with list comprehension and filtering
def normalize_metrics(raw):
    ordered_keys = ['load', 'latency', 'loss', 'stability', 'throughput']
    raw_values = [raw[k] for k in ordered_keys]
    
    # Normalize to 0-100 scale: invert where lower is better
    normalized = []
    for i, key in enumerate(ordered_keys):
        val = raw_values[i]
        if key in ['load', 'latency', 'loss']:
            # Inverted: lower raw = higher score
            norm = max(0, min(100, 100 - val * (2 if key == 'latency' else 1)))
        else:
            # Direct: higher raw = higher score
            norm = max(0, min(100, val * 100))
        normalized.append(norm)
    
    return normalized

# Decoy function that appears related but isn't used
def adjust_for_hardware_tier(metrics, tier='mid'):
    multiplier = {'low': 0.8, 'mid': 1.0, 'high': 1.15}.get(tier, 1.0)
    return {k: v * multiplier for k, v in metrics.items()}

# Critical aggregation function
def aggregate_performance(metrics, weights):
    normed = normalize_metrics(metrics)
    
    # Apply weights using list comprehension
    weighted_scores = [score * w for score, w in zip(normed, weights)]
    raw_sum = sum(weighted_scores)
    
    # Apply non-linear adjustment (important step)
    adjusted = raw_sum * (1.05 if raw_sum < 85 else 1.0)
    
    # Hidden correction factor based on stability threshold
    stability_index = metrics['stability']
    if stability_index > 0.8:
        adjusted += 3.0  # bonus for high stability
    
    # Final clamping
    return max(0, min(100, round(adjusted, 2)))

# Unused legacy function (distractor)
def legacy_evaluation(nodes):
    total = 0
    for n in range(nodes):
        total += (n + 1) * 1.5
    return total // nodes if nodes > 0 else 0

# Main execution flow
if __name__ == '__main__':
    # Gather primary metrics
    metrics = get_node_metrics()
    
    # Fetch weighting scheme
    weights = get_default_weights()
    
    # Compute final performance score
    final_score = aggregate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")
    
    # Additional irrelevant prints (noise)
    print(f"Debug: Metrics collected")
    print(f"Status: System evaluation complete")