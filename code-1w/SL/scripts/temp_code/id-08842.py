def analyze_pattern(seq):
    count = 0
    for i, val in enumerate(seq):
        if i % 2 == 0 and val > 3:
            count += val * 2
    return count

# Irrelevant helper (distractor)
def compute_hash(s):
    h = 0
    for c in s:
        h = (h * 31 + ord(c)) % 10007
    return h

# Unused transformation function (dead code path)
def transform_values(arr):
    return [x ** 0.5 for x in arr if x > 10]

# Misleading normalization factor (red herring)
normalization_bias = sum([i * 1.5 for i in range(7)]) / 4.0

# Spurious data structure (distractor)
user_preferences = {
    'theme': 'dark',
    'auto_save': True,
    'timeout': 300,
    'priority': 'low'
}

# Core logic disguised among noise
def filter_critical(x):
    return x > 0 and (x % 2 == 1 or x == 4)

def evaluate_stability(index, value):
    if index < 5:
        return value * 1.1
    else:
        return value * 0.9 if value % 2 == 0 else value * 1.05

def aggregate_signals(values):
    total = 0.0
    for idx, v in enumerate(values):
        if filter_critical(v):
            adjusted = evaluate_stability(idx, v)
            total += adjusted
    return total

def process_metrics(data, weights):
    temp_results = []
    for d, w in zip(data, weights):
        temp_results.append(d * w)
    
    # Secondary processing with conditional expression
    refined = [x if x > 5 else x * 1.2 for x in temp_results]
    
    # Key computation hidden in middle
    base_score = aggregate_signals(refined)
    penalty = 0
    for i, r in enumerate(refined):
        if i % 3 == 0 and r > 7:
            penalty += 2.5
    
    # Final result built from multiple concepts
    final_score = int(base_score - penalty) + 10  # Offset to avoid zero
    
    # Decoy assignment (misleading)
    final_score = final_score * 1  # No-op but looks meaningful
    
    return final_score

# Real input data (not obviously connected)
data = [3, 5, -2, 8, 4, 7]
weights = [1.0, 0.8, 1.2, 0.5, 1.1, 0.9]

# Call the main function
final_score = process_metrics(data, weights)
print(f"Target result: {final_score}")