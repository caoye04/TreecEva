import itertools

# Simulated system performance metrics
def collect_metrics():
    raw_data = [0.45, 0.67, 0.82, 0.51, 0.93, 0.76, 0.64, 0.88]
    filtered = [x for x in raw_data if x > 0.5]
    return filtered

# Legacy function - not used in current logic (dead code path)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    normalized = [(x - mean_val) * 2 for x in data]
    return normalized

# Irrelevant transformation for distraction
def transform_signal(signal):
    shifted = [s * 1.05 for s in signal]
    reversed_sig = shifted[::-1]
    averaged = [(reversed_sig[i] + reversed_sig[i+1]) / 2 
                for i in range(len(reversed_sig)-1)]
    return averaged  # never actually used

# Auxiliary calculation with misleading intermediate result
def compute_entropy(values):
    import math
    entropy = 0.0
    total = sum(values)
    for v in values:
        prob = v / total
        entropy -= prob * math.log(prob) if prob > 0 else 0
    temp_result = int(entropy * 1000)  # looks important but unused
    return entropy

# Core evaluation logic
def evaluate_performance(metrics, base):
    adjusted = [m * 1.1 for m in metrics if m >= base]
    
    # Complex filtering using itertools and slicing
    grouped = list(itertools.groupby(adjusted, key=lambda x: x >= 0.75))
    high_performers = []
    for k, g in grouped:
        if k:
            high_performers.extend(list(g))
    
    # Multiple assignment and distractor variables
    count = len(high_performers)
    total = sum(high_performers)
    avg_perf = total / count if count > 0 else 0
    
    # Distractor: complex but irrelevant bit manipulation
    magic_offset = 0
    for i in range(count):
        magic_offset ^= (i << 2) | 1
    magic_offset = magic_offset & 0xFF  # obfuscation, not used
    
    # Real computation path
    bonus = 0.05 if count >= 4 else 0.02
    final_raw = avg_perf + bonus
    
    # Secondary adjustment based on conditional logic
    if total > 2.5:
        final_raw *= 1.15
    elif total > 1.5:
        final_raw *= 1.05
    else:
        final_raw *= 0.95
    
    # Final threshold clamp
    final_score = max(0.5, min(final_raw, 1.0)) * 100
    
    # Dead code: post-processing that doesn't affect anything
    if final_score > 85:
        level = 'excellent'
    elif final_score > 70:
        level = 'good'
    else:
        level = 'acceptable'
    
    # This print is NOT allowed - replaced with required format below
    return final_score

# Orchestration with red herring calls
if __name__ == '__main__':
    data_stream = collect_metrics()
    entropy_value = compute_entropy(data_stream)  # distractor call
    dummy_signal = transform_signal(data_stream)   # another unused result
    baseline = 0.65
    final_score = evaluate_performance(data_stream, baseline)
    print(f"Result: {final_score}")