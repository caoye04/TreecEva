from collections import defaultdict, Counter

# Simulated sensor data analysis with red herrings
def analyze_readings(data_stream):
    readings = [x for x in data_stream if x > 0]
    temp_history = defaultdict(int)
    magnitude_count = Counter()

    # Irrelevant transformation: character frequency in hex codes (distractor)
    hex_frequencies = Counter(hex(x)[2:] for x in readings)
    for hex_char, count in hex_frequencies.items():
        if len(hex_char) > 1:
            temp_history[ord(hex_char[0])] += count

    # Real computation begins: classify magnitudes
    for val in readings:
        if val < 100:
            magnitude_count['low'] += 1
        elif val < 500:
            magnitude_count['medium'] += 1
        else:
            magnitude_count['high'] += 1

    # Dead code path: never accessed due to logic above (misleading)
    if False and magnitude_count['unknown'] > 0:
        correction_factor = sum(ord(c) for c in 'adjust') // 7
        for i in range(correction_factor):
            readings.append(i * 2)

    # Core signal extraction (buried among distractions)
    valid_pairs = []
    for i in range(len(readings) - 1):
        if readings[i] % 10 == 0 and readings[i+1] % 15 == 0:
            valid_pairs.append((readings[i], readings[i+1]))

    pair_strength = sum(a * b for a, b in valid_pairs if a + b > 100)

    # Fake smoothing algorithm (looks important but unused)
    smoothed = []
    window_size = 3
    for j in range(len(readings) - window_size + 1):
        segment = readings[j:j+window_size]
        smoothed.append(sum(segment) / len(segment))

    # Decoy statistical measures
    avg_smooth = sum(smoothed) / len(smoothed) if smoothed else 0
    peak_noise = max((x % 17 for x in readings if x % 2 == 1), default=0)

    # Key computational chain
    base_signal = len([x for x in readings if x % 5 == 0])
    noise_floor = len(readings) - base_signal
    signal_quality = base_signal * 2 - noise_floor

    # Secondary filter: tuple unpacking distraction
    thresholds = [(1, 50), (2, 100), (3, 150)]
    level, limit = thresholds[1]  # only this used

    aggregate_score = signal_quality * level + pair_strength

    # Outlier detection with string method red herring
    digit_chars = ''.join(str(x) for x in readings)
    digit_frequency = {d: digit_chars.count(d) for d in '0123456789'}
    common_digits = [d for d, cnt in digit_frequency.items() if cnt > 2]
    
    # String-based decoy calculation
    checksum_str = ''.join(set(digit_chars))
    decoy_sum = sum(ord(c) * 2 for c in checksum_str[:5])

    # Unused advanced bit manipulation (distractor)
    bit_analysis = 0
    for x in readings:
        bit_analysis ^= (x << 2) | (x >> 3)
        bit_analysis &= 0xFFFF  # clamp

    # Actual answer path
    outlier_candidates = [x for x in readings if x > limit]
    outlier_buffer = len(outlier_candidates) or 1

    final_diagnostic = aggregate_score // outlier_buffer

    # Print required result
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data stream
sensor_input = [10, 25, 15, 30, 60, 45, 17, 90, 105, 40, 55, 120, 85, 135, 19, 70]

result = analyze_readings(sensor_input)