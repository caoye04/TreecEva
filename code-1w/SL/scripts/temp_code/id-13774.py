from collections import defaultdict, Counter
import math

def main():
    # Sensor simulation data (real-world context: environmental monitoring)
    raw_readings = [23.4, 19.5, 20.1, 25.3, 18.2, 21.0, 19.8, 24.7, 20.3, 19.9]
    calibration_offsets = {'sensor_a': 0.15, 'sensor_b': -0.20, 'sensor_c': 0.08}
    baseline = 20.0

    # Irrelevant auxiliary data (distractor)
    legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1']
    metadata_log = defaultdict(lambda: 'unknown')
    for code in legacy_codes:
        metadata_log[code] += '_processed'

    # Step 1: Apply calibration (relevant)
    calibrated = [r + calibration_offsets.get(f'sensor_{chr(97+i%3)}', 0) for i, r in enumerate(raw_readings)]

    # Step 2: Detect anomalies using hysteresis logic (relevant)
    anomalies = []
    prev_state = False
    for val in calibrated:
        current_state = (val > baseline + 2.0) if not prev_state else (val > baseline - 1.0)
        if current_state and not prev_state:
            anomalies.append(val)
        prev_state = current_state

    # Dead code path (red herring)
    def deprecated_filter(x):
        return x > 25.0  # Never called
    obsolete_mask = list(map(deprecated_filter, raw_readings))

    # Step 3: Categorize readings (relevant)
    categories = []
    for val in calibrated:
        if val < baseline - 1.0:
            categories.append('low')
        elif val > baseline + 1.0:
            categories.append('high')
        else:
            categories.append('normal')
    category_count = Counter(categories)

    # Irrelevant set operations (distractor)
    unique_categories = set(categories)
    expected_categories = {'low', 'normal', 'high', 'critical'}
    missing_categories = expected_categories - unique_categories  # Always {'critical'}

    # Step 4: Simulate diagnostic flags (mixed relevance)
    flags = []
    for i, val in enumerate(calibrated):
        flag = 0
        if val > 24.0:
            flag |= 1 << 3
        if i % 3 == 0:
            flag |= 1 << 1
        if val < 19.0:
            flag |= 1 << 2
        flags.append(flag)
    total_flags = sum(flags)

    # Unused transformation (distractor)
    transformed_data = [
        math.log(abs(x)) * math.cos(math.pi * i / 4)
        for i, x in enumerate(calibrated)
    ]

    # Step 5: Prepare processed data structure (relevant)
    processed_data = {
        'readings': calibrated,
        'anomalies': anomalies,
        'category_distribution': category_count,
        'indices': {
            'high': [i for i, v in enumerate(calibrated) if v > baseline + 1.0],
            'low': [i for i, v in enumerate(calibrated) if v < baseline - 1.0]
        }
    }

    # Step 6: Build threshold map with fallback logic (relevant)
    threshold_map = defaultdict(float)
    threshold_map['warning_high'] = baseline + 1.5
    threshold_map['critical_high'] = baseline + 3.0
    threshold_map['warning_low'] = baseline - 1.5
    default_retries = [3, 2, 4]

    # Fake retry simulation (dead code)
    attempt_status = {}
    for idx, retries in enumerate(default_retries):
        for r in range(retries):
            attempt_status[(idx, r)] = (r == retries - 1)  # Success on last try

    # Step 7: Core analysis function (relevant)
    def analyze_readings(data, thresholds):
        high_threshold = thresholds['warning_high']
        low_threshold = thresholds['warning_low']
        critical_high = thresholds['critical_high']

        # Count severe deviations
        severe_high = len([v for v in data['readings'] if v >= critical_high])
        moderate_high = len([v for v in data['readings'] if high_threshold <= v < critical_high])
        severe_low = len(data['indices']['low'])

        # Compute weighted diagnostic score
        weights = {"severe_high": 3.0, "moderate_high": 1.5, "severe_low": 2.0}
        score = (
            weights["severe_high"] * severe_high +
            weights["moderate_high"] * moderate_high +
            weights["severe_low"] * severe_low
        )

        # Add adjustment based on anomaly timing (complex logic)
        if len(data['anomalies']) > 0:
            first_anomaly_idx = data['readings'].index(data['anomalies'][0])
            if first_anomaly_idx < len(data['readings']) // 2:
                score *= 1.2

        # Red herring calculation (never affects output)
        phantom_risk = 0.0
        for k, cnt in data['category_distribution'].items():
            if k in ['low', 'high']:
                phantom_risk += math.sqrt(cnt + 1) * 0.3

        return int(score)  # Final result as integer

    # Execute key statement
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")

if __name__ == '__main__':
    main()