import math

# Simulated system performance metrics
def collect_metrics():
    raw_data = {
        'response_time': 120,
        'throughput': 850,
        'error_rate': 0.03,
        'concurrent_users': 470,
        'cpu_util': 78.5,
        'memory_util': 65.2
    }

    # Irrelevant transformation (distractor)
    processed = {k: v * 1.05 for k, v in raw_data.items()}
    normalized = {}

    # Real normalization
    normalized['latency_score'] = 100 - (raw_data['response_time'] / 2)
    normalized['throughput_score'] = raw_data['throughput'] / 10
    normalized['reliability_score'] = (1 - raw_data['error_rate']) * 100
    normalized['load_capacity'] = min(raw_data['concurrent_users'] / 5, 100)
    normalized['resource_efficiency'] = 100 - ((raw_data['cpu_util'] + raw_data['memory_util']) / 2)

    # Dead code path (never executed)
    if False:
        dummy = sum(processed.values())
        normalized['ghost_metric'] = dummy * 0.1

    return normalized

def apply_corrections(data):
    # Misleading correction factors
    corrections = {
        'latency_score': 1.1,
        'throughput_score': 0.95,
        'reliability_score': 1.05,
        'load_capacity': 1.0,
        'resource_efficiency': 0.98
    }

    # Apply real adjustments
    adjusted = {}
    for key in data:
        if key in corrections:
            adjusted[key] = data[key] * corrections[key]
        else:
            adjusted[key] = data[key]

    # Decoy operation with no effect
    temp_set = set(adjusted.keys())
    shadow_copy = temp_set.copy()
    shadow_copy.add('placeholder')

    # Additional irrelevant logic
    if len(shadow_copy) > 5:
        pass  # meaningless check

    return adjusted

def calculate_derived_scores(adj):
    derived = adj.copy()

    # Composite metric with bit manipulation red herring
    throughput_val = int(adj['throughput_score'])
    reliability_val = int(adj['reliability_score'])

    # Distractor bitwise operation (not used in final result)
    masked_score = (throughput_val << 2) ^ (reliability_val >> 1) & 0xFF

    # Actual derived score using modular arithmetic
    derived['composite_stability'] = (
        (adj['reliability_score'] * 0.6) + 
        (adj['resource_efficiency'] * 0.4)
    )

    # Fake dependency
    if 'ghost_metric' in derived:
        derived['composite_stability'] *= 1.1

    return derived

def evaluate_weights(scores):
    # Weight configuration (some irrelevant)
    weights_dict = {
        'latency_score': 0.2,
        'throughput_score': 0.2,
        'reliability_score': 0.25,
        'load_capacity': 0.15,
        'resource_efficiency': 0.1,
        'composite_stability': 0.1  # bonus weight
    }

    # Unused weight variant (red herring)
    alt_weights = {k: v + 0.05 for k, v in weights_dict.items()}

    total_weight = sum(weights_dict.values())
    weighted_sum = 0.0

    for metric, value in scores.items():
        if metric in weights_dict:
            weighted_sum += value * weights_dict[metric]

    # Final scaling with integer division distraction
    scaled_result = int(weighted_sum // 0.1) / 10.0  # effectively rounds to 1 decimal

    # Dead computation
    checksum = 0
    for val in weights_dict.values():
        checksum = (checksum + int(val * 100)) % 97

    return scaled_result

def main():
    # Step 1: Collect base metrics
    metrics = collect_metrics()
    
    # Step 2: Apply corrections
    adjusted_metrics = apply_corrections(metrics)
    
    # Step 3: Calculate derived scores
    full_metrics = calculate_derived_scores(adjusted_metrics)
    
    # Step 4: Define weights (coincides with function expectations)
    weights = {
        'latency_score': 0.2,
        'throughput_score': 0.2,
        'reliability_score': 0.25,
        'load_capacity': 0.15,
        'resource_efficiency': 0.1,
        'composite_stability': 0.1
    }
    
    # Step 5: Evaluate final performance score
    final_score = evaluate_weights(full_metrics)
    
    # Print result as required
    print(f"Result: {final_score}")
    
    # Irrelevant final operations
    summary_set = set(full_metrics.keys())
    summary_set.discard('ghost_metric')  # does nothing
    extra_calc = sum([len(str(k)) for k in summary_set]) * 0.01
    
    return final_score

if __name__ == "__main__":
    main()