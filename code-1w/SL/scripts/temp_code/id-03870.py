import itertools

# Simulated sensor data processing with embedded logic chain
def preprocess_raw(signal_chunk):
    if not signal_chunk:
        return [0]
    smoothed = [sum(signal_chunk[i:i+3]) / len(signal_chunk[i:i+3]) for i in range(len(signal_chunk))]
    normalized = [val / max(smoothed) * 100 for val in smoothed]
    return [round(x, 2) for x in normalized]

# Irrelevant transformation - red herring
def frequency_shift(data, factor=1.5):
    return [d * factor for d in data if d > 50]

# Unused decoy function
def compress_data(seq):
    return [seq[i] for i in range(0, len(seq), 2)]

# Core analysis pipeline
processed_segments = []
raw_signals = [
    [12, 15, 18, 22, 19, 24, 28],
    [30, 28, 35, 40, 38, 33, 45],
    [50, 55, 53, 60, 65, 63, 70]
]

for segment in raw_signals:
    cleaned = preprocess_raw(segment)
    filtered_peaks = [x for x in cleaned if x > 75]  # Only some segments trigger this
    if len(filtered_peaks) >= 1:
        processed_segments.append(cleaned[::2])  # Take every other point
    else:
        processed_segments.append(cleaned[:3])   # First three only

# Dead code path - never executed due to data characteristics
redundant_buffer = []
if any(len(seg) > 10 for seg in processed_segments):
    redundant_buffer = list(itertools.chain.from_iterable(processed_segments))

# Distractor: complex but unused set operation
unique_values = set()
for s in processed_segments:
    unique_values.update(set(map(int, s)))
duplicate_check = unique_values & {x + 1 for x in unique_values}
phantom_mask = unique_values ^ {x * 2 for x in duplicate_check if x < 100}

# Real computation begins here — non-obvious due to noise above
effective_amplitudes = []
for seg in processed_segments:
    base_ref = seg[0]
    for val in seg[1:]:
        if val > base_ref * 1.1:
            effective_amplitudes.append(val - base_ref)
            break
    else:
        effective_amplitudes.append(base_ref * 0.1)

# Secondary processing with conditional mutation
calibration_log = []
amplitude_snapshot = effective_amplitudes.copy()

for i, amp in enumerate(effective_amplitudes):
    if i % 2 == 0:
        calibrated = round(amp * 0.85, 2)
        calibration_log.append(f"C{i}:{calibrated}")
        effective_amplitudes[i] = calibrated
    else:
        adjusted = amp + 2.5
        effective_amplitudes[i] = round(adjusted, 2)

# Tertiary transformation using itertools (required feature)
shifted_pairs = list(itertools.pairwise(effective_amplitudes))
gradient_series = [b - a for a, b in shifted_pairs if b > a]

# Logical evaluation branch
valid_gradients = []
for g in gradient_series:
    if g > 5.0:
        valid_gradients.append(g)
        if len(valid_gradients) > 1:
            break
else:
    valid_gradients.append(1.75)  # Fallback value added once

# Final aggregation through indirect routing
aggregate_flag = len(valid_gradients) == 1 and valid_gradients[0] == 1.75
temp_offset = sum(valid_gradients)

# Critical execution point
intermediate_fuse = temp_offset * 17

# Function that appears complex but has limited side effects
def analyze_signal(segments):
    flat_data = list(itertools.chain(*segments))
    mean_level = sum(flat_data) / len(flat_data)
    
    # Irrelevant categorization
    categories = {}
    for v in flat_data:
        cat = 'high' if v > 90 else 'mid' if v > 50 else 'low'
        categories[cat] = categories.get(cat, 0) + 1
    
    # Misleading entropy-like calculation
    import math
    total = sum(categories.values())
    entropy = sum(-(count/total) * math.log2(count/total) for count in categories.values())
    
    # Actual relevant logic: count how many segments had internal drop > 10%
    decay_events = 0
    for seg in segments:
        for i in range(1, len(seg)):
            if seg[i] < seg[i-1] * 0.9:
                decay_events += 1
                break
    
    # This is the real answer contributor
    signal_quality = len(segments) * decay_events * 100 + int(intermediate_fuse)
    
    # Dead assignment
    debug_trace = [f"Q{x}" for x in range(signal_quality % 7)]
    
    return signal_quality

# Execution point where answer is determined
final_diagnostic = analyze_signal(processed_segments)
print(f"Target result: {final_diagnostic}")