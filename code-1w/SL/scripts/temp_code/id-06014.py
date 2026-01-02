from collections import defaultdict

# Simulate system health monitoring with performance metrics
def collect_metrics():
    data = [
        'CPU_LOAD: 78', 'MEMORY_USAGE: 45', 'DISK_READ: 102', 'NETWORK_IN: 88',
        'CPU_LOAD: 85', 'MEMORY_USAGE: 50', 'DISK_READ: 95', 'NETWORK_IN: 90',
        'CPU_LOAD: 82', 'MEMORY_USAGE: 48', 'DISK_READ: 98', 'NETWORK_IN: 85'
    ]

    readings = defaultdict(list)
    for entry in data:
        key, val = entry.split(': ')
        readings[key].append(int(val))

    # Compute averages
    avg_cpu = sum(readings['CPU_LOAD']) / len(readings['CPU_LOAD'])
    avg_memory = sum(readings['MEMORY_USAGE']) / len(readings['MEMORY_USAGE'])
    avg_disk = sum(readings['DISK_READ']) / len(readings['DISK_READ'])
    avg_network = sum(readings['NETWORK_IN']) / len(readings['NETWORK_IN'])

    # Misleading secondary analysis (not used in final score)
    peak_load = max(readings['CPU_LOAD'])
    stability_ratio = (min(readings['CPU_LOAD']) / peak_load) * 100
    outlier_count = sum(1 for x in readings['MEMORY_USAGE'] if x > 49)

    return {
        'cpu': avg_cpu,
        'memory': avg_memory,
        'disk_io': avg_disk,
        'network': avg_network,
        'peak': peak_load,  # unused distractor
        'stability': stability_ratio,  # unused
        'outliers': outlier_count   # unused
    }

# Auxiliary function for normalization (used)
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0.5

# Performance evaluation logic
def evaluate_performance(metrics, weights):
    # Normalize metrics to [0,1] range based on expected operational bounds
    norm_cpu = normalize(metrics['cpu'], 50, 100)         # Target: higher is worse
    norm_memory = normalize(metrics['memory'], 30, 70)    # Balanced
    norm_disk = normalize(metrics['disk_io'], 80, 120)    # Higher is better
    norm_network = normalize(metrics['network'], 80, 100) # Tight optimal band

    # Invert where necessary
    inv_cpu = 1 - norm_cpu  # We want lower CPU load
    inv_disk = 1 - norm_disk  # Lower disk I/O preferred

    # Weighted scoring
    score = (
        inv_cpu * weights['cpu'] +
        norm_memory * weights['memory'] +
        inv_disk * weights['disk'] +
        norm_network * weights['network']
    )

    # Distractor computation: hypothetical stress index (never used)
    stress_index = (metrics['cpu'] * 0.6) + (metrics['memory'] * 0.4)
    adjusted_stress = stress_index * (1 - (outlier_count := metrics.get('outliers', 0)) * 0.05)

    # Final transformation
    final_normalized_score = round(score * 100, 2)
    return int(final_normalized_score)

# Main execution
if __name__ == "__main__":
    raw_metrics = collect_metrics()

    # Define weighting schema
    weights = {
        'cpu': 0.3,
        'memory': 0.2,
        'disk': 0.25,
        'network': 0.25
    }

    # Additional irrelevant preprocessing (distractor)
    processed_data = []
    for k, v_list in raw_metrics.items():
        if isinstance(v_list, list):
            processed_data.append(f'{k}_AVG:{sum(v_list)/len(v_list):.1f}')

    # Key statement
    final_score = evaluate_performance(raw_metrics, weights)

    # Print result as required
    print(f"Result: {final_score}")