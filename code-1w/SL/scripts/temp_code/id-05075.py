import itertools

# Simulated sensor data with noise and metadata
data_stream = [18, 22, 19, 25, 30, 28, 20, 17, 23, 27]
noise_floor = 15
calibration_offset = 3
sample_timestamps = list(range(10))

# Irrelevant auxiliary variables (distractors)
baseline_readings = [x + calibration_offset for x in data_stream]
aggregated_stats = {'sum': sum(data_stream), 'max': max(data_stream), 'min': min(data_stream)}
status_flags = {i: 'OK' if x > noise_floor else 'LOW' for i, x in enumerate(data_stream)}

# Unused function - red herring
def compute_entropy(signal):
    from math import log
    counts = {}
    for x in signal:
        counts[x] = counts.get(x, 0) + 1
    total = len(signal)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Decoy transformation chain
temp_buffer = []
for val in data_stream:
    if val > 20:
        temp_buffer.append(val * 2)
    else:
        temp_buffer.append(val // 2)

# Actual relevant processing begins here
filtered_data = [x for x in data_stream if x > noise_floor + 2]
squared_deltas = [(x - noise_floor) ** 2 for x in filtered_data]

# Multiple assignment and tuple unpacking (relevant)
mean_shifted = sum(squared_deltas) / len(squared_deltas)
drift_coefficient, _ = divmod(mean_shifted, 5)

# Bit manipulation as part of diagnostic (relevant)
defect_mask = 0b101010
signature_key = defect_mask ^ int(mean_shifted % 64)

# Destructuring with itertools (relevant concept)
rolling_pairs = list(itertools.pairwise(filtered_data))
weighted_slopes = [b - a for a, b in rolling_pairs]

# Lambda-based transformation chain (required feature)
transform_fn = lambda x: x * drift_coefficient if x > 10 else x + signature_key
processed_data = [round(transform_fn(x)) for x in weighted_slopes]

# Conditional control flow with early exit pattern (relevant)
if len(processed_data) == 0:
    final_diagnostic = -1
    print(f'Result: {final_diagnostic}')
else:
    # Real computation path
    aggregate_score = sum(abs(x) for x in processed_data)
    
    # Redundant dictionary operations (distractor)
    stats_summary = {}
    for i, val in enumerate(processed_data):
        stats_summary[f'sample_{i}'] = {
            'raw': val,
            'squared': val ** 2,
            'flagged': val > 10
        }
    
    # Final analysis function (key logic)
    def analyze_signal(signal):
        base = sum(signal)
        # Complex conditional weighting
        adjustment = 0
        for x in signal:
            if x > 5:
                adjustment += 2
            elif x < 0:
                adjustment -= 1
        # Critical bitwise interaction
        adjustment = adjustment & 7  # limit to 3 bits
        return base + (adjustment * len(signal))
    
    final_diagnostic = analyze_signal(processed_data)
    
    # Dead code path - misleading
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic) << 1
    
    # Print required output
    print(f'Result: {final_diagnostic}')