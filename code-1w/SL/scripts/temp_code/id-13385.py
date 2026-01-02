from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(data):
    return sum([len(str(x)) for x in data if isinstance(x, int)])

# Misleading preprocessing block (distractor)
temp_offsets = [i ** 2 - 3 * i + 2 for i in range(5)]
offset_map = {i: temp_offsets[i] for i in range(len(temp_offsets))}

# Core data structures
metric_data = [
    {'name': 'latency', 'value': 45, 'weight': 0.3},
    {'name': 'throughput', 'value': 88, 'weight': 0.4},
    {'name': 'error_rate', 'value': 2, 'weight': 0.3}
]

bonus_multiplier = 1.2
penalty_factor = 0.9  # Unused in final logic (red herring)

# Auxiliary tracking map (partially relevant)
event_log = ['start', 'process', 'validate', 'finalize']
log_counter = Counter(event_log)

# Decoy function with plausible but unused logic
def apply_penalty(score, factor):
    return score * factor if score > 60 else score * 0.7

# Complex transformation pipeline
processed = []
for entry in metric_data:
    raw = entry['value']
    weight = entry['weight']
    
    # Apply nonlinear scaling based on performance tier
    if raw >= 90:
        adjusted = raw * 1.1
    elif raw >= 75:
        adjusted = raw * 1.05
    elif raw >= 50:
        adjusted = raw * 0.95  # Small deduction for medium performers
    else:
        adjusted = raw * 0.8
    
    processed.append({'name': entry['name'], 'score': adjusted, 'w': weight})

# Secondary processing with list comprehension and filtering
filtered_scores = [p['score'] * p['w'] for p in processed if p['score'] > 40]

# Weighted aggregation
total_weighted = sum(filtered_scores)
base_performance = round(total_weighted, 3)

# Bit manipulation red herring
bit_mask = 0b101010
masked_result = base_performance ^ bit_mask  # Never used

# Conditional bonus logic with short-circuit evaluation
has_high_throughput = any(p['name'] == 'throughput' and p['score'] > 90 for p in processed)
is_latency_critical = processed[0]['score'] < 50

# Real bonus condition (non-obvious due to distractions)
enhanced_bonus = 1.1 if has_high_throughput or not is_latency_critical else 1.0

# Final calculation obscured by multiple similar variables
interim_score = base_performance * bonus_multiplier
final_score = interim_score * enhanced_bonus

# Additional decoy operations
audit_trail = defaultdict(list)
audit_trail['stages'].append('init')
audit_trail['stages'].append('score_finalized')

# Debug print that does not affect outcome
# print(f'Debug - masked result: {masked_result}')

Result: {final_score}