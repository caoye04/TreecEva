def analyze_pattern(sequence, depth):
    if depth == 0:
        return sum(sequence) % 7
    transformed = [seq * (depth % 2 + 1) for seq in sequence]
    shifted = transformed[1:] + [transformed[0]]
    return analyze_pattern(shifted, depth - 1)

# Irrelevant helper (dead path)
def unused_helper(data):
    return sorted(data, reverse=True)

# Distractor: complex-looking but unused function
def compute_entropy(arr):
    from math import log
    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(arr)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Decoy variables
temp_buffer = [0] * 100
mask_value = 0xFF
offset_table = {i: i**2 for i in range(10)}

# Real data with distractors mixed in
raw_metrics = [3, 6, 9, 12, 15]
scaling_factor = 2.5
base_threshold = 8
adjustment_mode = True if sum(raw_metrics) > 40 else False

# Red herring computation
aggregate = 0
for val in raw_metrics:
    aggregate += val * scaling_factor

# Conditional expression with slicing distraction
subset_data = raw_metrics[1:4] if adjustment_mode else raw_metrics[0:2]
processed = [x + 1 for x in subset_data]

# Key recursive logic (hidden among noise)
def evaluate_performance(logs, threshold):
    size = len(logs)
    peak = max(logs)
    valid_entries = [x for x in logs if x >= threshold]
    score = len(valid_entries) * 10
    
    # Hidden dependency on analyze_pattern
    aux_score = analyze_pattern([size, peak, threshold], 3)
    
    # Distractor block (never executed due to condition)
    extra_bonus = 0
    if len(logs) > 100:
        extra_bonus = sum(logs) // 100
    
    # Critical calculation
    final = score + aux_score + (5 if adjustment_mode else -5)
    return final

# Unused list comprehension red herring
_ = [i*j for i in range(3) for j in range(3) if i != j]

# Bit manipulation decoy (irrelevant)
bit_flag = (0b1010 << 3) & 0b1111000

# Character counting distractor
text_snippet = "performance evaluation"
char_count = sum(1 for c in text_snippet if c in 'aeiou')

# Main execution
metric_data = [5, 8, 9, 10, 12]
final_score = evaluate_performance(metric_data, base_threshold)

# Output result as required
print(f"Result: {final_score}")