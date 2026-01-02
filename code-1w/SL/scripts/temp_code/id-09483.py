def analyze_pattern(sequence):
    if not sequence:
        return 0
    total_peaks = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            total_peaks += 1
    return total_peaks

# Irrelevant helper function (decoy)
def smooth_data(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return smoothed

# Unused transformation (dead code path)
def transform_to_frequency_domain(samples):
    import math
    N = len(samples)
    freqs = [0] * N
    for k in range(N):
        real = 0
        for n in range(N):
            real += samples[n] * math.cos(2 * math.pi * k * n / N)
        freqs[k] = real / N
    return freqs

def compute_entropy(values):
    from collections import Counter
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * (p).bit_length()  # Simplified pseudo-entropy
    return int(entropy)

def calculate_final_score(data_set, weights):
    # Core logic begins
    baseline = sum(data_set) / len(data_set) if data_set else 0
    deviations = [abs(x - baseline) for x in data_set]
    
    # Determine outlier threshold (Q3 + 1.5 * IQR)
    sorted_devs = sorted(deviations)
    q1_idx = len(sorted_devs) // 4
    q3_idx = 3 * len(sorted_devs) // 4
    q1 = sorted_devs[q1_idx]
    q3 = sorted_devs[q3_idx]
    iqr = q3 - q1
    outlier_threshold = q3 + 1.5 * iqr
    
    outliers = {i for i, dev in enumerate(deviations) if dev > outlier_threshold}
    
    # Compute trend score using sign changes
    trend_changes = 0
    for i in range(1, len(data_set)):
        if (data_set[i] - data_set[i-1]) * (data_set[i-1] - (data_set[i-2] if i >= 2 else data_set[i-1])) < 0:
            trend_changes += 1
    
    # Use set operations to identify stable regions
    stable_indices = set(range(len(data_set))) - outliers
    clusters = []
    current_cluster = []
    for idx in sorted(stable_indices):
        if not current_cluster or idx == current_cluster[-1] + 1:
            current_cluster.append(idx)
        else:
            if len(current_cluster) >= 2:
                clusters.append(current_cluster)
            current_cluster = [idx]
    if current_cluster and len(current_cluster) >= 2:
        clusters.append(current_cluster)
    
    cluster_bonus = sum(len(c) for c in clusters)
    
    # Apply weights via conditional expression
    adjustment_factor = weights['peak_weight'] if len(clusters) > 2 else weights['default_penalty']
    
    # Auxiliary distraction: unused structure
    stats_summary = {
        'mean': baseline,
        'median': sorted(data_set)[len(data_set)//2],
        'peak_count': analyze_pattern(data_set),
        'entropy_metric': compute_entropy([int(x) for x in data_set]),
        'outlier_ratio': len(outliers) / len(data_set)
    }
    
    # Final computation chain
    raw_score = sum(data_set[i] for i in stable_indices)
    penalty = len(outliers) * 3.7
    bonus = cluster_bonus * adjustment_factor
    trend_score = trend_changes * 2.1
    
    # Critical execution point
    final_score = (raw_score - penalty + bonus + trend_score) * 0.95
    
    # Red herring: irrelevant print
    # print(f'Debug: {stats_summary}')
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data with embedded patterns
    data_set = [12, 15, 14, 16, 100, 18, 17, 19, 20, 21, 9, 8, 22, 23, 24]
    
    # Weight configuration (some keys unused)
    weights = {
        'peak_weight': 4.3,
        'default_penalty': 1.2,
        'legacy_mode': 0.5,
        'spike_multiplier': 2.0  # unused
    }
    
    # Distractor variables
    temp_result = smooth_data(data_set)
    freq_analysis = transform_to_frequency_domain(data_set[:8])
    shadow_copy = data_set[::-1]
    
    # Key statement
    final_score = calculate_final_score(data_set, weights)
    
    # Output result
    print(f"Result: {final_score}")