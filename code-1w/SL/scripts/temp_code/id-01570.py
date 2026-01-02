def analyze_sensor_data(raw_readings):
    filtered_data = [x for x in raw_readings if x > 0]
    baseline = sum(filtered_data) / len(filtered_data) if filtered_data else 0

    # Irrelevant transformation (distractor)
    inverted_map = {i: 1/(v+1) for i, v in enumerate(raw_readings)}
    normalization_factor = max(inverted_map.values()) if inverted_map else 1

    # Dummy statistical analysis (dead code path)
    def calculate_entropy(data):
        from math import log
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        entropy = 0
        total = len(data)
        for count in freq.values():
            p = count / total
            entropy -= p * log(p)
        return entropy

    entropy_value = calculate_entropy(filtered_data[:5]) if len(filtered_data) > 5 else 0.0

    # Character frequency distraction (string manipulation red herring)
    status_log = "sensor_ok sensor_fail sensor_ok sensor_pending"
    status_words = status_log.split()
    word_count = {word: status_words.count(word) for word in set(status_words)}
    avg_char_length = sum(len(w) for w in status_words) / len(status_words)

    # Real computation chain begins here (nested logic with distractors)
    moving_averages = []
    window_size = 3
    for i in range(len(filtered_data) - window_size + 1):
        window_avg = sum(filtered_data[i:i+window_size]) / window_size
        moving_averages.append(window_avg)

    # Secondary irrelevant list comp (distractor)
    squared_residuals = [((x - baseline) ** 2) for x in filtered_data]
    variance_estimate = sum(squared_residuals) / len(squared_residuals) if squared_residuals else 0

    # Key data structure transformation (relevant)
    trend_analysis = []
    for i in range(1, len(moving_averages)):
        if moving_averages[i] > moving_averages[i-1]:
            trend_analysis.append(1)
        elif moving_averages[i] < moving_averages[i-1]:
            trend_analysis.append(-1)
        else:
            trend_analysis.append(0)

    # Accumulation with bit manipulation decoy
    rising_trends = sum(1 for t in trend_analysis if t == 1)
    falling_trends = sum(1 for t in trend_analysis if t == -1)
    stability_points = len([t for t in trend_analysis if t == 0])

    # Bitwise red herring (no impact on result)
    magic_key = rising_trends ^ falling_trends
    checksum = (magic_key << 2) | (stability_points & 7)

    # Core calculation (hidden among distractions)
    aggregate_score = 0
    for idx, val in enumerate(moving_averages):
        if idx % 2 == 0:
            aggregate_score += val * 0.7
        else:
            aggregate_score += val * 0.3

    # Correction based on trend bias
    trend_bias = rising_trends - falling_trends
    if trend_bias > 0:
        correction_factor = trend_bias * 12.5
    elif trend_bias < 0:
        correction_factor = abs(trend_bias) * -8.2
    else:
        correction_factor = 50

    # Final diagnostic (target variable)
    final_diagnostic = aggregate_score + correction_factor

    # Unused debug print (distractor)
    # print(f'Debug: baseline={baseline}, entropy={entropy_value}, checksum={checksum}')

    # Irrelevant string slicing operation
    report_id = 'RPT-2023-XJ9'#
    project_code = report_id[4:8]
    version_flag = report_id[-1]

    # Output only the target result
    print(f"Result: {final_diagnostic}")

# Simulate sensor input
sensor_input = [120, -5, 130, 125, 140, -1, 138, 142, 137, 145]
analyze_sensor_data(sensor_input)