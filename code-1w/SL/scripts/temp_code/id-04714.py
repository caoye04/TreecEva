from collections import defaultdict
import math

# Irrelevant helper function (decoy)
def analyze_pattern(seq):
    freq = defaultdict(int)
    for item in seq:
        freq[item] += 1
    return {k: v for k, v in freq.items() if v > 1}

# Misleading data transformation (red herring)
def transform_signal(x):
    return [math.sin(i * 0.1) * 2 for i in range(len(x))]

# Unused utility (dead code path)
calculate_offset = lambda base, shift: (base * 0.9 + shift * 1.1) % 7

# Core logic disguised among distractions
def evaluate_item(value, weight):
    if value < 0:
        temp = abs(value) ** 0.5
    else:
        temp = value + 1
    adjusted = temp * weight
    if adjusted > 100:
        adjusted = 100 + (adjusted - 100) / 10  # Dampening effect
    return round(adjusted, 3)

# Another decoy function with plausible but unused logic
def normalize_vector(vec):
    magnitude = sum(x ** 2 for x in vec) ** 0.5
    return [round(x / magnitude, 4) for x in vec] if magnitude else vec

# Key processing function with embedded logic chain
def process_results(raw_data, importance_weights):
    # Step 1: Filter valid entries
    filtered = [(v, w) for v, w in zip(raw_data, importance_weights) if isinstance(v, (int, float)) and w > 0]
    
    # Step 2: Apply nonlinear transformation
    transformed = []
    for val, wt in filtered:
        if val == 0:
            result = 1.0
        elif val > 10:
            result = math.log(val) * 2
        elif val < -5:
            result = abs(val) ** 0.3
        else:
            result = val * 1.5
        transformed.append((result, wt))
    
    # Step 3: Weighted evaluation
    scores = []
    for t_val, weight in transformed:
        raw_score = evaluate_item(t_val, weight)
        # Artificial complexity: conditional bonus
        if raw_score > 50 and weight >= 2:
            raw_score *= 1.1
        scores.append(raw_score)
    
    # Step 4: Aggregate with damping on outliers
    sorted_scores = sorted(scores)
    if len(sorted_scores) > 4:
        trimmed = sorted_scores[1:-1]  # Remove min and max
    else:
        trimmed = sorted_scores
    
    # Step 5: Final computation
    total = sum(trimmed)
    count = len(trimmed)
    average = total / count if count else 0
    
    # Step 6: Apply business rule (threshold adjustment)
    if average < 20:
        final = average * 1.8
    elif average > 80:
        final = average * 0.95
    else:
        final = average + 5
    
    # Step 7: Round to nearest integer
    return int(round(final))

# Irrelevant dataset (distractor)
pattern_data = ['A', 'B', 'A', 'C', 'B', 'A', 'D']
signal_input = list(range(50))

# Used data (buried among others)
data = [12, -3, 0, 15, 8, -10, 25]
weights = [2.0, 1.5, 0.5, 3.0, 1.0, 2.5, 4.0]

# Dead code with plausible call (misdirection)
offset_val = calculate_offset(5, 3)
normalized_data = normalize_vector([3, 4, 5])

# Critical execution point
final_score = process_results(data, weights)

# Output the target result
print(f"Target result: {final_score}")