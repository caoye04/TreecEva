def analyze_pattern(sequence, threshold):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] > threshold:
            count += 1
            if count > 3:
                break
    return count

# Irrelevant helper function (distractor)
def calculate_entropy(data):
    import math
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(data)
    for f in freq.values():
        p = f / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Unused transformation (dead code path)
def transform_sequence(seq):
    return [x ** 2 - x for x in seq if x % 2 == 0]

# Decoy metric with misleading intermediate result
temp_result = 0
def track_progress(value, mode="linear"):
    global temp_result
    if mode == "quadratic":
        temp_result += value ** 2
    else:
        temp_result += value * 1.5
    return temp_result

# Core logic disguised among distractions
baseline = [12, 15, 18, 21, 24]
def evaluate_performance(metrics, base):
    offset = len(base) % 4
    adjusted = [m - base[i % len(base)] for i, m in enumerate(metrics)]
    
    # Conditional expression used
    scaling_factor = 1.75 if sum(adjusted) > 0 else 0.85
    
    # Slicing operation used
    segment = adjusted[:len(adjusted)//2 + 1]
    
    # Real computation hidden among red herrings
    raw_score = 0
    for val in segment:
        if val >= 0:
            raw_score += int(val * scaling_factor)
        else:
            raw_score -= abs(int(val / scaling_factor))
    
    # Multiple concepts: conditionals, slicing, arithmetic, logic
    penalty = 0
    if len(metrics) > 5 and metrics[0] < metrics[-1]:
        penalty = -7
    elif analyze_pattern(metrics, 10) == 4:
        penalty = -3
    
    final_score = raw_score + penalty
    
    # Distractor: unused variables and side-effect calls
    _ = calculate_entropy([1, 2, 2, 3, 3, 3])
    _ = track_progress(5, mode="quadratic")
    _ = transform_sequence([4, 6, 8, 10])
    
    return final_score

# Input data with meaningful structure
metric_data = [25, 30, 10, 40, 15, 20]

# Key execution point
final_score = evaluate_performance(metric_data, baseline)

print(f"Result: {final_score}")