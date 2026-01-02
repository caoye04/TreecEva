from collections import defaultdict, Counter
import math

# Simulated sensor data stream (irrelevant in part)
sensor_readings = [145, 178, 201, 145, 312, 178, 145, 401, 312, 201]

# Irrelevant frequency analysis (distractor)
reading_frequency = Counter(sensor_readings)
unique_readings = len(reading_frequency)
most_common_reading = reading_frequency.most_common(1)[0][1]

# Core data for processing
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Decoy transformation (dead path)
decoys = [x ** 2 + 2 * x + 1 for x in data_stream if x % 2 == 0]
shadow_value = sum(decoys) // (len(decoys) + 1) if decoys else 0

# Threshold map with misleading keys
threshold_map = defaultdict(lambda: 10)
for i in range(1, 8):
    if i % 3 == 0:
        threshold_map[i] = int(math.log(i * 5 + 1, 2))
    elif i % 2 == 1:
        threshold_map[i] = i * 2 + (i % 4)
    else:
        threshold_map[i] = 15

# Unused but plausible-looking normalization (red herring)
normalized_stream = []
scaling_factor = max(data_stream) / 10.0
for val in data_stream:
    temp_scaled = val / scaling_factor
    if temp_scaled > 5:
        normalized_stream.append(round(temp_scaled, 2))

# Real signal extraction via sliding window
aggregated_data = []
window_size = 3
for i in range(len(data_stream) - window_size + 1):
    window = data_stream[i:i + window_size]
    avg = sum(window) / len(window)
    var = sum((x - avg) ** 2 for x in window) / len(window)
    aggregated_data.append(int(avg + var))

# Secondary irrelevant counter (distraction)
segment_stats = Counter()
for seg in [data_stream[j:j+4] for j in range(0, len(data_stream), 4)]:
    segment_stats[len(set(seg))] += 1

# Auxiliary function that looks important but is unused
def deprecated_analysis(seq):
    return sum(a * b for a, b in zip(seq, seq[1:]))

# Main analysis logic
lookup_weights = {k: threshold_map[k] for k in range(1, 8)}

# Complex conditional transformation
transformed_signals = []
for idx, val in enumerate(aggregated_data):
    base_shift = lookup_weights.get(idx % 7 + 1, 5)
    if val > 8:
        transformed_signals.append(val - base_shift)
    elif val < 5:
        transformed_signals.append(val + base_shift // 2)
    else:
        transformed_signals.append(val)

# Masking operation with bit manipulation (partially relevant)
masked_values = []
for t_val in transformed_signals:
    binary_mask = (1 << 3) - 1  # mask to last 3 bits
    masked = t_val & binary_mask
    if masked < 4:
        masked = masked ^ 5  # XOR flip
    masked_values.append(masked)

# Final aggregation before diagnostic
summary_score = sum(masked_values)
penalty = 0
for k, v in threshold_map.items():
    if v > 10 and k % 2 == 0:
        penalty += v // 3

interim_result = summary_score - penalty

# Diagnostic function using multiple concepts
def analyze_pattern(data_list, thresholds):
    count_high = 0
    running_total = 0
    for i, item in enumerate(data_list):
        ref_threshold = thresholds.get(i % len(thresholds), 7)
        if item > ref_threshold:
            count_high += 1
            running_total += item * (i + 1)  # position-weighted
        elif item == ref_threshold:
            running_total += 5
    # Complex fallback logic (mostly not triggered)
    if count_high == 0:
        return int(math.sqrt(running_total)) + 100
    composite_index = running_total // (count_high if count_high else 1)
    adjustment = len([x for x in data_list if x in thresholds.values()])
    return composite_index - adjustment + len(data_list)

# Critical statement
final_diagnostic = analyze_pattern(aggregated_data, threshold_map)

print(f"Result: {final_diagnostic}")