def analyze_pattern(sequence, threshold=0.65):
    if not sequence:
        return False
    avg = sum(sequence) / len(sequence)
    above_threshold = [x for x in sequence if x > threshold]
    return len(above_threshold) / len(sequence) > 0.7

# Irrelevant sensor simulation (distractor)
def simulate_sensor_noise(length):
    import random
    return [random.uniform(0.1, 0.4) for _ in range(length)]

# Unused legacy function (dead code path)
def deprecated_normalization(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Core diagnostic logic
def compute_coherence(signal):
    squared = [x ** 2 for x in signal]
    return sum(squared) / len(squared)

def detect_anomaly_clusters(values, gap_tolerance=3):
    clusters = []
    current_cluster = []
    sorted_vals = sorted(enumerate(values), key=lambda x: x[1], reverse=True)
    
    for idx, val in sorted_vals:
        if not current_cluster:
            current_cluster.append(idx)
        elif abs(idx - current_cluster[-1]) <= gap_tolerance:
            current_cluster.append(idx)
        else:
            if len(current_cluster) >= 2:
                clusters.append(current_cluster)
            current_cluster = [idx]
    
    if current_cluster and len(current_cluster) >= 2:
        clusters.append(current_cluster)
    
    return clusters

# Red herring: complex but unused frequency analysis
def spectral_analysis(data):
    result = 1.0
    for i in range(len(data)):
        if i % 2 == 0:
            result *= (data[i] + 0.1) / (i + 1)
        else:
            result += data[i] ** 0.5
    return round(result, 4)

# Set operations used meaningfully
def compute_overlap(regions_a, regions_b):
    set_a = set(regions_a)
    set_b = set(regions_b)
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union) if union else 0

# Main processing chain
def process_metrics(signature, baseline):
    # Step 1: Validate input structure
    if len(signature) != len(baseline):
        raise ValueError("Mismatched dimensions")
    
    # Step 2: Compute coherence ratios
    sig_coherence = compute_coherence(signature)
    base_coherence = compute_coherence(baseline)
    coherence_ratio = sig_coherence / base_coherence if base_coherence != 0 else 0
    
    # Step 3: Detect anomaly clusters in deviation
    deviations = [abs(a - b) for a, b in zip(signature, baseline)]
    clusters = detect_anomaly_clusters(deviations)
    cluster_count = len(clusters)
    
    # Step 4: Use set operations on cluster positions
    flat_clusters = [idx for cluster in clusters for idx in cluster]
    reference_zones = list(range(5, 15)) + list(range(25, 30))
    overlap_score = compute_overlap(flat_clusters, reference_zones)
    
    # Step 5: Apply threshold logic with short-circuiting
    if coherence_ratio < 1.25 and not (cluster_count > 1 or overlap_score > 0.3):
        preliminary = 23
    elif analyze_pattern(deviations):  # Uses distractor logic internally
        preliminary = 46
    else:
        preliminary = 69
    
    # Step 6: Final adjustment using multiple factors
    adjustment_factor = 0
    if cluster_count >= 2:
        adjustment_factor += 17
    if overlap_score > 0.4:
        adjustment_factor += 29
    if sig_coherence > 0.8:
        adjustment_factor -= 11
    
    final_score = preliminary + adjustment_factor
    
    # Irrelevant transformation chain (distractor)
    temp_data = [x * 2 + 1 for x in baseline[:10]]
    temp_data = [t for t in temp_data if t > 1.5]
    normalized = [round((t - min(temp_data)) / (max(temp_data) - min(temp_data)), 3) for t in temp_data]
    
    # Unused intermediate results (misleading)
    entropy_proxy = 0
    for n in normalized:
        if n > 0.5:
            entropy_proxy += n * 0.3
        else:
            entropy_proxy += n * 0.7
    
    # Final diagnostic computed from relevant logic only
    final_diagnostic = final_score * 3 + int(coherence_ratio * 10)
    
    # Execution point of interest
    return final_diagnostic

# Data setup
baseline_readings = [
    0.42, 0.38, 0.41, 0.39, 0.43, 
    0.71, 0.69, 0.73, 0.70, 0.72,
    0.44, 0.40, 0.45, 0.37, 0.46,
    0.81, 0.79, 0.83, 0.80, 0.82,
    0.47, 0.43, 0.48, 0.42, 0.49
]

health_signature = [
    0.88, 0.41, 0.39, 0.85, 0.91,
    1.12, 1.08, 1.15, 1.10, 1.14,
    0.89, 0.84, 0.92, 0.36, 0.90,
    1.25, 1.20, 1.30, 1.22, 1.28,
    0.51, 0.88, 0.53, 0.86, 0.55
]

# Trigger execution
final_diagnostic = process_metrics(health_signature, baseline_readings)
print(f"Target result: {final_diagnostic}")