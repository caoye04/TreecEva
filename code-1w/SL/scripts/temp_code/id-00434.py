from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def analyze_pattern(seq):
    freq = Counter(seq)
    return sum(v ** 2 for v in freq.values())

# Misleading transformation chain
def transform_signal(x):
    if x < 0:
        return abs(x) * 3
    elif x == 0:
        return 1
    else:
        return int(math.log(max(x, 1)) + 1)

# Unused normalization (dead code path)
def normalize_vector(vec):
    magnitude = sum(v ** 2 for v in vec) ** 0.5
    return [v / magnitude for v in vec] if magnitude > 0 else vec

# Complex processing with distractors
def preprocess_dataset(raw_data):
    temp_result = []
    overflow_flag = False
    
    for item in raw_data:
        # Distractor: irrelevant transformation
        transformed = transform_signal(item)
        shifted = transformed + 5 if transformed % 2 else transformed - 3
        
        # Real logic embedded here
        adjusted = abs(item) ** 0.5
        if adjusted > 4:
            adjusted = 4.0
        temp_result.append(adjusted)
        
        # Red herring: unused tracking
        if len(temp_result) > 10 and not overflow_flag:
            overflow_flag = True
    
    # Another decoy structure
    stats = defaultdict(int)
    for val in temp_result:
        stats[int(val)] += 1
    
    return temp_result

# Core scoring logic buried in complexity
def calculate_component_score(values, multipliers):
    score = 0.0
    bonus_applied = False
    penalty_threshold = 15
    
    for i, (v, m) in enumerate(zip(values, multipliers)):
        base_contribution = v * m
        
        # Conditional modification (looks complex but some branches are rare)
        if i % 4 == 0 and base_contribution > 2:
            base_contribution *= 1.25
        elif i % 3 == 0:
            base_contribution *= 0.9
        
        # Actual key rule: cap each contribution at 3.5
        capped = min(base_contribution, 3.5)
        score += capped
        
        # Distractor: tracking unused condition
        if score > penalty_threshold and not bonus_applied:
            bonus_applied = True

    # Final nonlinear adjustment (important)
    if score > 10:
        score = math.sqrt(score) * 2
    
    return round(score, 6)

# Main scoring function with misleading name
def calculate_final_score(dataset, importance_weights):
    # Preprocess — contains noise but real transformation inside
    cleaned = preprocess_dataset(dataset)
    
    # Weight alignment (some weights are ignored due to length)
    effective_weights = [
        w * 0.8 if i % 5 == 0 else w
        for i, w in enumerate(importance_weights[:len(cleaned)])
    ]
    
    # Compute main component score
    component = calculate_component_score(cleaned, effective_weights)
    
    # Fake fusion with unrelated metric
    phantom_metric = analyze_pattern([int(x) for x in cleaned if x > 1])
    dummy_offset = math.sin(phantom_metric) if phantom_metric > 0 else 0
    
    # Final computation — dummy_offset has negligible impact
    final_score = component + dummy_offset  # effectively just component due to sin()
    
    # Critical assignment point
    return round(final_score, 6)

# Simulated input data (deterministic)
data = [16, -9, 25, 0, 36, 49, -4, 64, 81, 100, 121]
weights = [0.5, 1.0, 1.5, 0.75, 2.0, 1.25, 0.9, 1.1, 1.3, 0.6, 1.4]

# Execution flow
processed = preprocess_dataset(data)
intermediate_score = calculate_component_score(processed, weights)
final_score = calculate_final_score(data, weights)

print(f"Result: {final_score}")