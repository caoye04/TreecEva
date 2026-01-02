from collections import defaultdict, Counter
import itertools

# Simulate user interaction sequences from three different app modules
data_stream = [
    ('module_a', 'click'), ('module_b', 'hover'), ('module_a', 'scroll'),
    ('module_c', 'click'), ('module_b', 'click'), ('module_a', 'click'),
    ('module_c', 'hover'), ('module_c', 'click'), ('module_b', 'scroll')
]

# Process raw event data
raw_stats = defaultdict(int)
event_types = set()
for module, event in data_stream:
    raw_stats[(module, event)] += 1
    event_types.add(event)

# Derive basic metrics (some used later, some not)
total_interactions = sum(raw_stats.values())
unique_events = len(event_types)
module_popularity = defaultdict(int)
for (module, _), count in raw_stats.items():
    module_popularity[module] += count

# Misleading distraction: compute unused entropy-like metric
import math
total = total_interactions
entropy = 0.0
for count in raw_stats.values():
    p = count / total
    if p > 0:
        entropy -= p * math.log2(p)  # Not used in final result

# Focus on click events per module for engagement scoring
click_data = {module: raw_stats.get((module, 'click'), 0) for module in module_popularity}

# Apply time decay factor (simulated: older events weighted less)
decay_factors = {'module_a': 0.9, 'module_b': 0.95, 'module_c': 0.85}
weighted_clicks = defaultdict(float)
for module, clicks in click_data.items():
    weighted_clicks[module] = clicks * decay_factors[module]

# Normalize weighted clicks to [0,10] scale based on max
max_weighted = max(weighted_clicks.values())
normalized_scores = {mod: (val / max_weighted) * 10 for mod, val in weighted_clicks.items()}

# Aggregate using harmonic mean for balanced score (penalizes extreme lows)
def harmonic_mean(vals):
    if 0 in vals:
        return 0.0
    n = len(vals)
    return n / sum(1/v for v in vals)

aggregated_normalization = harmonic_mean(normalized_scores.values())

# Prepare processed data structure
processed_data = {
    'modules': list(normalized_scores.keys()),
    'base_clicks': click_data,
    'normalized': normalized_scores,
    'summary_metric': aggregated_normalization,
    'size_hint': len(data_stream) % 7  # Red herring field
}

# Secondary distraction: generate all pairs of modules (not used)
module_pairs = list(itertools.combinations(processed_data['modules'], 2))
pair_analysis = {}
for a, b in module_pairs:
    diff = abs(normalized_scores[a] - normalized_scores[b])
    pair_analysis[(a, b)] = round(diff, 2)

# Real computation path begins
baseline_offset = 3.5

# Simulate multi-phase calculation with irrelevant intermediate steps
temp_shift = 0.0
for module in processed_data['modules']:
    temp_shift += processed_data['normalized'][module] * 0.01  # negligible effect

# Final score depends only on summary_metric and baseline
intermediate_tweak = processed_data['summary_metric'] + temp_shift  # minor noise
final_score = int(baseline_offset + intermediate_tweak)  # actual answer

# Print result as required
print(f"Result: {final_score}")