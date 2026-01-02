def analyze_signal(data, limit):
    magnitude = sum(x ** 2 for x in data if x > 0)
    normalized = magnitude ** 0.5
    
    # Irrelevant transformation (distractor)
    inverted = [1 / (x + 1) for x in data]
    avg_inverted = sum(inverted) / len(inverted)
    
    # Semi-relevant preprocessing
    clipped = [min(x, limit) for x in data]
    total_energy = sum(clipped)
    
    # Red herring: unused computation
    entropy = 0
    for x in clipped:
        if x > 0:
            entropy -= x * __import__('math').log(x)
    
    # Core logic branch
    if total_energy > limit * 2:
        category = 'strong'
        adjustment = 10
    elif total_energy > limit:
        category = 'moderate'
        adjustment = 5
    else:
        category = 'weak'
        adjustment = 0
    
    # String-based state encoding (uses string method)
    status_flag = f"DIAGNOSTIC_{category.upper()}"
    code_suffix = status_flag[-3:]  # slicing operation
    
    # Final decision with side computation
    baseline = len(code_suffix) * 2
    final_score = baseline + adjustment
    
    # Actual answer derivation
    correction_factor = data.count(0)  # counts zeros in original signal
    final_diagnostic = final_score - correction_factor
    
    return final_diagnostic

# Setup input
pattern_buffer = [0, 4, -1, 3, 0, 2, 5]
threshold = 3

# Execute
final_diagnostic = analyze_signal(pattern_buffer, threshold)
print(f"Result: {final_diagnostic}")