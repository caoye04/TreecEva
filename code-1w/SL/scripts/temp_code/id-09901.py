def analyze_response_times(responses):
    avg_time = sum(responses) / len(responses)
    threshold = avg_time * 0.8
    fast_responses = [t for t in responses if t < threshold]
    return len(fast_responses)

response_data = [1.2, 0.8, 1.5, 0.6, 0.9, 1.1, 0.7]

# Irrelevant computation - distractor
idle_count = 0
for t in response_data:
    if t > 1.0:
        idle_count += 1

# Semi-relevant transformation
adjusted_times = list(map(lambda x: round(x * 1.1, 2), response_data))

# Another distractor: unused statistical calculation
variance_proxy = sum((x - sum(response_data)/len(response_data))**2 for x in response_data) / len(response_data)

# Core logic begins: feedback quality assessment
base_scores = [95, 87, 92, 88, 90]
weight_vector = [0.2] * 5
weighted_base = sum(a*b for a, b in zip(base_scores, weight_vector))

# Simulate user feedback clustering
feedback_clusters = {
    'cluster_A': {1, 3, 4},
    'cluster_B': {0, 2},
    'cluster_C': {1, 4}
}

duplicate_flags = []
for i in range(len(base_scores)):
    flagged = False
    for cluster in feedback_clusters.values():
        if i in cluster:
            if flagged:
                duplicate_flags.append(i)
            flagged = True

# Use set operations to find unique contributing feedback
feedback_set = feedback_clusters['cluster_A'] & feedback_clusters['cluster_C']  # {1, 4} ∩ {1, 4} → {1,4}
feedback_set = feedback_set | {2}  # Add index 2

# Calibration based on response speed
speed_index = analyze_response_times(response_data)
calibration_factor = speed_index / len(response_data)

# Red herring: complex but unused lambda chain
unused_enhancer = lambda x: (lambda y: y**2 + 0.5)(x * 0.9)
irrelevant_boost = unused_enhancer(3.0)

# Key function combining multiple concepts
def aggregate_performance(indices, factor):
    raw_sum = sum(base_scores[i] for i in indices)
    penalty = 0
    for i in indices:
        if base_scores[i] < 90:
            penalty += 5
    adjusted = raw_sum - penalty
    return int(adjusted * factor)

# Critical statement
final_score = aggregate_performance(feedback_set, calibration_factor)

print(f"Result: {final_score}")