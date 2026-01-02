def analyze_trends(raw_values):
    # Irrelevant transformation: normalizes values but not used in final result
    normalized = [round((x - min(raw_values)) / (max(raw_values) - min(raw_values)) * 100) for x in raw_values]
    trend_line = sum(normalized[i] - normalized[i-1] for i in range(1, len(normalized)))
    return trend_line

# Decoy data that looks important but unused
trend_data = [120, 135, 140, 138, 150, 160, 155]
analyze_trends(trend_data)

thresholds = {'low': 30, 'medium': 60, 'high': 90}
def process_metrics(entries):
    # Another distractor: processes entries but returns only a flag
    valid_count = sum(1 for e in entries if e > thresholds['medium'])
    return valid_count > 4

entry_list = [55, 65, 70, 75, 80, 85, 95]
process_metrics(entry_list)

def compute_weighted_index(data):
    # Unused complex logic with list comprehension and conditionals
    weights = [0.1, 0.2, 0.3, 0.4] if len(data) > 5 else [0.25] * 4
    weighted = sum(data[i] * weights[i % 4] for i in range(len(data)))
    adjusted = weighted * (1.1 if weighted < 300 else 0.95)
    return int(adjusted)

sample_data = [40, 50, 60, 70, 80, 90]
compute_weighted_index(sample_data)

# Core logic disguised among decoys
def evaluate_performance(metrics):
    # Key computation path begins here
    base = sum(x for x in metrics if x % 2 == 1)  # Sum of odd values
    adjustment = len([x for x in metrics if x > 50])  # Count of values > 50
    
    # Conditional expression used meaningfully
    penalty = 10 if any(metrics[i] < metrics[i+1] for i in range(len(metrics)-1)) else 0
    
    # Bit manipulation red herring
    encoded = 0
    for x in metrics:
        encoded ^= x  # XOR chain - looks important but irrelevant
    
    # Dead code path: function defined but not affecting output
    def recalculate(x):
        return x << 1 if x < 100 else x >> 1
    
    # Real calculation hidden among distractions
    intermediate = (base + adjustment * 5) % 97
    scaling_factor = 3 if intermediate > 50 else 2
    
    # Final derivation using tuple unpacking (distractor)
    config = (scaling_factor, 7)
    scale, offset = config
    
    result = intermediate * scale + offset
    
    # This variable is critical
    final_score = result - penalty
    
    # Print ensures visibility
    return final_score

# Actual input data
metric_data = [23, 44, 57, 62, 71, 39, 88]
final_score = evaluate_performance(metric_data)
print(f"Target result: {final_score}")