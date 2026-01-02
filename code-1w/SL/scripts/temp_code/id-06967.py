def analyze_sensor_stream(raw_stream, threshold=0.75):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [x * 1.05 for x in raw_stream if x > 1.2]
    temp_buffer = [x for x in temp_buffer if x < 900]  # Unused cleanup

    # Core data extraction
    normalized = [round(x / max(raw_stream), 4) for x in raw_stream]
    high_freq_peaks = []

    for i in range(2, len(normalized) - 2):
        window = normalized[i-2:i+3]
        if window[2] == max(window) and window[2] > threshold:
            high_freq_peaks.append(i)

    # Distractor: complex but unused frequency analysis
    def compute_harmonic_strength(signal, peaks):
        strength = 0
        for p in peaks:
            left = signal[p-1] if p > 0 else 0
            right = signal[p+1] if p < len(signal)-1 else 0
            strength += abs(left - right)
        return round(strength * 100, 2)

    harmonic_score = compute_harmonic_strength(normalized, high_freq_peaks)  # Not used

    # Real processing begins: extract segments around peaks
    critical_segments = []
    for peak_idx in high_freq_peaks:
        start = max(0, peak_idx - 3)
        end = min(len(raw_stream), peak_idx + 4)
        segment = raw_stream[start:end]
        critical_segments.append(segment)

    # Flatten list using list comprehension instead of itertools (idiomatic Python)
    flattened = [item for sublist in critical_segments for item in sublist]

    # Destructuring assignment (relevant)
    first, *middle, last = flattened[:8] if len(flattened) >= 8 else (flattened + [0]*(8-len(flattened)))

    # Bit manipulation red herring
    checksum = 0
    for val in flattened:
        checksum ^= int(val) & 0xFF
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF

    # Actual signal metric based on middle values
    mid_values = flattened[flattened.index(first)+1:flattened.index(last)]
    if not mid_values:
        mid_values = flattened[1:-1] or [0]

    avg_mid = sum(mid_values) / len(mid_values)

    # String-based status encoding (distractor)
    status_code = ''.join([chr(97 + (int(v) % 26)) for v in mid_values[:5]])
    status_flag = status_code.upper().replace('A', 'X').lower()  # Dead computation

    # Real logic: apply transformation and slice central portion
    processed = [abs(v - avg_mid) ** 0.5 for v in flattened]
    center_slice = processed[len(processed)//3 : 2*len(processed)//3]

    # Final aggregation through tuple unpacking
    summary_stats = (
        sum(center_slice),
        len(center_slice),
        max(center_slice),
        min(center_slice)
    )

    total, count, peak_dev, floor_dev = summary_stats
    quality_adjusted = total * (1 + (peak_dev - floor_dev) / 100)

    return int(round(quality_adjusted))


def process_readings(data_str):
    # Parse input string
    readings = [float(x) for x in data_str.strip().split(',')]

    # Set-based filtering (removes duplicates, distractor element)
    unique_readings = sorted(set(readings))
    duplicate_count = len(readings) - len(unique_readings)  # Unused

    # Slicing to remove potential noise at edges
    trimmed = unique_readings[2:-2] if len(unique_readings) > 6 else unique_readings

    # Call core analyzer with trimmed data
    diagnostic_value = analyze_sensor_stream(trimmed, threshold=0.68)

    # Decoy post-processing chain
    adjustment_factor = 0
    for i, val in enumerate(trimmed):
        if i % 3 == 0 and val > 50:
            adjustment_factor += 0.1
    final_adjustment = adjustment_factor * 10  # Never applied

    # Correct result propagation
    final_diagnostic = diagnostic_value + 100  # Key statement

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated sensor data stream
sensor_input = "105.3,201.7,188.4,195.2,88.9,203.1,197.4,102.8,189.6,201.7,195.2"
final_diagnostic = process_readings(sensor_input)