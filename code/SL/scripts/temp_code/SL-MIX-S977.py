import math
from itertools import combinations
from statistics import mean, variance

def calculate_marker_diversity(markers):
    # Filter valid markers (ASCII sum between 100-500)
    valid_markers = [m for m in markers if 100 <= sum(ord(c) for c in m) <= 500]
    
    # Calculate pairwise uniqueness using combinatorics
    uniqueness_scores = []
    for pair in combinations(valid_markers, 2):
        score = abs(len(pair[0]) - len(pair[1])) * len(set(pair[0]) & set(pair[1]))
        uniqueness_scores.append(score)
    
    # Statistical normalization
    if len(uniqueness_scores) > 1:
        base_stat = mean(uniqueness_scores) / (1 + math.sqrt(variance(uniqueness_scores)))
    else:
        base_stat = 0
    
    return round(base_stat, 2)

# Patient cohort data
patient_data = {
    'cohort_A': ['ACTG', 'GTCA', 'TTAA', 'CCGG'],
    'cohort_B': ['AATT', 'GGCC', 'ACGT', 'TGCA', 'NNNN'],
    'cohort_C': ['AAAA', 'CCCC', 'TTTT']
}

# Process with context manager for logging
with open('diversity_log.txt', 'w') as log_file:
    cohort_metrics = {}
    for cohort, markers in patient_data.items():
        metric = calculate_marker_diversity(markers)
        cohort_metrics[cohort] = metric
        log_file.write(f"{cohort}: {metric}\n")
    
    # Merge metrics with baseline data
    baseline = {'cohort_D': 2.75, 'cohort_E': 3.20}
    all_metrics = cohort_metrics | baseline
    
    # Compute final diversity index
    sorted_values = sorted(all_metrics.values())
    mid_idx = len(sorted_values) // 2
    diversity_index = sum(sorted_values[:mid_idx+1]) if mid_idx > 0 else sorted_values[0]

print(f"Result: {diversity_index}")