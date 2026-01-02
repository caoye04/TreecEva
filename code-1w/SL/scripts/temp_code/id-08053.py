def analyze_efficiency(values):
    weighted_sum = sum(x * (i + 1) for i, x in enumerate(values))
    norm_factor = max(values) if values else 1
    return weighted_sum / norm_factor if norm_factor != 0 else 0

productivity = [85, 90, 78, 92, 88]
risk_levels = [3, 5, 2, 6, 4]

# Irrelevant computation - distractor
temporal_weights = list(map(lambda x: x ** 0.5, risk_levels))
baseline = sum(temporal_weights) / len(temporal_weights)

# Semi-relevant transformation
adjusted_productivity = [val - 5 for val in productivity if val > 80]

# Dummy state tracking
state_log = []
for idx, val in enumerate(adjusted_productivity):
    state_log.append(f'Step {idx}: {val}')

# Misleading aggregation
phantom_metric = 0
for r in risk_levels:
    if r % 2 == 0:
        phantom_metric += r * 1.5
    else:
        continue  # Dead code branch

# Core logic begins
risk_factor = sum(r ** 2 for r in risk_levels) / 100

# Another distraction: character counting in dummy labels
labels = ['A', 'B', 'C', 'D', 'E']
char_count = sum(len(label) for label in labels)
useless_offset = char_count * 0.1

# Simple sorting used as preprocessing
sorted_productivity = sorted(productivity, reverse=True)

def evaluate_performance(efficiency_list, penalty):
    base = sum(efficiency_list) / len(efficiency_list)
    adjustment = analyze_efficiency(efficiency_list)
    return int(base - penalty + adjustment)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

print(f'Result: {final_score}')