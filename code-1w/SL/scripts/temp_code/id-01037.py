def analyze_readings(sensor_data, config):
    # Irrelevant preprocessing block (dead code path)
    temp_buffer = [0] * len(sensor_data)
    for i in range(len(sensor_data)):
        temp_buffer[i] = sensor_data[i] + 2

    # Unused transformation
    shifted_data = [x << 1 for x in sensor_data if x % 3 == 0]

    # Actual relevant logic starts here
    baseline = sum(sensor_data) / len(sensor_data)
    deviations = [abs(x - baseline) for x in sensor_data]
    peak_deviation = max(deviations)

    # Decoy function that's never called
    def false_alarm_detection(seq):
        return [i for i, x in enumerate(seq) if x > 1000]  

    # Real processing step
    filtered = [x for x in deviations if x > config['noise_floor']]
    return {'baseline': baseline, 'peak': peak_deviation, 'count': len(filtered)}


def generate_thresholds(levels):
    # Complex but irrelevant mapping
    thresholds = {}
    for idx, level in enumerate(levels):
        key = f"level_{idx}"
        if level < 5:
            thresholds[key] = level * 17.3
        elif level < 10:
            thresholds[key] = level * 12.8 + 5
        else:
            thresholds[key] = level * 9.1
    # This function is actually unused later
    return {k: v for k, v in sorted(thresholds.items(), reverse=True)}

# Misleading data initialization
raw_logs = [142, 155, 138, 161, 149, 153, 146, 158, 144, 150]
calibration_offsets = {f"sensor_{i}": (i*3 + 7) % 11 for i in range(8)}

# Dead-end computation with bit manipulation red herring
binned_flags = 0
for val in raw_logs:
    if val % 4 == 0:
        binned_flags |= (1 << (val % 8))

# Real signal extraction (obscured)
signal_envelope = [x - 140 for x in raw_logs]

# Another decoy structure
status_matrix = [[i + j for j in range(5)] for i in range(4)]

# Key data structures
threshold_map = {
    'noise_floor': 3.5,
    'sensitivity': 1.8,
    'window': 5
}

def process_metrics(sequence, limits):
    # Core logic buried in distractions
    stats = analyze_readings(sequence, limits)
    
    # Irrelevant nested loop (never affects output)
    dummy_accum = 0
    for i, val in enumerate(sequence):
        for j, (k, v) in enumerate(zip(sequence, sequence[1:])):
            if i < 2 and j % 2 == 0:
                dummy_accum += (val ^ k) & v  # Bitwise red herring

    # Distracting intermediate calculations
    moment = 0
    for i, x in enumerate(sequence):
        moment += (x - stats['baseline']) ** 2
    variance = moment / len(sequence)

    # Meaningful but obscured aggregation
    trend_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_score += 1
        elif sequence[i] < sequence[i-1]:
            trend_score -= 0.5

    # Critical logic hidden among decoys
    diagnostic_weight = stats['count'] * limits['sensitivity']
    if stats['peak'] > 10:
        diagnostic_weight += 5

    # Final computation
    final_diagnostic = int(diagnostic_weight + trend_score)  # This will be the answer
    
    # Never-executed branch (dead code)
    if False:
        final_diagnostic *= 2  

    return final_diagnostic

# Primary execution chain
calibration_sequence = [x * 1.5 for x in signal_envelope]

# Unused sorting operation (distraction)
sorted_diagnostics = sorted(calibration_sequence, key=lambda x: abs(x-1), reverse=True)

# Key assignment statement
final_diagnostic = process_metrics(calibration_sequence, threshold_map)

print(f"Result: {final_diagnostic}")