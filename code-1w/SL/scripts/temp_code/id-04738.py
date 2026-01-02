from itertools import combinations

def analyze_efficiency(values):
    # Irrelevant helper function with dead logic
    temp = [v ** 2 for v in values if v > 0]
    smoothed = [t * 0.95 for t in temp]
    return sum(smoothed) // len(smoothed) if smoothed else 0

def compute_baseline(data):
    # Distractor computation
    base = 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            base += x * 1.1
    return int(base)

def process_performance(metrics, adjustments):
    # Core logic begins
    cumulative = 0
    history = {}
    
    for key in sorted(metrics.keys()):
        raw_value = metrics[key]
        adjustment_factor = adjustments.get(key, 1.0)
        
        # Apply adjustment
        adjusted = raw_value * adjustment_factor
        
        # Track transformed values (semi-relevant)
        if adjusted > 50:
            history[key] = round(adjusted, 2)
        
        # Actual contribution to result
        if key.startswith('p'):
            cumulative += int(adjusted // 10)
        elif key.endswith('x'):
            cumulative -= int(abs(adjusted) // 20)
    
    # Real core operation: count valid high performers
    high_performers = [k for k, v in history.items() if v > 75]
    bonus = len(high_performers) * 5
    
    # Dummy sorting with no impact
    sorted_keys = sorted(history.keys(), key=lambda x: history[x], reverse=True)
    shadow_total = sum([ord(c) for c in ''.join(sorted_keys)])  # unused
    
    # Final computation
    outlier_check = [v for v in metrics.values() if v > 90]
    penalty = 10 if len(outlier_check) >= 3 else 0
    
    final_score = cumulative + bonus - penalty
    
    # Use of dictionary and itertools (required features)
    pairs = list(combinations(history.keys(), 2))
    pair_count = len(pairs)  # distractor metric
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    metrics = {
        'p1': 85,
        'p2': 92,
        'p3': 45,
        'ax': 60,
        'bx': 95,
        'cx': 30,
        'py': 70
    }
    adjustments = {
        'p1': 1.2,
        'p2': 0.95,
        'ax': 1.1,
        'bx': 0.8,
        'py': 1.0
    }
    
    # Dead code path
    if False:
        dummy = compute_baseline([10, 20, 30])
    
    # Key statement
    final_score = process_performance(metrics, adjustments)