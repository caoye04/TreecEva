import math

# Simulated system metrics (some are red herrings)
def get_system_metrics():
    cpu_load = 78.2
    memory_usage = 45.6
    disk_io = 200  # Irrelevant - not used in final calculation
    network_latency = 40
    packet_loss = 0.05
    gpu_temp = 65  # Distractor - unused
    uptime_hours = 127  # Distractor
    context_switches = 15000  # Dead code path
    return {
        'cpu': cpu_load,
        'memory': memory_usage,
        'latency': network_latency,
        'loss': packet_loss,
        'io_ops': disk_io  # Included but irrelevant
    }

# Weight configuration with misleading entries
def get_weights():
    weights = {
        'cpu': 0.3,
        'memory': 0.25,
        'latency': 0.35,
        'loss': 0.1,
        'bandwidth': 0.2  # Not present in data - deliberate red herring
    }
    # Extra computation on weights (distraction)
    adjusted = {k: v * 1.1 for k, v in weights.items() if k != 'bandwidth'}
    normalized = {k: v / sum(adjusted.values()) for k in adjusted}
    return normalized  # Note: 'bandwidth' already excluded

# Auxiliary function - looks important but only partially used
def calculate_health_factor(metrics):
    base = metrics.get('cpu', 0)
    mem_penalty = 0.1 * metrics.get('memory', 0) if metrics.get('memory', 0) > 40 else 0
    latency_risk = math.exp(-metrics.get('latency', 0) / 100)
    # Following lines look complex but are unused
    dummy_calc = (lambda x: x ** 2 + 1)(base) if base < 80 else 0
    return base - mem_penalty + (1 - latency_risk) * 10

# Core evaluation logic with conditional expressions and list comprehensions
def preprocess_values(raw_metrics, raw_weights):
    # Extract valid keys present in both
    valid_keys = ['cpu', 'memory', 'latency', 'loss']
    filtered_metrics = {k: raw_metrics[k] for k in valid_keys if k in raw_metrics}
    
    # Normalize metrics to 0-100 scale inversely for latency and loss
    normalized = []
    for key in valid_keys:
        if key not in filtered_metrics:
            continue
        val = filtered_metrics[key]
        if key == 'latency':
            score = max(0, 100 - (val / 2))  # Inverse: lower latency = higher score
        elif key == 'loss':
            score = max(0, 100 - (val * 1000))  # High penalty for packet loss
        else:
            score = 100 - val  # Assume all others: lower = better
        normalized.append(('raw_' + key, val, 'score_' + key, score))
    
    # List comprehension to extract only relevant scores
    scores = [item for item in normalized if item[0].startswith('raw_')]
    values_dict = {item[2]: item[3] for item in scores}  # Map score_key -> value
    
    # Return dictionary structure that will be used selectively
    return values_dict

# Final scoring with conditional weighting and distractors
def evaluate_performance(metrics, weights):
    processed = preprocess_values(metrics, weights)
    
    # Extract individual scores
    cpu_score = processed.get('score_cpu', 0)
    memory_score = processed.get('score_memory', 0)
    latency_score = processed.get('score_latency', 0)
    loss_score = processed.get('score_loss', 0)
    
    # Compute weighted average using only subset of available data
    total_weight = 0
    weighted_sum = 0
    for metric_name in ['cpu', 'memory', 'latency']:  # Note: 'loss' is intentionally excluded here despite being processed
        weight_key = f'score_{metric_name}'
        if metric_name == 'latency' and latency_score < 50:
            continue  # Conditional exclusion (not triggered here)
        score_val = processed.get(f'score_{metric_name}', 0)
        weight_val = weights.get(metric_name, 0)
        weighted_sum += score_val * weight_val
        total_weight += weight_val
    
    # Fallback mechanism (not needed but looks important)
    final_raw = weighted_sum / total_weight if total_weight > 0 else 50
    
    # Additional adjustment based on health factor (only partially influences)
    health = calculate_health_factor(metrics)
    adjustment = (health - 70) / 10  # Small correction term
    adjusted_score = final_raw + adjustment
    
    # Apply ceiling and floor
    bounded_score = max(0, min(100, adjusted_score))
    
    # Decoy transformation (never used)
    fft_transform = [bounded_score * math.cos(i) for i in range(5)]
    smoothed = sum(fft_transform) / len(fft_transform) if len(fft_transform) > 0 else 0
    
    # Final decision with conditional expression
    final_value = bounded_score if bounded_score >= 60 else (90 if smoothed > 45 else bounded_score)
    
    # Key assignment point
    final_score = round(final_value, 4)
    
    # Unused variables - red herrings
    audit_log = f"Final: {final_score}, Raw: {final_raw}, Health: {health}, Smoothed: {smoothed:.2f}"
    compliance_flag = True if final_score > 75 else False
    recalibration_needed = False
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    metrics = get_system_metrics()
    weights = get_weights()
    final_score = evaluate_performance(metrics, weights)
    print(f"Result: {final_score}")