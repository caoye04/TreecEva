from collections import defaultdict, Counter
import math

# Simulated sensor data processing with noise filtering and pattern analysis
def acquire_signal():
    raw_samples = [i * 0.5 + (i % 7) for i in range(60)]
    return [x for x in raw_samples if x % 2.5 != 1.0]

# Irrelevant transformation: signal smoothing (not used in final path)
def smooth_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        neighbors = signal[max(0, i-1):min(len(signal), i+2)]
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed

# Red herring function: frequency analysis (never called)
def detect_frequency_peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    return len(peaks) > 5

# Core transformation: maps values based on modulo cycles and logs
def transform_signal(samples):
    result = []
    for val in samples:
        if val % 3.0 < 1.5:
            transformed = math.log(val + 1) * 2
        elif val > 25:
            transformed = val / 4
        else:
            transformed = val ** 0.5
        result.append(round(transformed, 3))
    return result

# Auxiliary diagnostic: counts distribution buckets (used indirectly)
def generate_histogram(data):
    hist = defaultdict(int)
    for x in data:
        bucket = int(x // 2)
        hist[bucket] += 1
    return hist

# Decoy diagnostic using character conversion (misleading path)
def evaluate_signature(data):
    signature = ''.join([chr(int(abs(x)) % 26 + 65) for x in data[:10]])
    upper_count = sum(1 for c in signature if c.isupper())
    lower_bound = math.floor(min(data))
    return lower_bound if upper_count > 5 else 0

# Real logic: pattern classification based on growth rate and density
def has_accelerating_trend(seq):
    if len(seq) < 4:
        return False
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    second_diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
    positive_acc = sum(1 for d in second_diffs if d > 0)
    return positive_acc >= len(second_diffs) * 0.6

# Central analysis combining multiple metrics
def analyze_pattern(processed, threshold):
    count_regime_a = sum(1 for x in processed if x < threshold)
    count_regime_b = sum(1 for x in processed if x >= threshold)
    ratio = count_regime_b / (count_regime_a + 1)

    # Density-based sub-analysis
    dense_cluster = [x for x in processed if threshold - 2 <= x <= threshold + 2]
    cluster_score = len(dense_cluster) * ratio

    # Trend validation
    sorted_vals = sorted(processed)
    trend_valid = has_accelerating_trend(sorted_vals)

    # Final diagnostic calculation
    base_score = cluster_score * 100
    adjustment = 27 if trend_valid else -15
    return int(base_score + adjustment)

# Misleading auxiliary check (dead code path)
def validate_redundancy_checks(data_map):
    total_keys = len(data_map)
    large_buckets = sum(1 for k, v in data_map.items() if v > 5)
    return large_buckets / total_keys > 0.3

# Unused recursive filter (decoy)
def recursively_prune(outliers, limit=3):
    if limit == 0 or len(outliers) < 10:
        return outliers
    mid = len(outliers) // 2
    kept = outliers[:mid]
    return recursively_prune(kept, limit - 1)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Acquire raw signal
    signal_data = acquire_signal()
    
    # Step 2: Apply core transformation
    transformed_data = transform_signal(signal_data)
    
    # Step 3: Generate unused smoothed version (distraction)
    filtered_data = smooth_signal(signal_data)  # Dead end
    
    # Step 4: Compute histogram (used later)
    distribution_map = generate_histogram(transformed_data)
    
    # Step 5: Evaluate false signature (red herring)
    dummy_diagnostic = evaluate_signature(transformed_data)
    
    # Step 6: Set dynamic threshold from log-normalized length
    n = len(transformed_data)
    base_threshold = math.log(n) * 3.5
    
    # Step 7: Analyze pattern with real logic
    final_diagnostic = analyze_pattern(transformed_data, base_threshold)
    
    # Step 8: Print result
    print(f"Target result: {final_diagnostic}")