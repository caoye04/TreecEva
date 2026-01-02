from itertools import compress, cycle

def analyze_efficiency(values):
    # Irrelevant helper function with dead-end logic
    running = []
    for v in values:
        if v > 50:
            running.append(v * 0.1)
    return [x for x in running if x < 7]  # Not used later

def preprocess_data(raw):
    # Misleading transformation that isn't directly used
    cleaned = [s.strip().lower() for s in raw]
    converted = [c.title() for c in cleaned]
    return converted

def evaluate_performance(metrics, weights):
    base = sum(m * w for m, w in zip(metrics, weights))
    adjustment = 0
    
    # Simulate conditional bonus based on patterns
    if len(metrics) % 2 == 0:
        adjustment += 10
    else:
        adjustment -= 5
    
    # Distractor loop: computes something irrelevant
    temp_results = []
    for i in range(3):
        temp = 0
        for j in range(i+1):
            temp += j ** 2
        temp_results.append(temp)  # Unused afterward
    
    # Real computation continues
    multiplier = 1.5 if all(m > 20 for m in metrics) else 1.0
    intermediate = base * multiplier
    
    # Another red herring: string processing with no impact
    status_labels = ['low', 'medium', 'high']
    case_transformed = list(map(str.upper, status_labels))
    flag_check = any('HIGH' in x for x in case_transformed)  # True but unused
    
    # Final adjustment using lambda filter via itertools
    valid_weights = list(compress(weights, [w > 0.1 for w in weights]))
    weight_filter = list(map(lambda x: x + 0.05, cycle(valid_weights)))[:len(valid_weights)]
    final_adjustment = sum(weight_filter) * 0.2
    
    result = intermediate + final_adjustment + adjustment
    return int(result)

# Main execution block
raw_input = ["  Data  ", "Input", "Stream"]
preprocessed = preprocess_data(raw_input)

# Core data for actual calculation
metrics_data = [45, 60, 75, 80]  # Performance metrics
weight_scheme = [0.3, 0.25, 0.35, 0.1]  # Importance weights

# Dead code path: linear search never called
def find_threshold(data, target):
    for idx, val in enumerate(data):
        if val >= target:
            return idx
    return -1

# Actual key computation
final_score = evaluate_performance(metrics_data, weight_scheme)
print(f"Target result: {final_score}")