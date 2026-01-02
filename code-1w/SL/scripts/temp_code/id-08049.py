from collections import defaultdict, Counter
import math

# Simulated system performance metrics
def collect_metrics():
    raw_data = [
        ('cpu', 78), ('mem', 85), ('disk', 45), ('net', 30),
        ('cpu', 80), ('mem', 82), ('disk', 50), ('net', 35),
        ('cpu', 75), ('mem', 88), ('disk', 40), ('net', 40)
    ]
    
    # Irrelevant aggregation - red herring
    temp_agg = defaultdict(list)
    for k, v in raw_data:
        temp_agg[k].append(v)
    
    # Distractor transformation
    avg_temp = {k: sum(v)/len(v) for k, v in temp_agg.items()}
    
    # Actual metric processing
    base_metrics = {}
    for key, values in temp_agg.items():
        if key == 'cpu':
            base_metrics['compute'] = sum(values) / len(values)
        elif key == 'mem':
            base_metrics['memory'] = sum(values) / len(values)
        elif key == 'disk':
            base_metrics['storage'] = sum(values) / len(values)
        elif key == 'net':
            base_metrics['bandwidth'] = sum(values) / len(values)
    
    # Dead code path - never used
    def unused_normalization(data):
        max_val = max(data.values())
        return {k: v/max_val for k, v in data.items()}
    
    # Misleading intermediate score
    phantom_score = 0
    for val in base_metrics.values():
        phantom_score += val * 0.1
    
    return base_metrics

# Weight configuration with decoy entries
def load_weights():
    weight_config = {
        'compute': 0.35,
        'memory': 0.30,
        'storage': 0.20,
        'bandwidth': 0.15,
        'security': 0.0,      # Decoy - not in metrics
        'latency': 0.0       # Decoy - not in metrics
    }
    
    # Extra processing to distract
    filtered = {k: v for k, v in weight_config.items() if v > 0}
    total = sum(filtered.values())
    normalized = {k: v/total for k, v in filtered.items()}  # Normalization not actually needed
    
    # Return original filtered weights
    return weight_config

# Evaluation logic with early returns and branching
def evaluate_performance(metrics, weights):
    if not metrics or not weights:
        return -1
    
    # Initialize accumulator
    raw_product_sum = 0.0
    weight_sum = 0.0
    
    # Core calculation with conditional filtering
    for component, score in metrics.items():
        if component in weights and weights[component] > 0:
            if score >= 50:
                # Apply nonlinear boost for acceptable performance
                boosted_score = score * (1 + 0.1 * math.exp(-score / 100))
            else:
                # Severe penalty for poor performance
                boosted_score = score * 0.5
            
            contribution = boosted_score * weights[component]
            raw_product_sum += contribution
            weight_sum += weights[component]
        
        # Early break condition that won't trigger here - red herring
        if component == 'security' and score < 60:
            break
    
    # Final weighted score
    if weight_sum == 0:
        return 0
    
    preliminary = raw_product_sum / weight_sum
    
    # Secondary adjustment based on storage threshold
    if metrics.get('storage', 0) < 45:
        preliminary *= 0.9  # Penalty
    
    # Tertiary adjustment - bonus if compute and memory both high
    if metrics.get('compute', 0) > 75 and metrics.get('memory', 0) > 80:
        preliminary *= 1.05
    
    # Round to avoid floating point artifacts
    return round(preliminary, 6)

# Auxiliary function that looks important but isn't used
def generate_diagnostic_report(data):
    counter = Counter()
    for k, v in data.items():
        if v > 80:
            counter['high'] += 1
        elif v > 60:
            counter['medium'] += 1
        else:
            counter['low'] += 1
    return dict(counter)

# Main execution flow
if __name__ == '__main__':
    # Collect performance metrics
    collected_metrics = collect_metrics()
    
    # Load weighting schema
    weights = load_weights()
    
    # Compute phantom statistics - irrelevant
    flat_values = []
    for v in collected_metrics.values():
        flat_values.extend([v] * 2)  # Artificial duplication
    variance = sum((x - sum(flat_values)/len(flat_values))**2 for x in flat_values) / len(flat_values)
    std_dev = math.sqrt(variance)
    
    # Evaluate final performance score
    final_score = evaluate_performance(collected_metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")