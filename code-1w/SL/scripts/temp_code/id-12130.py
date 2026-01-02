def analyze_trend(data, threshold=0.5):
    """Irrelevant function analyzing trend – dead code path."""
    positive_changes = 0
    for i in range(1, len(data)):
        if data[i] - data[i-1] > threshold:
            positive_changes += 1
    return positive_changes > len(data) // 2

def compute_entropy(values):
    """Unused distraction: computes entropy but never called."""
    from math import log
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

def preprocess_signal(signal_data):
    """Distraction: complex preprocessing not used in main logic."""
    filtered = [x for x in signal_data if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]

def evaluate_performance(metrics, weights):
    # Core logic hidden among distractions
    base = 0
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        if i % 2 == 0:
            base += metric * weight * 1.1
        else:
            base += metric * weight * 0.9
    
    # Apply adjustment based on pattern in bit representation
    adjustment = 0
    for val in metrics:
        bits = bin(int(val * 10))[2:]  # Scale and convert to bit string
        ones = bits.count('1')
        zeros = bits.count('0')
        if ones > zeros:
            adjustment += 1
        elif zeros > ones:
            adjustment -= 1
    
    # Secondary modulation using slicing and set logic
    segment = metrics[1:-1]  # middle elements
    unique_vals = set(round(x, 1) for x in segment)
    if len(unique_vals) < len(segment) * 0.6:
        base *= 1.05
    
    # Final interference: red herring with enumerate and zip
    decoy_sum = 0
    for idx, (a, b) in enumerate(zip(segment, segment[1:])):
        decoy_sum += (a - b) * (idx + 1)  # Complicated but unused
    
    final_score = int(base + adjustment * 50)  # Critical assignment
    return final_score

# Irrelevant global variables
system_status = {'active': True, 'mode': 'debug', 'version': 2.1}
config_params = {k: v for k, v in zip(['alpha', 'beta', 'gamma'], [0.1, 0.9, 0.5])}

# Unused data structures as distractors
historical_readings = [
    [0.4, 0.7, 0.3],
    [0.8, 0.2, 0.6],
    [0.5, 0.5, 0.5]
]

# Main execution flow
metrics = [0.6, 0.8, 0.4, 0.9, 0.7]
weights = [1, 2, 3, 2, 1]

# Dead code block – misleading control flow
if __name__ == '__main__':
    temp_results = []
    for m in metrics:
        temp_results.append(m ** 2 if m > 0.5 else m ** 0.5)
    # This is never used

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")