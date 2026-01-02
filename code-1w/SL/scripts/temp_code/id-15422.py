def analyze_trend(data, threshold=0.5):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1] * (1 + threshold):
            trend.append('surge')
        elif data[i] < data[i-1] * (1 - threshold):
            trend.append('drop')
        else:
            trend.append('stable')
    return trend

# Irrelevant helper function (dead code path)
def normalize_values(arr):
    max_val = max(arr)
    return [x / max_val for x in arr]

def compute_entropy(weights):
    import math
    entropy = 0
    for w in weights:
        if w > 0:
            entropy -= w * math.log(w)
    return round(entropy, 4)

# Misleading metrics with decoy calculations
temporal_weights = [0.1, 0.2, 0.4, 0.2, 0.1]
entropy_value = compute_entropy(temporal_weights)  # Decoy usage

system_log = {
    'events': ['start', 'update', 'save', 'crash', 'restart', 'update', 'exit'],
    'timestamps': [100, 150, 200, 250, 300, 350, 400],
    'priority': [1, 2, 1, 5, 2, 3, 1]
}

# Unused transformation (distractor)
delayed_sequence = [x * 2 for x in system_log['timestamps']][::2]

benchmark_data = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [1, 3, 2, 5, 4]
]

aggregated = []
for row in benchmark_data:
    row_avg = sum(row) / len(row)
    aggregated.append(row_avg)

# Slice-based processing (key python feature)
cropped_data = aggregated[1:]  # Remove first element
smoothed = [sum(cropped_data[i:i+2]) / 2 for i in range(len(cropped_data) - 1)]

status_flags = {"active": True, "debug": False, "verbose": True}

# Conditional logic with red herring branch
if status_flags["debug"]:
    debug_trace = [x ** 0.5 for x in smoothed]  # Never executed
else:
    adjusted = [x * 1.1 for x in smoothed]  # Relevant path

# Dictionary-based mapping with irrelevant entries
scaling_map = {
    'alpha': 1.05,
    'beta': 1.08,
    'gamma': 1.12,  # This one is used
    'delta': 1.03
}

scaled_values = [x * scaling_map['gamma'] for x in adjusted]

# Simulate performance metric extraction
metrics = {
    'baseline': sum(aggregated) / len(aggregated),
    'volatility': max(scaled_values) - min(scaled_values),
    'consistency': len([v for v in scaled_values if v > 6.0]),
    'peak': max(scaled_values)
}

# Unused recursive function (decoy)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

unused_series = [fibonacci(i) for i in range(6)]  # Dead computation

# Core evaluation logic (target)
def evaluate_performance(met, data):
    base = met['baseline']
    vol = met['volatility']
    cons = met['consistency']
    peak = met['peak']
    
    # Complex conditional scoring
    if cons >= 2 and vol < 3.0:
        score = base * 1.5 + peak * 0.8
    elif peak > 7.0:
        score = base * 1.2 + cons * 2.0
    else:
        score = base + vol * 0.5
    
    # Additional adjustment using slicing on nested data
    bonus_region = data[1][2:4]  # Extracts [6, 8]
    bonus = sum(bonus_region) / 10.0  # 1.4
    
    # Final score with bonus
    final = int(score + bonus)  # Key result
    
    # Red herring assignment (misleads with float)
    final_float = round(score + bonus + 0.456, 3)
    
    return final

# Execution point of interest
final_score = evaluate_performance(metrics, benchmark_data)
print(f"Target result: {final_score}")