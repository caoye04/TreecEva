import math

def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return [x for x in data if x > threshold]

def compute_entropy(values):
    """Another decoy function not directly related to final result."""
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def validate_readings(readings):
    """Dead-end validation function with misleading output."""
    valid_count = 0
    for r in readings:
        if 0 <= r <= 1:
            valid_count += 1
    return valid_count == len(readings)

def filter_outliers(seq, factor=1.5):
    """Unused preprocessing step — red herring."""
    q1 = sorted(seq)[len(seq)//4]
    q3 = sorted(seq)[3*len(seq)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in seq if lower <= x <= upper]

def transform_metric(x, mode='linear'):
    if mode == 'log':
        return math.log(1 + x)
    elif mode == 'square':
        return x * x
    else:
        return x * 0.9  # default path used indirectly

def evaluate_performance(metrics, weights):
    # Core logic begins here — but buried among distractions
    adjusted = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            adjusted.append(transform_metric(val, 'square'))
        else:
            adjusted.append(transform_metric(val))  # uses default case
    
    # Real computation: weighted harmonic mean approximation
    weighted_inv_sum = 0.0
    weight_total = 0.0
    temp_results = []
    
    for j in range(len(adjusted)):
        safe_val = max(adjusted[j], 1e-6)  # avoid division by zero
        contribution = weights[j] / safe_val
        weighted_inv_sum += contribution
        weight_total += weights[j]
        temp_results.append(contribution)  # irrelevant storage
    
    # Distractor block: sorting and unused stats
    temp_results.sort(reverse=True)
    avg_contribution = sum(temp_results) / len(temp_results) if temp_results else 0
    peak = temp_results[0] if temp_results else 0
    
    # Actual answer derivation — obscured by noise
    harmonic_base = weight_total / weighted_inv_sum if weighted_inv_sum != 0 else 0
    
    # Additional misdirection: conditional expression that looks important but isn't decisive
    offset = 10 if all(m > 0.5 for m in metrics) else -5
    bonus = 5 if len([w for w in weights if w > 0.8]) >= 2 else 0
    
    # Final adjustment using irrelevant intermediate variables (only harmonic_base matters)
    final_value = harmonic_base + (offset if offset > 0 else 0) - (bonus // 2)  # only harmonic_base is key
    
    # This variable is what we actually care about
    final_score = int(round(final_value * 1.75))  # scaling then cast
    
    # Dead code branch — never executed due to fixed input
    if any(m < 0 for m in metrics):
        fallback = sum(metrics) * 2
        final_score = fallback  # unreachable
    
    return final_score

# Main execution context
if __name__ == '__main__':
    # Irrelevant setup data
    sensor_data = [0.82, 0.91, 0.77, 0.88, 0.65]
    thresholds = [0.7, 0.85, 0.72, 0.8, 0.6]
    entropy_source = [4, 5, 3, 6, 2]
    
    # Unused transformation chain
    filtered = filter_outliers(sensor_data, factor=2.0)
    normalized = [x * 1.1 for x in filtered if x in sensor_data]
    
    # Key inputs — hidden in middle of noise
    metrics = [0.8, 0.9, 0.7, 0.6, 0.85]  # performance indicators
    weights = [0.3, 0.25, 0.2, 0.15, 0.1]   # importance coefficients
    
    # Trigger the actual logic
    final_score = evaluate_performance(metrics, weights)
    
    # Print required output
    print(f"Result: {final_score}")