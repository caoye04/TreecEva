def analyze_pattern(sequence):
    if len(sequence) < 5:
        return sum(sequence) * 2
    else:
        return sum(x ** 2 for x in sequence if x % 2 == 0)

# Irrelevant helper function (decoy)
def compute_entropy(values):
    import math
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

# Unused transformation (dead code path)
def transform_legacy(items):
    return [item << 1 for item in items][::-1]

# Distractor variables
temp_offset = 42
buffer_zone = [1, 3, 5, 7]
shadow_mask = 0xFF

# Real data pipeline
config = {
    'threshold': 15,
    'mode': 'aggressive',
    'scaling': 1.5
}

raw_data = [4, 6, 2, 8, 5, 3, 9, 1]
filtered_data = [x for x in raw_data if x > 3]
sliced_view = filtered_data[1:6]  # slicing operation

# Set operations used meaningfully
data_set_a = set(sliced_view)
data_set_b = {2, 4, 6, 8}
overlap = data_set_a & data_set_b

# Conditional expression with distraction
bonus_flag = True if len(overlap) >= 2 and config['mode'] == 'aggressive' else False
adjustment = 10 if bonus_flag else 0

# Main processing chain
def process_metrics(data, cfg):
    base = sum(data)
    
    # Complex conditional logic with red herring variables
    if base > cfg['threshold']:
        multiplier = cfg['scaling']
        
        # Nested logic with distractors
        secondary_score = 0
        for i, val in enumerate(data):
            if i % 2 == 0:
                secondary_score += val * 3
            else:
                # This block looks important but contributes minimally
                temp = val ^ 7
                secondary_score += min(temp, val + 2)
        
        # Bit manipulation decoy (used but not impactful)
        masked_value = base & shadow_mask
        
        # Key computation
        outcome = base * multiplier + adjustment
        
        # More distractions
        outlier_check = any(x > 20 for x in data)
        fallback = max(data) * 5
        
        # Final decision influenced only by core factors
        final_outcome = outcome if not outlier_check else fallback
        
        return int(final_outcome)
    
    else:
        return min(data) * 10

# Execution point of interest
data = [x + 1 for x in sliced_view if x in overlap or x % 4 == 0]
final_score = process_metrics(data, config)

# Output requirement
print(f"Result: {final_score}")