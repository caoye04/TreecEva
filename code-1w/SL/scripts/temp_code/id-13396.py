from itertools import combinations, cycle

# Simulated sensor fusion system for autonomous drone navigation
base_signals = [0.87, 0.92, 0.65, 0.44, 0.91]
decoy_offsets = [0.13, -0.08, 0.22, -0.17, 0.09]

# Irrelevant transformation - red herring
shifted_decoys = [round(d + 0.05, 2) for d in decoy_offsets]
buffer_map = {i: round(1.0 / (1 + abs(d)), 3) for i, d in enumerate(decoy_offsets)}

# Fake calibration sequence (dead code path)
def calibrate_system(mode='safe'):
    if mode == 'aggressive':
        return [s * 1.15 for s in base_signals]
    else:
        return [s for s in base_signals]

# Unused but plausible signal processing
temp_amplitudes = []
for sig in base_signals:
    level = int(sig * 100)
    bin_factors = [level >> i & 1 for i in range(4)]
    weighted_sum = sum(f * (2**i) for i, f in enumerate(bin_factors))
    temp_amplitudes.append(weighted_sum)

# Real metric weights (only some are used)
metric_weights = {
    'precision': 0.35,
    'recall': 0.25,
    'latency_penalty': 0.15,
    'jitter_factor': 0.10,
    'redundancy_bonus': 0.15
}

# Mixed-quality outcome data with noise injection
raw_outcomes = [
    {'success': True,  'response_time': 120, 'errors': 0,  'phase': 'A'},
    {'success': False, 'response_time': 210, 'errors': 3,  'phase': 'B'},
    {'success': True,  'response_time': 95,  'errors': 1,  'phase': 'C'},
    {'success': True,  'response_time': 180, 'errors': 0,  'phase': 'D'}
]

# Distractor accumulator - looks important but unused later
cumulative_phase_score = 0
phase_cycle = cycle(['X', 'Y', 'Z'])
for _ in range(len(raw_outcomes)):
    next(phase_cycle)
    cumulative_phase_score += 1  # Misleading increment

# Complex truth evaluation with nested logic
valid_entries = []
penalty_adjustment = 0
for entry in raw_outcomes:
    is_accurate = entry['errors'] <= 1
    is_timely = entry['response_time'] < 200
    high_priority = entry['phase'] in ['A', 'C']
    
    # Multi-condition gate that seems to do something significant
    if is_accurate and (is_timely or high_priority):
        weight = 1.0
        if entry['errors'] == 0:
            weight *= 1.1
        if high_priority:
            weight *= 1.05
        entry['weight'] = round(weight, 2)
        valid_entries.append(entry)
    else:
        penalty_adjustment -= 5  # Minor red herring adjustment

# Real scoring logic hidden among distractions
partial_scores = []
for entry in valid_entries:
    base_score = 100 if entry['success'] else 60
    time_bonus = max(0, (150 - entry['response_time']) * 0.2)
    error_penalty = entry['errors'] * 10
    final_entry_score = base_score + time_bonus - error_penalty
    partial_scores.append(final_entry_score)

# Critical aggregation using only selected weights
active_weight_keys = ['precision', 'recall', 'redundancy_bonus']
combined_signal = sum(base_signals[i] * (i + 1) for i in range(0, len(base_signals), 2))
signal_mod = round(combined_signal % 1, 3)

# Real computation chain begins here
aggregate_precision = sum(partial_scores) / len(partial_scores) if partial_scores else 0
aggregate_recall = len([e for e in raw_outcomes if e['success']]) / len(raw_outcomes)

# Hidden combinatorics affecting bonus calculation
bonus_combinations = list(combinations([w for w in metric_weights.values() if w > 0.1], 2))
combination_factor = len(bonus_combinations) * 0.05

# Main performance formula
raw_performance = (
    aggregate_precision * metric_weights['precision'] + 
    aggregate_recall * metric_weights['recall'] + 
    combination_factor * metric_weights['redundancy_bonus']
)

# Final adjustment based on signal mod (subtle dependency)
if signal_mod > 0.5:
    raw_performance *= 1.05
else:
    raw_performance *= 0.98

# Key assignment point
final_score = round(raw_performance, 4)

# Print required output
print(f"Result: {final_score}")