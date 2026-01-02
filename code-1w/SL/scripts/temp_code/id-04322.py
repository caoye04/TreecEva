from itertools import combinations

def analyze_frequency(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def generate_pairs(elements):
    # Irrelevant helper that's called but not used in final logic
    return list(combinations(elements, 2))

def compute_entropy(values):
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * __import__('math').log2(prob)
    return round(entropy, 4)

def validate_range(val, low=0, high=100):
    # Distractor function: looks important but only used once trivially
    return low <= val <= high

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    max_possible = 0
    temp_adjustment = 0

    # Simulate intermediate state tracking
    status_log = []
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        if metric < 50:
            status_log.append(f"metric_{i}_low")
            temp_adjustment += 5
        else:
            status_log.append(f"metric_{i}_ok")
    
    # Core logic embedded with distractions
    for idx in range(len(metrics)):
        raw_val = metrics[idx]
        w = weights[idx]
        
        # Artificial complexity: some normalization that doesn't change outcome
        normalized_metric = (raw_val - 20) if raw_val > 60 else raw_val
        adjusted_metric = min(100, max(0, normalized_metric))
        
        # Dead code path based on impossible condition (adds interference)
        if len(status_log) > 100:  # Never true
            adjusted_metric = 0
        
        weighted_sum += adjusted_metric * w
        max_possible += 100 * w
    
    # Real answer computed here
    efficiency_ratio = weighted_sum / max_possible
    
    # Distractor variables
    phantom_score = (metrics[0] ** 2) % 97
    debug_trace = set(status_log)
    
    final_score = int(weighted_sum)  # This is what we actually want
    
    # Early return red herring (never triggers due to data)
    if efficiency_ratio > 1.0:
        return -1
        
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    metrics = [78, 85, 92, 67, 88]
    weights = [0.2, 0.3, 0.25, 0.15, 0.1]
    
    # Irrelevant preprocessing
    text_data = "performanceevaluationmetrics"
    freq_map = analyze_frequency(text_data)
    unique_chars = set(freq_map.keys())
    pairs = generate_pairs([10, 20, 30])  # Computed but unused
    
    # Key computation
    final_score = evaluate_performance(metrics, weights)
    
    # Additional distraction
    entropy_value = compute_entropy(list(freq_map.values()))
    range_check = validate_range(sum(weights) * 100)  # Always True
    
    print(f"Result: {final_score}")