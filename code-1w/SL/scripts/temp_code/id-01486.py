from collections import defaultdict, Counter

# Simulated system telemetry data
timing_data = [1.2, 0.8, 1.5, 0.7, 1.3, 0.9, 1.6, 0.6, 1.1, 1.0]
raw_flags = [True, False, True, True, False, True, False, True, True, False]

# Irrelevant auxiliary data (distractor)
event_log = ['start', 'pause', 'resume', 'error', 'retry', 'success', 'fail', 'timeout', 'reset', 'done']
metadata_map = {i: {'type': 'event', 'active': False} for i in range(10)}

# Misleading intermediate transformation (dead path)
processed_log = []
for idx, entry in enumerate(event_log):
    if 'e' in entry:
        processed_log.append(entry.upper())

# Decoy function that is never called
def analyze_performance_legacy(data):
    return sum(x ** 0.5 for x in data) / len(data)

# Unused statistical variables (red herring)
avg_latency = sum(timing_data) / len(timing_data)
std_deviation = (sum((x - avg_latency) ** 2 for x in timing_data) / len(timing_data)) ** 0.5
outlier_threshold = avg_latency + 1.5 * std_deviation

# Bit manipulation decoy (irrelevant)
flag_int = sum(1 << i for i, val in enumerate(raw_flags[:8]) if val)
scrambled = flag_int ^ 0b10101010
shifted = (scrambled << 3) & 0b11111111

# Destructuring with partial use (partial distractor)
first, second, *rest = timing_data
offset_correction = first * second  # Used only in unused calculation

# Construct flag tuples with index (partially relevant)
indexed_flags = [(i, raw_flags[i]) for i in range(len(raw_flags))]

# Filter valid intervals based on flags (relevant logic start)
active_intervals = [timing_data[i] for i in range(len(timing_data)) if raw_flags[i]]

# Simulate multi-step data refinement (nested logic)
refined_data = []
for val in active_intervals:
    if val < 1.4:
        refined_data.append(val * 1.1)
    else:
        adjusted = val * 0.95
        if adjusted > 1.0:
            refined_data.append(adjusted)

# Apply slicing to exclude potential outliers (relevant)
sorted_refined = sorted(refined_data)
trimmed = sorted_refined[1:-1] if len(sorted_refined) > 4 else sorted_refined

# Count frequency of rounded values (collections.Counter usage)
freq = Counter(int(round(x, 0)) for x in trimmed)

def aggregate_metrics(data_slice, flag_list):
    # Nested dictionary for metric tracking (defaultdict usage)
    metrics = defaultdict(lambda: defaultdict(float))
    
    temp_buffer = []
    for x in data_slice:
        if x > 0.9:
            temp_buffer.append(x ** 2)
        else:
            temp_buffer.append(x ** 0.5)
    
    # Complex conditional accumulation
    for i, val in enumerate(temp_buffer):
        key = 'high' if val > 1.0 else 'low'
        metrics[key]['sum'] += val
        metrics[key]['count'] += 1
        if i % 2 == 0:
            metrics[key]['squared_sum'] += val ** 2
    
    # Compute composite diagnostic score
    high_sum = metrics['high']['sum']
    low_sum = metrics['low']['sum']
    high_count = metrics['high']['count']
    
    # Final diagnostic formula (key computation)
    if high_count > 0:
        ratio_component = high_sum / (low_sum + 1e-8)
        square_avg = (metrics['high']['squared_sum'] / high_count) ** 0.5
        diagnostic = (ratio_component * 12.5) + (square_avg * 3.7)
    else:
        diagnostic = low_sum * 5.2
    
    # Normalize using bit-derived constant (misleading but deterministic)
    normalization_factor = ((shifted & 0b111) or 1)  # Ensures non-zero
    return int(diagnostic * 100) / normalization_factor

# Secondary filtering based on index conditions (adds nesting depth)
filtered_pairs = []
for i, flag in indexed_flags:
    if i % 2 == 0 and flag:
        filtered_pairs.append((i, timing_data[i]))

# Extract subset for final processing
subset_indices = [p[0] for p in filtered_pairs]
subset_data = [timing_data[i] for i in subset_indices]

# Flags are reconstructed in a roundabout way (obfuscation)
reconstructed_flags = [any(idx == i for i, _ in filtered_pairs) for idx in range(len(timing_data))]

# Critical statement
final_diagnostic = aggregate_metrics(subset_data, reconstructed_flags)

print(f"Result: {final_diagnostic}")