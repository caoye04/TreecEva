from itertools import combinations

# Simulate sensor data acquisition and processing with noise filtering
raw_signals = [102, 95, 130, 45, 88, 110, 65, 140]
noise_floor = 50
signal_baseline = 100

detected_peaks = []
filtered_data = []
peak_metadata = {}

# Step 1: Identify potential peaks above baseline + noise floor
for val in raw_signals:
    if val > signal_baseline + noise_floor * 0.5:
        detected_peaks.append(val)
        if val > 120:
            peak_metadata[val] = 'high_magnitude'
        elif val > 100:
            peak_metadata[val] = 'moderate_magnitude'

# Misleading secondary pass - appears important but only adds noise
expanded_pairs = list(combinations(detected_peaks, 2))
spurious_score = 0
for a, b in expanded_pairs:
    spurious_score += (a - b) ** 2  # Irrelevant computation

# Normalize detected peaks (distractor normalization)
normalized_peaks = [round(p / 1.5) for p in detected_peaks]

# Real filtering: only values above dynamic adaptive threshold
adaptive_offset = len(expanded_pairs) % 25  # Seemingly complex, actually bounded
threshold_map = {v: v > (signal_baseline + adaptive_offset) for v in detected_peaks}

for val in detected_peaks:
    if threshold_map[val]:
        filtered_data.append(val)

# Auxiliary diagnostic log (dead code path, never used)
diagnostic_log = []
if len(filtered_data) > 2:
    diagnostic_log.append('MULTIPLE_SIGNALS_DETECTED')
elif len(filtered_data) == 1:
    diagnostic_log.append('SINGLE_DOMINANT_SIGNAL')
else:
    diagnostic_log.append('NO_CLEAR_SIGNAL')

# Core processing function (depends on prior state)
def process_signals(data, thresholds):
    aggregate = 0
    contribution_weights = {}
    
    for val in data:
        # Weighting logic that depends on threshold classification
        weight = 1.5 if thresholds[val] else 1.0
        contribution_weights[val] = weight
        aggregate += val * weight
    
    # Secondary adjustment based on count (actual impact)
    if len(data) >= 3:
        aggregate *= 0.9  # Stability correction factor
    elif len(data) == 0:
        aggregate = 10  # Default fallback
        
    return int(aggregate)

# Execute main logic step
final_output = process_signals(filtered_data, threshold_map)

# Additional irrelevant transformation
inverted_map = {v: k for k, v in threshold_map.items()}
sorted_inverted = sorted(inverted_map.items())

# Print final result as required
print(f"Result: {final_output}")