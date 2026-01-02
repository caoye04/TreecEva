from itertools import combinations

def analyze_trends(data, threshold):
    trends = []
    for i in range(2, len(data) + 1):
        for subset in combinations(data, i):
            if sum(subset) / len(subset) > threshold:
                trends.append(subset)
    return trends

# Irrelevant function - red herring
def compute_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

# Decoy data structures
placeholder_data = [3, 7, 1, 9, 4]
dummy_metrics = {'a': 10, 'b': 20, 'c': 30}
shadow_config = {k: v * 2 for k, v in dummy_metrics.items()}

baseline = 5.5
raw_input = [6, 8, 4, 7, 5, 9]

# Misleading intermediate calculation
aggregated = sum(x ** 2 for x in raw_input if x > 5) // 3

# Unused transformation path
transformed = [x + 2 for x in raw_input]
filtered = list(filter(lambda x: x < 8, transformed))

# Core logic buried among distractions
metrics = {
    'peak': max(raw_input),
    'span': len([x for x in raw_input if x >= baseline]),
    'density': len(list(combinations([x for x in raw_input if x > 6], 2))),
    'stability': sum(1 for i in range(1, len(raw_input)) if abs(raw_input[i] - raw_input[i-1]) <= 2)
}

# Another decoy operation
snapshot = set(raw_input)
cross_set = snapshot & {4, 5, 6, 7}
side_result = len(cross_set) * 11

# Real evaluation logic
status_flags = {
    'high_peak': metrics['peak'] > 8,
    'adequate_span': metrics['span'] >= 4,
    'sufficient_density': metrics['density'] >= 3,
    'stable_sequence': metrics['stability'] >= 2
}

# Heavily masked scoring logic
flag_count = sum(status_flags.values())
penalty = 0
if metrics['peak'] == max(dummy_metrics.values()):
    penalty += 5  # Dead condition - never reached

if len(raw_input) % 2 == 0 and min(raw_input) < 5:
    penalty -= 1

# Critical execution point
final_score = flag_count * 17 - penalty + (metrics['span'] if status_flags['adequate_span'] else 0)

# Redundant print (not the target)
dummy_output = compute_variance(placeholder_data)

# Target result output
print(f"Result: {final_score}")