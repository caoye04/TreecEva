from collections import defaultdict, Counter
import math

# Simulated sensor data processing for environmental monitoring system
def analyze_readings(readings):
    processed = []
    outlier_count = 0
    cumulative_noise = 0.0

    for i, val in enumerate(readings):
        if abs(val - 50) > 40:  # Arbitrary threshold
            outlier_count += 1
            continue
        noise = (val % 7) * 0.1
        cumulative_noise += noise
        corrected = val - cumulative_noise
        processed.append(max(0, corrected))
    
    # Dead code path - never used in final calculation
    stats = defaultdict(int)
    for p in processed:
        stats['total'] += p
        stats['count'] += 1
    
    return processed

# Irrelevant helper function - looks important but unused
def calculate_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in freqs.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    return entropy

# Data transformation pipeline
def transform_signals(raw_signals):
    transformed = []
    phase_shift = 0
    for idx, (t, s) in enumerate(zip(range(len(raw_signals)), raw_signals)):
        adjusted = s * 0.9 + phase_shift * 0.1
        phase_shift = (phase_shift + 1) % 5
        if idx % 3 == 0:
            adjusted = abs(adjusted - 10)  # Distortion every 3rd element
        transformed.append(adjusted)
    return transformed

# Core evaluation logic
def compute_baseline(ref_data):
    base = 0
    for i, x in enumerate(ref_data):
        if i % 2 == 0:
            base += x * 2
        else:
            base -= x // 3
    return base + 17  # Magic offset

# Weighted scoring with bit manipulation obfuscation
def apply_weights(values, weights):
    result = 0
    for v, w in zip(values, weights):
        # Bitwise red herring
        temp = (v ^ 255) & 127  # Manipulate bits unnecessarily
        temp = (temp + v) >> 1   # More distraction
        result += v * w          # Actual relevant operation
    return result

# Main performance evaluator
def evaluate_performance(metrics, benchmark_weights):
    score = 0
    
    # Apply complex weighting with decoy operations
    weighted_sum = apply_weights(metrics, benchmark_weights)
    
    # Distractor: Unused normalization chain
    normalized = [m / (sum(metrics) + 1e-8) for m in metrics]
    entropy_metric = -sum(n * math.log(n + 1e-8) for n in normalized)
    
    # Real computation path
    base_modifier = len(metrics) << 2  # Left shift as multiplier
    adjustment = 0
    
    for i, m in enumerate(metrics):
        if m > 50:
            adjustment += (m // 10) & 7  # Bitwise AND as red herring
        elif m < 30:
            adjustment -= i % 4
    
    # Final composition
    intermediate = weighted_sum + base_modifier
    penalty = 0
    
    # Conditional penalty based on pattern matching
    for a, b in zip(metrics, metrics[1:]):
        if (a & b) > 20:  # Bitwise AND condition
            penalty += 5
    
    score = intermediate - penalty + adjustment
    
    # Critical execution point
    final_score = int(score)
    return final_score

# === Setup and Execution ===
if __name__ == "__main__":
    # Simulated input data
    raw_sensor_data = [65, 70, 20, 85, 40, 60, 30, 90, 25]
    
    # Process through irrelevant pipeline
    cleaned = analyze_readings(raw_sensor_data)
    signals = transform_signals(cleaned)
    
    # Core metrics for evaluation
    metrics = [
        int(sum(signals)),                    # Aggregated signal strength
        len([x for x in signals if x > 45]),   # High-threshold count
        int(calculate_entropy(signals) * 10),  # Fake dependency (always 0 due to dead call)
        compute_baseline(signals)              # Base computed from transformed signals
    ]
    
    # Benchmark weights (arbitrary)
    benchmark_weights = [1.2, 0.8, 0.5, 1.5]
    
    # Key statement
    final_score = evaluate_performance(metrics, benchmark_weights)
    
    # Output result
    print(f"Result: {final_score}")