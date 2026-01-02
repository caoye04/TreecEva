from collections import defaultdict, Counter
import math

# System telemetry simulation for a distributed sensor array
sensor_ids = [101, 102, 103, 104, 105]
signal_logs = [
    '101:23.1,102:19.5,103:27.3',
    '101:25.4,104:31.2,105:18.9',
    '102:20.1,103:26.7,104:29.8',
    '101:24.3,105:19.7,103:28.0',
    '104:30.5,102:18.9,101:22.8'
]

# Irrelevant telemetry metadata (distractor)
telemetry_headers = ['HDR_X9', 'CHKSUM_4F', 'MODE_G', 'ENC_NONE']
packet_sequence = list(range(1000, 1005))
buffer_overflow_flag = False
retry_attempts = 3

# Parse raw logs into structured data
collected_signals = defaultdict(list)
for log in signal_logs:
    readings = log.split(',')
    for reading in readings:
        sensor, value = reading.split(':')
        collected_signals[int(sensor)].append(float(value))

# Dead code path - never executed but looks relevant (distractor)
def legacy_calibrate(x):
    return (x * 0.97) + 2.1  # unused

def deprecated_filter(seq):
    return [x for x in seq if x > 20]  # unused

# Auxiliary functions with plausible but misleading computations
noise_floor = 17.5
adjustment_factor = 0.88

# Simulated environmental interference (mostly irrelevant)
environmental_drift = {
    t: 2.1 * math.sin(t * 0.4) for t in range(len(signal_logs))
}
compensation_curve = [math.cos(i * 0.3) for i in range(10)]
baseline_offset = sum(compensation_curve[:5]) / 5

# Real processing begins here
filtered_signals = {}
for sid, readings in collected_signals.items():
    avg = sum(readings) / len(readings)
    if avg > noise_floor:
        filtered_signals[sid] = round(avg * adjustment_factor, 2)

# Secondary transformation: map to categories
signal_strength_map = {}
for sid, val in filtered_signals.items():
    if val < 20:
        signal_strength_map[sid] = 'LOW'
    elif val < 25:
        signal_strength_map[sid] = 'MEDIUM'
    else:
        signal_strength_map[sid] = 'HIGH'

# Bit manipulation red herring (complex but unused)
rolling_hash = 0
for sid in sorted(collected_signals.keys()):
    rolling_hash ^= (sid << 2)
    rolling_hash += len(collected_signals[sid])
    rolling_hash &= 0xFFFF  # keep within 16 bits

# Decoy diagnostic function that looks important
def compute_system_health(data):
    count = len(data)
    total_len = sum(len(v) for v in data.values())
    return (total_len * 100) // (count * 3) if count else 0

health_score = compute_system_health(collected_signals)  # distractor result

# Actual key computation uses set operations and combinatorics
active_sensors = set(filtered_signals.keys())
high_power_sensors = {s for s, v in filtered_signals.items() if v >= 24.0}
divergent_pairs = set()

for s1 in active_sensors:
    for s2 in active_sensors:
        if s1 < s2 and abs(s1 - s2) % 2 == 1:
            divergent_pairs.add((s1, s2))

# Use of Counter for frequency analysis (relevant)
pattern_counter = Counter()
for readings in collected_signals.values():
    pattern_counter[len(readings)] += 1

mode_frequency = pattern_counter.most_common(1)[0][1]

# System key derived from structural properties
system_key = len(divergent_pairs) + mode_frequency

# Core analysis function (depends on correct data flow)
def analyze_pattern(signals, key):
    values = sorted([v for v in signals.values()])
    n = len(values)
    if n < 3:
        return sum(values)
    
    # Weighted combination using trigonometric weighting
    weights = [math.cos(i * math.pi / (n + 1)) for i in range(n)]
    weighted_sum = sum(val * w for val, w in zip(values, weights))
    
    # Key modifies result through bit shifting
    shift_amount = key % 5
    adjusted_result = int(weighted_sum * (1 << shift_amount))
    
    # Final adjustment using set difference size
    all_ids = {101, 102, 103, 104, 105}
    missing_count = len(all_ids - active_sensors)
    return adjusted_result - (missing_count * 100)

# Misleading intermediate call (looks like final step)
temporary_diagnostic = analyze_pattern(filtered_signals, 7)

# Critical execution point
final_diagnostic = analyze_pattern(collected_signals, system_key)

# Print final answer as required
print(f"Result: {final_diagnostic}")