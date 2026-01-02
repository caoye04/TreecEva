from collections import defaultdict, Counter
import math

# Simulated sensor array data processing with diagnostic overhead
def process_sensor_data(raw_readings):
    # Irrelevant preprocessing: normalize timestamps (unused later)
    timestamps = [r[0] for r in raw_readings]
    base_time = min(timestamps)
    normalized_times = [(t - base_time) / 1000.0 for t in timestamps]

    # Relevant: extract sensor values and types
    sensor_values = [r[2] for r in raw_readings]
    sensor_types = [r[1] for r in raw_readings]

    # Distractor: frequency analysis of sensor types (not used in final logic)
    type_counter = Counter(sensor_types)
    dominant_type = type_counter.most_common(1)[0][0]
    type_entropy = sum(- (count / len(sensor_types)) * math.log(count / len(sensor_types)) 
                      for count in type_counter.values())

    # Distractor: build unused time-series structure
    time_series_map = defaultdict(list)
    for t, s_type, value in raw_readings:
        time_series_map[s_type].append((t, value))

    # Phase 1: filter valid high-magnitude readings (threshold = 75)
    high_magnitude = [v for v in sensor_values if abs(v) > 75]
    magnitude_flag = len(high_magnitude) > 3

    # Phase 2: classify by sign pattern (only negative clusters matter)
    negative_runs = []
    current_run = 0
    for v in sensor_values:
        if v < 0:
            current_run += 1
        else:
            if current_run > 0:
                negative_runs.append(current_run)
                current_run = 0
    if current_run > 0:
        negative_runs.append(current_run)

    significant_negative = any(run >= 3 for run in negative_runs)

    # Phase 3: transform via bitwise mixing (relevant path)
    transformed = []
    for i, val in enumerate(sensor_values):
        shifted = abs(val) >> 2
        toggled = shifted ^ i  # bit flip based on index
        wrapped = toggled % 100
        transformed.append(wrapped)

    # Phase 4: conditional amplification (control flow dependent)
    amplified = []
    for x in transformed:
        if x < 50:
            amplified.append(x * 2)
        elif x < 75:
            amplified.append(x + 10)
        else:
            amplified.append(x)

    # Phase 5: integration step (sum of squares mod 1000)
    squared_sum = sum(x * x for x in amplified) % 1000

    # Diagnostic dump (never accessed)
    diagnostics = {
        'sample_count': len(raw_readings),
        'type_diversity': len(type_counter),
        'temporal_span': max(timestamps) - min(timestamps),
        'amplitude_range': (min(sensor_values), max(sensor_values)),
        'entropy': round(type_entropy, 4)
    }

    return squared_sum

# Dead function - looks important but unused
def legacy_compatibility_layer(data, mode='legacy'):
    accumulator = 0
    for item in data:
        if isinstance(item, tuple) and len(item) == 3:
            accumulator += item[1].count('X') * item[2]
    return accumulator << 1

# Unused helper that appears to do security hashing
def obsfuscate_key(sequence):
    mask = 0xA3F1
    result = 0
    for s in sequence:
        result ^= (hash(str(s)) & 0xFFFF) ^ mask
    return result % 99991

# Main execution path
raw_data = [
    (1623540000, 'TEMP-X', 88),
    (1623540010, 'VIBR-A', -45),
    (1623540020, 'VIBR-A', -67),
    (1623540030, 'TEMP-X', -89),
    (1623540040, 'PRESS-Y', 34),
    (1623540050, 'VIBR-A', -91),
    (1623540060, 'VIBR-A', -55),
    (1623540070, 'TEMP-X', 104),
    (1623540080, 'PRESS-Y', -66),
    (1623540090, 'VIBR-A', -77)
]

# Simulated multi-phase pipeline (only 'phase3' contributes to final answer)
phases = ['calibration', 'validation', 'diagnostics', 'phase3']
phase_results = []

for p in phases:
    if p == 'calibration':
        interim = sum(x[2] for x in raw_data[:3])
    elif p == 'validation':
        counts = defaultdict(int)
        for item in raw_data:
            counts[item[1]] += 1
        interim = len([c for c in counts.values() if c > 2])
    elif p == 'diagnostics':
        # Complex string analysis with no impact
        labels = ''.join([t[1][0] for t in raw_data])
        patterns = [labels[i:i+3] for i in range(len(labels)-2)]
        freq = Counter(patterns)
        interim = sum(1 for f in freq.values() if f >= 2)
    elif p == 'phase3':
        # Only this branch matters
        interim = process_sensor_data(raw_data)
    
    phase_results.append(interim)

# Finalization step
def finalize(value):
    # Apply logarithmic scaling (only if positive)
    if value <= 0:
        return -1
    log_val = math.log(value, 2)
    rounded = round(log_val * 100) / 100
    return int(rounded * 100)

checksum = 0
# Key statement
checksum = finalize(sum(phase_results))

print(f"Result: {checksum}")