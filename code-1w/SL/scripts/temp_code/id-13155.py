from collections import defaultdict
import math

def preprocess_data(raw):
    # Irrelevant preprocessing step with distractor logic
    temp_result = defaultdict(int)
    for k, v in raw.items():
        if v > 0:
            temp_result[k] = math.log(v + 1) * 0.8
    return temp_result

def filter_outliers(values):
    # Semi-relevant filtering (not actually used in final path)
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [x for x in values if abs(x - mean_val) <= 2 * std_dev]

def calculate_composite_metrics(d):
    # Complex but partially irrelevant metric calculation
    magnitude = sum(v**2 for v in d.values()) ** 0.5
    entropy = -sum((v/magnitude) * math.log(v/magnitude) for v in d.values() if v > 0)
    return {'magnitude': magnitude, 'entropy': entropy}

def calculate_final_score(data, weights):
    # Core logic begins here
    normalized = {}
    total = sum(data.values())
    
    for k, v in data.items():
        normalized[k] = v / total if total != 0 else 0
    
    # Introduce misleading intermediate variables
    adjustment_factor = 1.0
    decay = 0.95
    for i in range(2):  # Nested loop - adds complexity
        for k in normalized:
            normalized[k] *= decay
            decay = max(0.9, decay * 0.98)  # Distracting state update
    
    # Relevant weighted aggregation
    score = 0.0
    for k, v in normalized.items():
        weight = weights.get(k, 0.5)
        contribution = v * weight
        score += contribution
    
    # Additional plausible but simple transformation
    score = max(0, score * 100)
    
    # Dead code path - misleading conditional
    if score < 0:
        score *= -1  # Never executed
    
    # Final computation step
    bonus = len([w for w in weights.values() if w > 0.7]) * 2.5
    final_score = score + bonus
    
    return final_score

# Main execution
raw_data = {'input_A': 45, 'input_B': 67, 'input_C': 23, 'input_D': 89}
weights = {'input_A': 0.6, 'input_B': 0.8, 'input_C': 0.4, 'input_D': 0.75}

# Call helper functions that do not affect final result
processed = preprocess_data(raw_data)
metrics = calculate_composite_metrics(raw_data)

# Key statement
final_score = calculate_final_score(raw_data, weights)

print(f"Result: {final_score}")