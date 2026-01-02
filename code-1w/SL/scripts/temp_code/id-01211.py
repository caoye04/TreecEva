from itertools import combinations
import math

# Irrelevant utility function (decoy)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v]

# Unused transformation table (distractor)
transform_map = {
    'A': lambda x: x * 2,
    'B': lambda x: x + 10,
    'C': lambda x: int(math.sqrt(x))
}

# Misleading intermediate calculations
baseline_offset = 42
scaling_factor = 1.75
noise_sequence = [i * scaling_factor for i in range(5)]

# Actual core logic disguised among distractors
def evaluate_item(value, weight):
    if value < 0:
        return 0
    return int((value * weight) ** 0.8)

# Red herring function that's never called
def deprecated_scoring(items):
    total = 0
    for item in items:
        if item % 3 == 0:
            total += item // 3
    return total

# Real processing function with nested logic
def process_results(data, weights):
    temp_results = []
    
    # Nested comprehension with filtering (relevant)
    filtered_pairs = [
        (d, w) for d, w in zip(data, weights) 
        if d > 5 and w > 0
    ]
    
    # Irrelevant bit manipulation block (dead path)
    debug_flags = 0
    for i in range(3):
        debug_flags |= (1 << i)
        debug_flags ^= (i + 1)
    
    # Core computation with lambda and combination logic
    combo_boost = 0
    if len(filtered_pairs) >= 3:
        # Meaningful but non-obvious interaction
        valid_combos = list(combinations(range(len(filtered_pairs)), 3))
        combo_values = [
            sum(filtered_pairs[i][0] for i in c) for c in valid_combos
            if all(filtered_pairs[i][1] >= 1.0 for i in c)
        ]
        if combo_values:
            max_combo = max(combo_values)
            # Key transformation using exponent and floor
            combo_boost = int(math.floor(max_combo ** 0.6))
    
    # Primary accumulation loop
    for d, w in filtered_pairs:
        # Non-linear evaluation
        score = evaluate_item(d, w)
        temp_results.append(score)
    
    # Final aggregation with offset distraction
    base_total = sum(temp_results)
    adjustment = len(temp_results) * 3
    
    # Final result influenced by combo_boost (critical path)
    final_value = base_total + adjustment + combo_boost - baseline_offset
    
    # Dead code branch (never executes due to logic)
    if baseline_offset < 0:
        final_value *= 2
        
    return final_value

# Irrelevant global constants
MAX_BUFFER_SIZE = 1024
PACKET_HEADER = b'\xDE\xAD\xBE\xEF'

# Input data (meaningful)
data = [12, -3, 8, 15, 6]
weights = [1.2, 0.5, 1.0, 1.5, 0.8]

# Spurious list comprehension (no side effects)
dummy_transform = [math.ceil(x * 0.1) for x in data if x % 2 == 0]

# Critical execution point
final_score = process_results(data, weights)

# Output result as required
print(f"Result: {final_score}")