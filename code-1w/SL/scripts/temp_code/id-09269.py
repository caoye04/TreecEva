def analyze_pattern(sequence):
    """Irrelevant helper that analyzes string patterns but is never called with meaningful data"""
    counts = {}
    for char in sequence:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + (1 if char.isupper() else -1)
    return sum(counts.values())

# Distractor variables - unused in final computation
temp_offset = 31415
scaling_factor = 0.987
buffer_cache = [0] * 100

# Decoy function - looks important but unused
def legacy_calibrate(x):
    return (x * 2 + 1) % 97

# Real data structures
weights = {'A': 3, 'B': -2, 'C': 5, 'D': 1}
data = [
    {'type': 'A', 'value': 12, 'meta': 'xyz'},
    {'type': 'B', 'value': 8, 'meta': 'abc'},
    {'type': 'C', 'value': 5, 'meta': 'xyz'},
    {'type': 'A', 'value': 15, 'meta': 'def'},
    {'type': 'D', 'value': 20, 'meta': 'xyz'}
]

# Dead code path - simulated fallback
recovery_mode = False
if recovery_mode:
    default_weights = {k: 1 for k in weights}
    result_fallback = sum(d['value'] for d in data)

# Linear search with conditional expression - relevant logic
filtered_data = [d for d in data if d['meta'].startswith('x')]

# Bit manipulation red herring
obfuscation_key = 241
scrambled = obfuscation_key ^ 17 ^ 17  # Cancels out

# Dictionary aggregation - core logic hidden among distractions
def process_results(entries, weight_map):
    total = 0
    for entry in entries:
        key = entry['type']
        val = entry['value']
        # Conditional expression based on value properties
        modifier = 2 if val > 10 else 1
        if key in weight_map:
            contribution = val * weight_map[key] * modifier
            total += contribution
    
    # String method used in non-essential cleanup (but looks like it affects logic)
    tag_summary = ''.join(sorted(set(d['meta'][0] for d in entries)))
    bonus = 10 if 'x' in tag_summary.lower() else 0
    
    # Final adjustment - only this matters
    return total + bonus

# Misleading intermediate calculations
count_analysis = len(data) * temp_offset // 1000  # Dead end
consistency_check = all(d['value'] > 0 for d in data)  # True but unused

# Key execution point
final_score = process_results(data, weights)

# Output requirement
print(f"Target result: {final_score}")