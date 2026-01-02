from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant pattern counting (distractor)
    up_sequences = 0
    for t in trend:
        if t == 1:
            up_sequences += 1

    # Real logic: count oscillations
    oscillations = 0
    for i in range(1, len(trend)):
        if trend[i] != 0 and trend[i] != trend[i-1]:
            oscillations += 1

    return oscillations

# Simulated sensor readings
data_stream = [23.1, 24.5, 23.8, 25.2, 24.9, 26.1, 25.7, 27.0]

# Preprocess with irrelevant transformations
smoothed = [round((data_stream[i] + data_stream[i+1]) / 2, 1) for i in range(len(data_stream)-1)]
smoothed.append(data_stream[-1])  # Align lengths

# Generate all possible triplets (computationally heavy but partially irrelevant)
triplet_modes = []
for combo in combinations(smoothed, 3):
    mode_val = max(set(combo), key=combo.count) if len(set(combo)) < 3 else combo[1]
    triplet_modes.append(mode_val)

# Compute statistical summaries (some irrelevant)
mean_level = sum(data_stream) / len(data_stream)
variance_proxy = sum((x - mean_level) ** 2 for x in data_stream) / len(data_stream)
peak_deviation = max(abs(x - mean_level) for x in data_stream)

# Hidden state tracker (semi-relevant)
current_state = 0
state_log = []
for val in data_stream:
    if val > mean_level + 0.5:
        current_state = 1
    elif val < mean_level - 0.5:
        current_state = -1
    else:
        current_state = 0
    state_log.append(current_state)

# Core logic: evaluate signal stability
signal_changes = 0
for i in range(1, len(state_log)):
    if state_log[i] != state_log[i-1]:
        signal_changes += 1

# Secondary analysis on raw trend
raw_trend = [1 if data_stream[i] > data_stream[i-1] else -1 for i in range(1, len(data_stream))]
consistent_segments = 1
for i in range(1, len(raw_trend)):
    if raw_trend[i] == raw_trend[i-1]:
        consistent_segments += 1

# Final computation with multiple inputs (only some are used)
def compute_aggregate(raw, smooth, changes, segments, oscillations):
    baseline = sum(raw) / len(raw)
    noise_estimate = len([x for x in zip(raw, smooth) if abs(x[0]-x[1]) > 0.5])
    # Actual determining factors:
    score_component_1 = changes * 2
    score_component_2 = segments // 3
    oscillation_weight = oscillations * 1.5
    
    # Distractor calculation
    phantom_score = noise_estimate * 0.7
    temp_adjustment = len(smooth) - len(raw)
    
    # Final formula (only uses specific components)
    final_score = score_component_1 + score_component_2 + oscillation_weight
    
    # Dead code branch (never executed but looks relevant)
    if temp_adjustment > 100:
        final_score *= 0.9
        
    return int(final_score)

# Execute main evaluation
oscillations_detected = analyze_pattern(data_stream)
final_score = compute_aggregate(
    raw=data_stream,
    smooth=smoothed,
    changes=signal_changes,
    segments=consistent_segments,
    oscillations=oscillations_detected
)

print(f"Result: {final_score}")