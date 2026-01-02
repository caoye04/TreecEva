def analyze_sensor_data(raw_stream, window_size=7):
    # Irrelevant preprocessing: reverse and slice (distractor)
    reversed_stream = raw_stream[::-1]
    trimmed = reversed_stream[3:-2]
    processed = [x * 1.05 for x in raw_stream if x > 0]  # Distractor: not used later

    # Real computation begins: sliding window peak detection
    peaks = []
    for i in range(len(raw_stream) - window_size + 1):
        window = raw_stream[i:i + window_size]
        avg = sum(window) / len(window)
        if window[window_size // 2] > avg * 1.2:
            peaks.append(1)
        else:
            peaks.append(0)

    # Bit manipulation red herring
    bit_accumulator = 0
    for p in peaks[:5]:
        bit_accumulator = (bit_accumulator << 1) | p
    # Unused result

    # Frequency analysis (partially relevant)
    frequency_map = {}
    for val in raw_stream:
        rounded = int(round(val / 10) * 10)
        frequency_map[rounded] = frequency_map.get(rounded, 0) + 1

    # Extract dominant bands (decoy logic)
    sorted_bands = sorted(frequency_map.items(), key=lambda x: -x[1])
    top_band_value = sorted_bands[0][0] if sorted_bands else 0

    # Actual signal conditioning path
    filtered_values = [v for v in raw_stream if v > top_band_value * 0.3]
    normalized = [(v - min(filtered_values)) / (max(filtered_values) - min(filtered_values) + 1e-8) for v in filtered_values]

    # Simulate binary diagnostic flags from normalized values
    diagnostics = []
    for n in normalized:
        flag = 0
        if n > 0.7:
            flag |= 4
        if n < 0.3:
            flag |= 2
        if abs(n - 0.5) < 0.1:
            flag |= 1
        diagnostics.append(flag)

    # Threshold engine (unused alternative)
    class ThresholdEngine:
        def __init__(self, levels):
            self.levels = levels

        def evaluate(self, x):
            return sum(1 for lvl in self.levels if x > lvl)

    engine = ThresholdEngine([0.25, 0.5, 0.75])
    # Not used

    # Actual threshold application
    thresholds = {'critical': 0.8, 'warning': 0.6, 'info': 0.4}
    high_alerts = sum(1 for n in normalized if n > thresholds['critical'])
    mid_alerts = sum(1 for n in normalized if thresholds['warning'] < n <= thresholds['critical'])

    # Decoy statistical summary
    stats_summary = {
        'mean': sum(normalized) / len(normalized),
        'variance': sum((x - sum(normalized)/len(normalized))**2 for x in normalized) / len(normalized),
        'skew': 0  # Placeholder
    }

    # Core aggregation logic (depends on diagnostics and thresholds)
    def aggregate_diagnostics(flags, thresh):
        total_score = 0
        for f in flags:
            if f & 4:  # High signal
                total_score += 3
            elif f & 2:  # Low signal
                total_score -= 1
            if f & 1:  # Mid signal
                total_score += 1
        # Modulate by threshold-relative density
        adjustment = (high_alerts - mid_alerts) * 2
        return total_score + adjustment

    final_diagnostic = aggregate_diagnostics(diagnostics, thresholds)
    
    # Dead code path: recursive traversal (never called)
    def traverse_tree(data):
        if len(data) <= 1:
            return data[0] if data else 0
        mid = len(data) // 2
        left = traverse_tree(data[:mid])
        right = traverse_tree(data[mid+1:])
        return left ^ right

    # Output the target variable
    print(f"Result: {final_diagnostic}")