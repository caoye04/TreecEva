from itertools import combinations
from typing import Set, Dict, List

def analyze_trends(data: List[float]) -> float:
    # Irrelevant trend analysis (dead-end function)
    changes = [data[i+1] - data[i] for i in range(len(data)-1)]
    avg_change = sum(changes) / len(changes) if changes else 0
    return round(avg_change, 3)

# Simulated system metrics
cpu_load = [0.78, 0.82, 0.75, 0.91, 0.88]
memory_usage = [0.64, 0.71, 0.69, 0.73, 0.77]
disk_io = [120, 135, 110, 145, 130]

# Distractor variables (not used in final calculation)
system_health = sum(cpu_load) / len(cpu_load)
stability_index = analyze_trends(cpu_load)
baseline_threshold = 0.8

# Core evaluation data
metric_set: Set[str] = {'latency', 'throughput', 'error_rate', 'reliability'}
benchmark_data: Dict[str, float] = {
    'latency': 45.2,
    'throughput': 987.3,
    'error_rate': 0.0021,
    'reliability': 0.998,
    'jitter': 3.4  # Irrelevant key
}

# Auxiliary mapping (some entries are red herrings)
weight_map: Dict[str, float] = {
    'latency': 0.3,
    'throughput': 0.25,
    'error_rate': 0.35,
    'reliability': 0.1,
    'bandwidth': 0.15,  # Unused weight
    'security': 0.05   # Unused weight
}

# Helper function to filter relevant metrics
def get_relevant_keys(available: Set[str], required: Set[str]) -> Set[str]:
    return available.intersection(required)

# Secondary scoring for distraction
legacy_metrics = ['response_time', 'availability']
overlap_count = len(set(legacy_metrics).intersection(metric_set))
temp_penalty = overlap_count * 5

# Main evaluation logic
def evaluate_performance(metrics: Set[str], data: Dict[str, float]) -> int:
    relevant_keys = get_relevant_keys(metrics, set(data.keys()))
    
    # Compute base score from actual values
    base_score = 0
    for key in relevant_keys:
        weight = weight_map.get(key, 0)
        value = data[key]
        if key == 'latency':
            base_score += (100 - min(value, 100)) * weight
        elif key == 'throughput':
            base_score += min(value / 10, 100) * weight
        elif key == 'error_rate':
            base_score += (1 - min(value, 1)) * 100 * weight
        elif key == 'reliability':
            base_score += value * 100 * weight
    
    # Apply arbitrary scaling (real computation)
    scaled_score = base_score * 1.1
    
    # Generate distractor combo analysis
    combo_pairs: List[Set[str]] = [set(combo) for combo in combinations(metrics, 2)]
    complex_interactions = len([c for c in combo_pairs if 'reliability' in c and 'throughput' in c])
    
    # Final score adjustment (only scaling matters)
    final_raw = scaled_score - temp_penalty + (complex_interactions * 2)
    
    return int(round(final_raw))

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")