def analyze_component(x, threshold=5):
    if x < threshold:
        return (x ** 2) + 3
    else:
        return (x // 2) - 1

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum(d * 0.5 for d in data if d > 3)

# Distractor variables
temp_log = [1, 3, 5, 7, 9]
offset_cache = {'a': 10, 'b': 20}
scaling_factor = 1.5  # Unused in final calculation

# Real data processing chain
def evaluate_stages(phases):
    results = []
    for i, phase in enumerate(phases):
        if i % 2 == 0:
            processed = analyze_component(phase + i)
        else:
            processed = analyze_component(phase * 2)
        results.append(processed)
    return results

# Bit manipulation red herring
def decoy_encrypt(val):
    return val ^ 0xFF + 10

# Another irrelevant transformation
class FilterPipeline:
    def __init__(self, values):
        self.values = values

    def apply_mask(self):
        return [v & 0xF for v in self.values]  # Never instantiated

# Core logic with set operations and enumeration
feedback_levels = [4, 6, 2, 8, 5]
level_flags = set()
for idx, level in enumerate(feedback_levels):
    if level >= 5:
        level_flags.add(f"high_{idx}")
    else:
        level_flags.add(f"low_{idx}")

# Misleading intermediate aggregation
decoy_aggregate = 0
for val in feedback_levels:
    decoy_aggregate += decoy_encrypt(val)

# Real aggregation using zip and conditional logic
def aggregate_performance(ratings):
    base_scores = evaluate_stages(ratings)
    modifiers = [1, -1, 2, -2, 0]
    adjusted = []
    for score, mod in zip(base_scores, modifiers):
        adjusted.append(score + mod)
    
    # Additional filtering via set operation
    valid_indices = {i for i, r in enumerate(ratings) if r != 5}
    filtered = []
    for i, adj in enumerate(adjusted):
        if i in valid_indices:
            filtered.append(adj)
    
    # Final computation
    raw_total = sum(filtered)
    
    # Secondary adjustment based on flag count
    flag_count = len(level_flags)
    if flag_count > 3:
        raw_total -= 2
    
    # Introduce a bitwise distraction (irrelevant)
    masked = raw_total & 0xFFFF
    inverted = ~raw_total
    
    # But only this matters:
    final_shift = raw_total >> 1
    return final_shift

# Execution point of interest
final_score = aggregate_performance(feedback_levels)
Result: {final_score}