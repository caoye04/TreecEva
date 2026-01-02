from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def analyze_sensor_readings(readings):
    cumulative_shift = 0
    transient_buffer = []
    mode_analysis = defaultdict(int)
    diagnostic_weight = 0.0
    entropy_tracker = []

    for reading in readings:
        # Irrelevant entropy tracking (distractor)
        if reading > 50:
            entropy_tracker.append(math.log(reading))

        # Bit manipulation for hardware-level simulation (mixed relevance)
        shifted = reading ^ 0b1101
        shifted = (shifted << 2) & 0xFF
        cumulative_shift += shifted % 7

        # Count frequency for mode detection (relevant)
        mode_analysis[reading] += 1

        # Transient noise filtering (partially relevant)
        if reading % 3 == 0 and len(transient_buffer) < 5:
            transient_buffer.append(reading * 0.9)

    # Dead code path - never executed due to logic above (red herring)
    if len(entropy_tracker) > 100:
        avg_entropy = sum(entropy_tracker) / len(entropy_tracker)
        diagnostic_weight += avg_entropy * 0.1

    # Core logic: find most frequent reading (mode)
    max_freq = max(mode_analysis.values())
    modes = [k for k, v in mode_analysis.items() if v == max_freq]
    primary_mode = min(modes)  # Deterministic selection

    # Secondary metric: aggregate shift contribution (misleading intermediate)
    shift_diagnostic = cumulative_shift * 1.5

    # Apply conditional weighting based on buffer state (distractor)
    if len(transient_buffer) == 5:
        diagnostic_weight += 10.5
    else:
        diagnostic_weight += 3.25  # Default weight

    # Final diagnostic combines multiple sources, but only mode matters
    raw_score = primary_mode * 100
    noise_penalty = len(transient_buffer) * 2
    return int(raw_score - noise_penalty + shift_diagnostic * 0)  # shift ignored


def validate_calibration(sequence):
    # Unused validation function (dead code path)
    return all(x > 0 for x in sequence) and len(sequence) <= 50

# Complex preprocessing pipeline
raw_data_stream = [42, 33, 42, 65, 42, 33, 77, 65, 42, 91, 65, 42]

# Distractor transformations
transformed = list(map(lambda x: (x * 2 + 1) if x % 2 else (x // 2), raw_data_stream))
count_summary = Counter(transformed)
filtered_view = [x for x in transformed if x > 40]

# Simulated time-series windowing (irrelevant)
windowed = []
for i in range(0, len(transformed) - 3):
    windowed.append(sum(transformed[i:i+4]))

# Data enrichment with metadata (distractor)
enriched = []
for val in raw_data_stream:
    enriched.append({
        'value': val,
        'is_critical': val > 70,
        'rank': math.floor(math.log(val + 1)) if val > 0 else 0
    })

# Key assignment: reading_log undergoes meaningful transformation
reading_log = [x['value'] * 2 for x in enriched if not x['is_critical']]

# Secondary derived variables (red herring)
binary_projection = [bin(x)[2:] for x in filtered_view]
aggregated_window = sum(windowed) // len(windowed) if windowed else 0

# Core computation buried among distractions
def compute_diagnostic(log):
    base = sum(log) // len(log)
    offset = log.count(84)  # 42*2=84; appears 4 times
    return base + offset * 10

# Critical execution point
final_diagnostic = compute_diagnostic(reading_log)

# Output required result
print(f"Result: {final_diagnostic}")