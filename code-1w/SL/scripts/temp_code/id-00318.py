def process_item_weights(items):
    weights = []
    for i, item in enumerate(items):
        if i % 2 == 0:
            weights.append(item * 1.5)
        else:
            weights.append(item * 0.8)
    return weights

items = [12, 7, 9, 14, 6]
weighted_items = process_item_weights(items)

# Irrelevant computation path (dead code)
def unused_helper(data):
    return [x ** 2 for x in data if x > 10]

junk_data = [3, 11, 15, 2]
irrelevant_result = unused_helper(junk_data)

# Misleading intermediate values
temp_offset = sum(weighted_items) // len(weighted_items)
scaling_factor = temp_offset * 0.3

# Real logic begins: rank adjustment using bitwise and dictionary mapping
base_values = [88, 92, 75, 85, 95]
modifiers = [True, False, True, False, True]
risk_flags = {i: val > 85 for i, val in enumerate(base_values)}

status_map = {0: 'low', 1: 'medium', 2: 'high', 3: 'critical'}
flag_summary = {}
for idx, flag in risk_flags.items():
    if flag:
        flag_summary[idx] = status_map.get(idx % 4, 'unknown')

# Conditional expression with zip and enumerate
adjusted_bases = [
    val + (10 if mod else -5) 
    for idx, (val, mod) in enumerate(zip(base_values, modifiers))
]

# Bitwise interference (some distractor usage)
dummy_mask = 0b1101
masked_values = [val ^ dummy_mask & 0b1010 for val in adjusted_bases]

# Actual critical calculation path
valid_corrections = []
for v in masked_values:
    if v > 90:
        valid_corrections.append(v // 3)
    elif v < 80:
        valid_corrections.append(v // 4)
    else:
        valid_corrections.append(v // 5)

# Helper function that appears complex but only one path matters
def calculate_adjusted_rank(values, flags):
    total = 0
    contribution_log = {}
    for i, (v, f) in enumerate(zip(values, flags)):
        # Only this branch contributes to final answer
        if f:
            contribution = (v * 2) ^ 7  # XOR introduces non-linearity
            total += contribution
            contribution_log[i] = contribution
        else:
            # Dead logic — never used
            backup = v + sum(contribution_log.values()) % 10
            continue  # Redundant control flow
    
    # Final transformation
    final_shift = total >> 1  # Right shift by 1
    return final_shift

# Key statement
final_score = calculate_adjusted_rank(base_values, modifiers)
print(f"Result: {final_score}")