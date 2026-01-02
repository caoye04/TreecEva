def preprocess_item(x):
    if x < 0:
        return x * -1
    elif x == 0:
        return 1
    return x + 2

# Irrelevant transformation chain
def transform_sequence(seq):
    temp = []
    for i, val in enumerate(seq):
        temp.append(val * (i + 1))
    return [v for v in temp if v % 2 == 0]

# Decoy function that looks important but isn't used in final path
def compute_legacy_metric(arr):
    total = 0
    for item in arr:
        total += item ** 2
    return total / len(arr) if arr else 0

# Core calculation with distractors
def calculate_base_metrics(values, multipliers):
    result = 0
    adjustment = 0
    
    # Red herring loop with unused accumulator
    unused_sum = 0
    for idx, (v, m) in enumerate(zip(values, multipliers)):
        unused_sum += v * (m % idx if idx != 0 else m)
    
    # Actual logic buried in distractions
    scaling_factor = 1.5 if len(values) > 3 else 1.0
    weighted_items = map(lambda x: x[0] * x[1] * scaling_factor, zip(values, multipliers))
    
    # Early termination red herring
    if sum(multipliers) == 0:
        return 0
    
    result = sum(weighted_items)
    
    # Secondary adjustment with conditional expression
    adjustment = sum([preprocess_item(v) for v in values]) if result > 0 else 0
    
    return result + adjustment

# Complex weight adjustment with dead code branch
def adjust_weights(w):
    new_w = w.copy()
    temp_store = {}  # Unused cache
    
    for i in range(len(new_w)):
        if i % 3 == 0 and i != 0:  # Rare condition never met in practice
            temp_store[i] = new_w[i] * 2
        elif i < 5:
            new_w[i] *= 0.9
    
    # Dead code path
    if False:
        for k in temp_store:
            new_w[k] += temp_store[k]
    
    return new_w

# Main scoring logic with nested distractions
def calculate_final_score(raw_data, importance_weights):
    # Preprocessing with irrelevant filtering
    filtered_data = [x for x in raw_data if x != -999]
    cleaned_data = list(map(preprocess_item, filtered_data))
    
    # Distractor: tuple unpacking that isn't fully used
    summary_stats = {
        'min_val': min(cleaned_data),
        'max_val': max(cleaned_data),
        'range': lambda: max(cleaned_data) - min(cleaned_data)
    }
    
    # Weight adjustment (actually used)
    adjusted_weights = adjust_weights(importance_weights)
    
    # Secondary metric computed but only conditionally used
    secondary_score = 0
    for idx, val in enumerate(cleaned_data):
        if idx % 2 == 1:
            secondary_score += val * 0.1
    
    # Primary score calculation
    base_score = calculate_base_metrics(cleaned_data, adjusted_weights)
    
    # Conditional override that won't trigger
    if summary_stats['min_val'] < 0 and summary_stats['max_val'] > 1000:
        return secondary_score * 10
    
    # Final composition - this is the actual answer path
    volatility_index = sum(1 for i in range(1, len(cleaned_data)) if abs(cleaned_data[i] - cleaned_data[i-1]) > 2)
    penalty = volatility_index * 0.5 if volatility_index > 3 else 0
    
    final_component = base_score - penalty + secondary_score
    
    # Key execution point
    final_score = int(round(final_component))
    
    return final_score

# Irrelevant global variables
MAX_THRESHOLD = 9999
DEFAULT_PADDING = [0, 0, 0]

# Input data with meaningful and distracting elements
data = [4, -2, 7, 1, 9, -999, 3]  # -999 is filtered out
weights = [0.8, 1.2, 0.9, 1.1, 0.7, 1.3, 0.6]

# Trigger computation
final_score = calculate_final_score(data, weights)

print(f"Result: {final_score}")