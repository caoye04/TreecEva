from itertools import compress, cycle

# Simulated sensor network data with metadata
timestamps = list(range(100, 200, 2))
raw_readings = [t * 0.3 + (t % 7) * 0.1 for t in timestamps]
sensor_ids = [f'SENSOR_{i:03d}' for i in range(50)]

# Irrelevant auxiliary data (distraction)
legacy_codes = [f'LC{i}{hex(i * 3)[-1]}' for i in range(50)]
redundant_flags = [i % 4 == 0 for i in range(50)]

# Data alignment via compress using a red herring condition
valid_mask = [(r + 5) % 6 < 4 for r in raw_readings]
filtered_readings = list(compress(raw_readings, valid_mask))
filtered_timestamps = list(compress(timestamps, valid_mask))

# Misleading transformation chain (not used in final result)
shadow_buffer = [x * 0.9 + 2 for x in filtered_readings]
scaled_buffer = [abs(y - 1) ** 0.5 for y in shadow_buffer]

# Core diagnostic logic
smoothed = []
for i in range(2, len(filtered_readings)):
    val = (filtered_readings[i-2] + filtered_readings[i-1] + filtered_readings[i]) / 3
    smoothed.append(val)

defect_indicators = []
for s in smoothed:
    if s > 35.0:
        defect_indicators.append(int(s % 7))
    elif s < 25.0:
        defect_indicators.append(-int(s % 4))
    else:
        defect_indicators.append(1)

# Create threshold map with dummy entries
base_threshold = 3.5
threshold_map = {k: base_threshold + (ord(k[-1]) % 5) for k in ['low', 'mid', 'high']}
threshold_map['override'] = 0  # unused override (distraction)

# Spurious list built but only length matters indirectly
event_log = []
for idx, reading in enumerate(filtered_readings):
    if idx % 7 == 0 and reading > 30:
        event_log.append(f'ALERT_{idx}')

# Actual processing function
def process_readings(data, thresholds):
    cumulative_score = 0
    pattern_cycle = cycle([1, -1, 2])

    for i, entry in enumerate(data):
        # Inject cyclic modulation (mild distraction)
        mod_factor = next(pattern_cycle)
        adjusted = entry * 0.75 + mod_factor

        # Key classification logic
        if adjusted > 34.2:
            cumulative_score += 5
        elif adjusted < 24.8:
            cumulative_score -= 3
        else:
            cumulative_score += 1

    # Final adjustment using defect indicators (critical path)
    spike_count = sum(1 for x in defect_indicators if x > 0)
    dip_count = sum(1 for x in defect_indicators if x < 0)
    net_volatility = spike_count - dip_count

    # Distractor computation (looks important but not decisive)
    historical_bias = len(event_log) * 0.5 - 2
    debug_weight = abs(historical_bias)  # unused

    # True answer determinant
    final_score = cumulative_score + net_volatility
    return int(final_score * 1.2)  # stabilization factor

# Filtered data construction (key execution point)
filtered_data = [x for x in smoothed if 20 < x < 40]

# Critical statement
final_diagnostic = process_readings(filtered_data, threshold_map)

print(f"Result: {final_diagnostic}")