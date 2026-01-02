from collections import defaultdict, Counter

def analyze_pattern(seq):
    # Irrelevant function: analyzes character patterns (dead end)
    freq = Counter(seq)
    pattern_score = 0
    for ch, count in freq.items():
        if count > 1:
            pattern_score += ord(ch) % 7
    return pattern_score

def auxiliary_transform(data):
    # Distractor function: applies meaningless transformation
    transformed = []
    for i, val in enumerate(data):
        if i % 3 == 0:
            transformed.append(val * 2 + i)
        else:
            transformed.append(val // (i + 1))
    return transformed

def compute_rolling_average readings):
    # Another red herring: computes rolling average but not used in final logic
    window_size = 3
    rolling_avg = []
    for i in range(len(readings) - window_size + 1):
        avg = sum(readings[i:i+window_size]) / window_size
        rolling_avg.append(round(avg, 2))
    return rolling_avg

def validate_calibration(signal):
    # Misleading intermediate validation (never called)
    total_power = 0
    for s in signal:
        if s > 0:
            total_power += s ** 0.5
    return total_power < 100

def process_readings(data, limits):
    # Core logic embedded in noise
    temp_log = defaultdict(int)
    alert_count = 0
    cumulative_shift = 0

    for idx, reading in enumerate(data):
        # Track out-of-bound readings
        if reading < limits['min'] or reading > limits['max']:
            alert_count += 1
            temp_log[idx] = reading  # Logged but only size matters

        # Complex-looking but essential transformation
        adjusted = reading // 2
        if idx % 2 == 0:
            adjusted = (adjusted * 3) % 97
        else:
            adjusted = (adjusted + 5) % 43

        cumulative_shift ^= adjusted  # Bit manipulation with real impact

        # Early termination decoy - looks important but not decisive
        if alert_count > 3:
            break  # This does trigger, but path still converges

    # Real computation hidden among distractions
    base_metric = len(temp_log) * alert_count
    shift_factor = cumulative_shift & 0xFF  # Use lower 8 bits

    # Final result derived from multiple indirect steps
    final_diagnostic = (base_metric + shift_factor) * 17

    # Dead code branch (unreachable due to structure)
    if False:
        fallback = auxiliary_transform(data)
        final_diagnostic -= sum(fallback) % 100

    return final_diagnostic

# Simulated sensor data and threshold configuration
sensor_data = [12, 45, 67, 89, 12, 34, 56, 78, 91, 23]
thresholds = {'min': 15, 'max': 85}

# Orchestration with irrelevant setup
pattern_test = "aabbc"
analyze_pattern(pattern_test)  # Called but result ignored

intermediate = auxiliary_transform(sensor_data)  # Computed but unused
rolling_avgs = compute_rolling_average(sensor_data)  # Stored, never used

# Key execution point
final_diagnostic = process_readings(sensor_data, thresholds)

# Output result as required
print(f"Result: {final_diagnostic}")