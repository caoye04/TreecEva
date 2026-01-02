from itertools import combinations

# Simulate system performance metrics under varying load conditions
def collect_metrics(base_load, stress_factor):
    metrics = {}
    temp_data = []
    for i in range(1, 6):
        load = base_load * (1 + stress_factor * i / 10)
        throughput = (100 - abs(load - 50)) ** 1.1
        latency = 1000 / (1 + throughput) + stress_factor * i
        error_rate = max(0.01, (load / 100) ** 3)
        temp_data.append((throughput, latency, error_rate))
    
    # Compute derived statistics
    avg_throughput = sum(t[0] for t in temp_data) / len(temp_data)
    avg_latency = sum(t[1] for t in temp_data) / len(temp_data)
    harmonic_response = len(temp_data) / sum(1/(t[1] + 1) for t in temp_data)
    
    metrics['efficiency'] = avg_throughput / (avg_latency ** 0.5)
    metrics['stability'] = 1 / (sum(t[2] for t in temp_data) / len(temp_data))
    metrics['peak_load'] = max(t[0] for t in temp_data) / 10
    metrics['consistency'] = avg_throughput / max(t[0] for t in temp_data)
    
    # Irrelevant intermediate calculation (distractor)
    comb = list(combinations([1, 2, 3, 4], 2))
    dummy_sum = sum(a * b for a, b in comb)
    metrics['fictitious_index'] = dummy_sum * 0.1  # Not used later
    
    return metrics

def normalize_metric(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

def evaluate_performance(metrics, weights):
    # Normalize key indicators
    norm_eff = normalize_metric(metrics['efficiency'], 5, 50)
    norm_stab = normalize_metric(metrics['stability'], 20, 100)
    norm_peak = normalize_metric(metrics['peak_load'], 3, 9)
    norm_cons = normalize_metric(metrics['consistency'], 0.6, 1.0)
    
    # Weighted scoring
    score_components = [
        norm_eff * weights[0],
        norm_stab * weights[1],
        norm_peak * weights[2],
        norm_cons * weights[3]
    ]
    
    # Apply non-linear bonus for high consistency
    if metrics['consistency'] > 0.85:
        score_components[3] *= 1.2
    
    raw_score = sum(score_components)
    
    # Secondary adjustment based on unused metric (misleading dependency)
    adjustment = 0
    if metrics.get('fictitious_index', 0) > 15:  # This will never trigger meaningfully
        adjustment = -1
    
    # Final scaling
    final_score = int(raw_score * 10 + adjustment)  # Actual result
    
    # Dead code path (red herring)
    if False:
        fallback = 0
        for k in sorted(metrics.keys()):
            fallback += hash(k) % 10
        final_score = fallback
    
    return final_score

# Main execution
base_metrics = collect_metrics(base_load=40, stress_factor=1.2)
weights = [0.3, 0.3, 0.2, 0.2]
final_score = evaluate_performance(base_metrics, weights)
print(f"Result: {final_score}")