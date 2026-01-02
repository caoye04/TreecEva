from collections import defaultdict
import itertools

# Simulated sensor data processing system for a distributed IoT network
node_signals = [78, 85, 92, 64, 73, 88, 95, 61, 77, 83]
signal_weights = [0.9, 1.1, 1.0, 0.8, 1.2, 1.0, 0.95, 1.05, 1.15, 0.85]

# Irrelevant calibration constants (distractor)
calibration_offset = 3.14159
temp_buffer = [0] * 15
buffer_index = 0
for i in range(len(temp_buffer)):
    temp_buffer[i] = (i * calibration_offset) % 7

# Weighted signal aggregation (relevant)
weighted_sum = 0.0
for i in range(len(node_signals)):
    weighted_sum += node_signals[i] * signal_weights[i]

average_signal = weighted_sum / len(node_signals)

# Noise floor estimation (partially relevant, partially misleading)
noise_floor = sum([x < 75 for x in node_signals]) * 2.5
adjusted_signal = average_signal - noise_floor if noise_floor > 10 else average_signal + 2.5

# Decoy function: looks important but unused
def compute_health_score_v1(data):
    return sum(x ** 0.5 for x in data if x > 70) / len(data)

# Another decoy: complex but irrelevant transformation
transformation_matrix = [[(i*j) % 3 for j in range(4)] for i in range(4)]
mapped_diagnostics = []
for row in transformation_matrix:
    mapped_diagnostics.append([x * adjusted_signal / 4 for x in row])

# Real processing begins: construct health vector based on thresholds
health_vector = []
for val in node_signals:
    if val >= 90:
        health_vector.append(3)
    elif val >= 80:
        health_vector.append(2)
    elif val >= 70:
        health_vector.append(1)
    else:
        health_vector.append(0)

# Threshold configuration map (used later)
threshold_map = defaultdict(lambda: 1.0)
threshold_map.update({
    'critical': 2.5,
    'elevated': 1.8,
    'normal': 1.0,
    'baseline': 0.0  # Unused key (red herring)
})

# Simulate historical moving averages (dead path)
historical_avgs = []
for window in range(3, 6):
    for start in range(len(node_signals) - window + 1):
        window_avg = sum(node_signals[start:start+window]) / window
        historical_avgs.append(window_avg)

# Auxiliary diagnostic flags (some used, some not)
event_log = []
trigger_count = 0
for idx, sig in enumerate(node_signals):
    if sig > 90 and idx % 2 == 0:
        event_log.append(f"HIGH_{idx}")
        trigger_count += 1

# Unused symbolic mapping (distractor)
symbolic_codes = {0: 'OK', 1: 'WARN', 2: 'ELEV', 3: 'CRIT'}
code_translations = [symbolic_codes[x] for x in health_vector]

# Core logic: multi-stage metric processor
valid_states = [x for x in health_vector if x >= 1]
state_frequency = defaultdict(int)
for state in valid_states:
    state_frequency[state] += 1

# Composite scoring with conditional logic
base_score = 0
for state, freq in state_frequency.items():
    if state == 3:
        base_score += freq * threshold_map['critical']
    elif state == 2:
        base_score += freq * threshold_map['elevated']
    else:
        base_score += freq * threshold_map['normal']

# Adjustment factor using itertools cycle (meaningful use)
cycle_weights = list(itertools.cycle([0.9, 1.1, 1.0]))
adjustment = 0
for i, state in enumerate(valid_states):
    adjustment += state * cycle_weights[i % 3]

# Final normalization with conditional expression
size_factor = len(valid_states) if len(valid_states) > 0 else 1
normalized_adjustment = adjustment / size_factor

# Critical execution point
final_diagnostic = process_metrics(health_vector, threshold_map)

# Top-level function defined at end to obscure relevance
def process_metrics(states, thresholds):
    # Re-calculate frequency (redundant but obscures flow)
    count_3 = states.count(3)
    count_2 = states.count(2)
    count_1 = states.count(1)
    
    # Apply threshold multipliers
    score = 0
    score += count_3 * thresholds['critical']
    score += count_2 * thresholds['elevated']
    score += count_1 * thresholds['normal']
    
    # Secondary adjustment based on pattern continuity
    consecutive_high = 0
    max_consecutive = 0
    for s in states:
        if s >= 2:
            consecutive_high += 1
        else:
            max_consecutive = max(max_consecutive, consecutive_high)
            consecutive_high = 0
    max_consecutive = max(max_consecutive, consecutive_high)
    
    if max_consecutive >= 3:
        score *= 1.25
    elif max_consecutive == 0:
        score *= 0.8
    
    # Final clamp and rounding
    score = round(score, 4)
    
    # Dead code branch (never reached due to return)
    if score < 0:
        submit_alert('NEGATIVE_SCORE')
        return None
        
    return score

# Print result as required
Result: {final_diagnostic}