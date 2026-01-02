from collections import defaultdict, Counter
from itertools import combinations

# Simulate system health monitoring with performance scoring
def analyze_sequence(data):
    counts = Counter(data)
    total_pairs = 0
    for k, v in counts.items():
        if v > 1:
            total_pairs += v * (v - 1) // 2
    return total_pairs

def generate_patterns(elements):
    # Irrelevant function: generates all 3-element combos (dead path)
    patterns = []
    for c in combinations(elements, 3):
        patterns.append(c)
    return len(patterns)  # Never used

def compute_entropy(arr):
    # Misleading computation: looks important but unused
    from math import log2
    freq = Counter(arr)
    total = len(arr)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)

def normalize_values(raw_scores):
    min_val = min(raw_scores)
    max_val = max(raw_scores)
    if max_val == min_val:
        return [1.0] * len(raw_scores)
    return [(x - min_val) / (max_val - min_val) for x in raw_scores]

def filter_outliers(data, threshold=1.5):
    # Dead code path: defined but not invoked in critical flow
    median = sorted(data)[len(data)//2]
    deviances = [abs(x - median) for x in data]
    mad = sorted(deviances)[len(deviances)//2]  # Median absolute deviation
    if mad == 0:
        return data
    filtered = [x for x in data if abs(x - median) / mad <= threshold]
    return filtered

def bitwise_diagnostic(value):
    # Distractor: complex bit logic that feeds into unused variables
    shifted = (value << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    parity = bin(toggled).count('1') % 2
    return toggled | (parity << 8)

def evaluate_component_health(status_log):
    history = defaultdict(int)
    score = 0
    for event in status_log:
        history[event] += 1
        if event == 'ERROR':
            score -= 10
        elif event == 'WARNING':
            score -= 3
        elif event == 'INFO':
            score += 1
        else:
            score += 2
    # Complex interdependency: only final score matters
    adjustment = len([v for v in history.values() if v > 2])
    return score + adjustment

def transform_features(features):
    # Unused transformation chain
    transformed = {}
    for k, v in features.items():
        if isinstance(v, int):
            transformed[k] = (v ** 2) % 97
        else:
            transformed[k] = hash(str(v)) % 100
    return transformed

def evaluate_performance(metrics, weights):
    # Core function - evaluates weighted performance score
    base_score = 0
    temp_results = []
    
    # Real logic begins
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        if i % 2 == 0:
            base_score += metric * weight * 0.8
        else:
            adjusted = metric * 1.2
            temp_results.append(adjusted)
    
    # Secondary aggregation
    secondary_sum = sum(temp_results) * 0.9
    
    # Inject irrelevant intermediate steps
    dummy_data = [1, 1, 2, 3, 5, 8, 13]
    fibonacci_check = analyze_sequence(dummy_data)  # returns 3 (from duplicates? no — actually 0)
    
    # More distractions
    _ = compute_entropy([1,2,2,3,3,3,4,4,4,4])  # Called but result ignored
    
    # Bit manipulation decoy
    diagnostic_code = bitwise_diagnostic(len(metrics))
    
    # Real continuation: combine base and secondary
    final_raw = base_score + secondary_sum
    
    # Normalization using real data
    normalized_input = normalize_values(metrics + weights)
    scaling_factor = normalized_input[0] * 2.5  # Use first normalized value
    
    # Final calculation
    final_score = int((final_raw * scaling_factor) - diagnostic_code % 100)
    
    # Critical red herring: this looks like it affects output but doesn't
    _ = transform_features({'metrics_len': len(metrics), 'version': 'A'})
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    metrics = [45, 82, 33, 71, 59]
    weights = [0.2, 0.5, 0.3, 0.8, 0.4]
    
    # Irrelevant pre-processing
    raw_events = ['INFO', 'INFO', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'DEBUG', 'DEBUG']
    health_score = evaluate_component_health(raw_events)  # Computed but unused
    
    # Generate unused pattern count
    _ = generate_patterns(['A','B','C','D','E'])
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Output result as required
    print(f"Target result: {final_score}")