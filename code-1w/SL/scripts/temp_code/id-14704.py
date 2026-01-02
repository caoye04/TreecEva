import itertools

# Simulate sensor data processing with noise filtering and performance scoring
def collect_diagnostics():
    raw_readings = [0.85, 0.92, 0.78, 0.63, 0.95, 0.88, 0.76]
    baseline = 0.8
    adjusted = [r - 0.05 for r in raw_readings if r > baseline]
    return adjusted

def generate_patterns(n):
    # Irrelevant function: generates bit patterns not used in main logic
    return list(itertools.product([0, 1], repeat=n))

def filter_outliers(data, threshold=0.1):
    mean_val = sum(data) / len(data)
    return [x for x in data if abs(x - mean_val) / mean_val < threshold]

def compute_entropy(values):
    # Distractor calculation: computes entropy but unused
    from math import log2
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * log2(p) for p in probs if p > 0)

def shift_phase_signal(signal, steps=1):
    # Dead code path: never invoked in execution
    return signal[steps:] + signal[:steps]

def normalize_weights(ws):
    total = sum(ws)
    return [w / total for w in ws]

def apply_correction(factor):
    # Misleading intermediate: appears important but unused
    temp = 1.0
    for i in range(5):
        temp *= (factor + i) / (i + 1)
    return temp

def validate_integrity(checksum, expected_prefix="sig"):
    # Unused validation routine (red herring)
    return checksum.startswith(expected_prefix)

def evaluate_reliability(indices):
    # Complex but irrelevant transformation
    cumsum = 0
    for i, idx in enumerate(indices):
        cumsum += idx * (0.9 ** i)
    return cumsum * 100

def extract_key_metrics(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    peak = max(readings)
    stability = peak - avg
    # Hidden use: only 'avg' and 'peak' matter; others are distractors
    return {'average': avg, 'variance': variance, 'peak': peak, 'stability': stability}

def evaluate_performance(metrics, weights):
    # Only these fields are actually used
    score_components = [
        metrics['average'] * weights[0],
        metrics['peak'] * weights[2]  # weights[1], [3] ignored
    ]
    bonus = 5 if metrics['average'] > 0.82 else 0
    penalty = 0
    if metrics['stability'] > 0.1:
        penalty += 3
    # Final computation
    base_score = sum(score_components) * 100
    return base_score + bonus - penalty

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect and filter sensor diagnostics
    diagnostics = collect_diagnostics()  # [0.8, 0.87, 0.9] -> after adjustment and filter
    clean_data = filter_outliers(diagnostics, threshold=0.15)
    
    # Step 2: Extract key performance metrics
    metrics = extract_key_metrics(clean_data)
    
    # Step 3: Setup weighting scheme
    weights = [0.6, 0.1, 0.3, 0.0]  # Last weight unused
    normalized_weights = normalize_weights(weights)  # Computed but not used
    
    # Step 4: Evaluate final performance score
    final_score = evaluate_performance(metrics, weights)
    
    # Irrelevant computations to increase interference
    entropy = compute_entropy([1, 2, 3])
    patterns = generate_patterns(4)
    reliability = evaluate_reliability([1, 2, 3, 4])
    correction_factor = apply_correction(1.5)
    
    # Output target result
    print(f"Result: {final_score}")