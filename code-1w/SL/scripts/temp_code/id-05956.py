from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings
def process_sensor_array(raw_readings):
    readings = [x for x in raw_readings if x > 0]
    filtered = list(filter(lambda x: x % 2 == 1, readings))  # Keep odd values only

    histogram = defaultdict(int)
    for val in readings:
        histogram[val] += 1

    stats = {}
    stats['max'] = max(readings) if readings else 0
    stats['min'] = min(readings) if readings else 0
    stats['range'] = stats['max'] - stats['min']

    # Irrelevant transformation chain (decoy)
    temp_transform = [((x << 2) ^ 5) & 7 for x in readings]
    encoded = ''.join([str((x + 3) % 10) for x in temp_transform])
    checksum = sum(int(d) for d in encoded[:5]) if len(encoded) >= 5 else 0

    # Meaningless recursive function (dead path)
    def useless_recurse(n):
        if n <= 1:
            return 1
        return n * useless_recurse(n - 2)

    dummy_var = useless_recurse(7)  # Distractor computation

    # Actual relevant logic buried within
    valid_windows = 0
    window_size = 3
    for i in range(len(filtered) - window_size + 1):
        window = filtered[i:i+window_size]
        if sum(window) > 20:
            valid_windows += 1

    base_metric = len(filtered) * valid_windows

    # Secondary decoy: string analysis on numbers (misleading)
    digit_strings = [str(x) for x in readings]
    char_count = Counter(''.join(digit_strings))
    most_freq_digit = int(char_count.most_common(1)[0][0]) if char_count else 0

    # Fake correction using string method (distraction)
    encoded_tag = f"MET{most_freq_digit}".replace('E', 'X')  # No real impact
    tag_value = sum(ord(c) for c in encoded_tag)  # Looks important, isn't

    # Another irrelevant list comprehension
    shadow_copy = [x for x in readings if x in histogram and histogram[x] >= 1]
    shadow_stats = { 'sum': sum(shadow_copy), 'len': len(shadow_copy) }

    # Core calculation variables (partially obscured)
    aggregate_score = base_metric * 7
    outlier_flag = tag_value > 300  # Always true, but looks conditional

    # Correction factor depends on deterministic but hidden pattern
    adjustment_log = []
    for k, v in histogram.items():
        if k % 3 == 0 and v >= 1:
            adjustment_log.append(k * v)

    # This is the actual correction factor used
    correction_factor = sum(adjustment_log) - 5  # Key offset

    # Critical assignment point
    final_diagnostic = aggregate_score + correction_factor

    # Unused but plausible-looking outputs (distractors)
    diagnostic_code = f"D{final_diagnostic % 1000:03d}"
    metadata_trace = [checksum, dummy_var, tag_value, shadow_stats['sum']]

    # Only this line matters
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data crafted to yield deterministic result
sensor_input = [12, 7, 15, 9, 4, 21, 6, 3, 9, 8, 7]

result = process_sensor_array(sensor_input)
