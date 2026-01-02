from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (real processing)
sensor_feeds = [
    [1.2, 1.5, 1.3, 2.1, 1.8],
    [0.9, 1.1, 1.0, 1.4, 1.2],
    [2.3, 2.5, 2.4, 2.6, 2.7]
]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_OFFSET_X = -0.05
REFERENCE_BASELINE = 1.6
MAX_TOLERANCE_BAND = 0.4

# Misleading intermediate metrics (red herring)
stale_metrics = {
    'avg_noise': 0.33,
    'signal_drift': 0.07,
    'ghost_readings': 2
}

# Unused fallback algorithm (dead code path)
def legacy_analysis(data):
    return sum(x ** 0.5 for x in data if x > 0) / len(data)

# Fake health scoring (decoy function)
def compute_health_score(readings):
    weighted = [r * 0.85 for r in readings]
    return sum(w for w in weighted if w > 1.0)

# Real data preprocessing
filtered_streams = []
for feed in sensor_feeds:
    cleaned = [x for x in feed if abs(x - REFERENCE_BASELINE) <= MAX_TOLERANCE_BAND * 2]
    filtered_streams.append(cleaned)

# Aggregation with slicing and transformation
aggregated = []
for i, stream in enumerate(filtered_streams):
    segment = stream[1:-1] if len(stream) > 2 else stream
    aggregated.extend(segment)

# Threshold configuration (used later)
threshold_map = defaultdict(lambda: 1.5)
threshold_map.update({
    'critical': 2.2,
    'warning': 1.6,
    'info': 1.1
})

# Auxiliary counters (mixed use)
event_counter = Counter()
for val in aggregated:
    if val >= threshold_map['warning']:
        event_counter['high'] += 1
    elif val >= threshold_map['info']:
        event_counter['medium'] += 1
    else:
        event_counter['low'] += 1

# Phantom normalization (irrelevant)
normalized_aggregated = list(map(lambda x: x / (x + 0.1), aggregated))

# Spurious signal fusion (unused result)
fused_signal = 0.0
for idx, val in enumerate(normalized_aggregated):
    fused_signal += val * math.sin(idx)

# Real diagnostic logic begins here
def analyze_trend(values, thresh):
    above = len([v for v in values if v > thresh])
    total = len(values)
    return above / total if total else 0

# Secondary helper (actually used)
def extract_diagnostic(patterns):
    if not patterns:
        return 0.0
    peak = max(patterns)
    base = min(patterns)
    return round((peak - base) * 100, 4)

# Main processing function
def process_metrics(data_input, limits):
    # Step 1: Apply dynamic filtering
    windowed = data_input[::2]  # slicing every other element

    # Step 2: Identify critical breaches
    critical_level = limits['critical']
    breaches = [pt for pt in windowed if pt > critical_level]

    # Step 3: Compute trend ratio
    trend_ratio = analyze_trend(windowed, limits['warning'])

    # Step 4: Extract amplitude metric
    amplitude_score = extract_diagnostic(windowed)

    # Step 5: Combine into composite index
    raw_index = len(breaches) * 1000 + int(trend_ratio * 100)

    # Step 6: Apply corrective offset (simulated calibration)
    final_adjustment = raw_index + int(amplitude_score)

    # Step 7: Post-process with safety cap
    capped_result = min(final_adjustment, 99999)

    # Step 8: Final diagnostic output
    return capped_result + 17  # deterministic offset

# Trigger point: execute main logic
health_data = aggregated
final_diagnostic = process_metrics(health_data, threshold_map)

# Print required result
print(f"Target result: {final_diagnostic}")