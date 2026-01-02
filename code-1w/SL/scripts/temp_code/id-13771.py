import math

# Simulated sensor data processing with multiple distractions
def collect_diagnostics():
    raw_signals = [0.3, 0.82, 0.67, 0.91, 0.44, 0.76, 0.58, 0.83]
    timestamps = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]
    device_ids = ['D-001', 'D-002', 'D-003', 'D-004']

    # Irrelevant mapping for red herring
    id_to_location = {did: f'Zone-{i+1}' for i, did in enumerate(device_ids)}
    location_readings = {loc: [] for loc in id_to_location.values()}

    # Distractor: complex unused transformation
    def transform_signal(x, a=1.5, b=0.5):
        return a * math.sin(x * math.pi) + b * math.log(x + 1) if x > 0 else 0

    transformed = [transform_signal(val) for val in raw_signals]  # Dead path

    # Real signal filter (only values above 0.7)
    high_readings = [s for s in raw_signals if s > 0.7]

    # Another distraction: string-based tagging
    labels = ['low', 'high', 'medium']
    label_map = {l: idx for idx, l in enumerate(labels)}
    signal_categories = []
    for v in raw_signals:
        if v < 0.55:
            signal_categories.append('low')
        elif v < 0.75:
            signal_categories.append('medium')
        else:
            signal_categories.append('high')
    
    # Decoy aggregation (never used later)
    category_count = {lbl: signal_categories.count(lbl) for lbl in labels}
    total_low = category_count['low']
    total_high = category_count['high']

    # Actual processing path begins here
    moving_avg = []
    window_size = 3
    for i in range(len(raw_signals) - window_size + 1):
        avg = sum(raw_signals[i:i+window_size]) / window_size
        moving_avg.append(round(avg, 2))

    # Filter based on moving average threshold
    stable_periods = [m for m in moving_avg if m > 0.65]

    # Key intermediate result
    baseline_ref = sum(stable_periods) / len(stable_periods) if stable_periods else 0.0

    # Simulate data corruption check (irrelevant but looks important)
    checksum_str = ''.join(f'{int(s*100):02d}' for s in raw_signals)
    valid_checksum = len(checksum_str) % 2 == 0 and '99' not in checksum_str

    # Red herring: unused nested function
    def validate_integrity(data):
        if not data:
            return False
        squared_sum = sum(x**2 for x in data)
        return squared_sum > 1.0

    # Real filtering logic
    filtered_data = []
    for i, val in enumerate(raw_signals):
        if val in high_readings and val >= moving_avg[i % len(moving_avg)]:
            filtered_data.append(val)

    # Auxiliary distraction: set operations (required feature)
    unique_categories = set(signal_categories)
    excluded_zones = set(['Zone-1', 'Zone-3'])
    active_tags = unique_categories - {'low'} | {'critical'}  # Mix of set ops

    # String method distraction
    device_tag_summary = ''.join(device_ids).upper().replace('-', '')
    hex_digest = ''.join(format(ord(c), 'x') for c in device_tag_summary[:4])

    # Core analysis function (uses filtered_data and threshold)
    def analyze_readings(data, threshold):
        if not data:
            return 0.0
        
        # Apply exponential weighting
        weighted_sum = 0.0
        decay_factor = 0.85
        for idx, reading in enumerate(reversed(data)):
            weight = decay_factor ** idx
            weighted_sum += reading * weight
        
        # Normalize by effective count
        norm_factor = sum(decay_factor ** i for i in range(len(data)))
        adjusted_mean = weighted_sum / norm_factor
        
        # Final classification
        if adjusted_mean > threshold:
            outcome_code = 42  # arbitrary code
            temp_flag = f"HIGH-{outcome_code}"
            # Use string method
            flag_clean = temp_flag.lower().strip('-high-')
            try:
                outcome_digit = int(flag_clean)
            except:
                outcome_digit = 1
            return int(adjusted_mean * 100) + outcome_digit
        else:
            return int(adjusted_mean * 100)

    # Critical execution point
    final_diagnostic = analyze_readings(filtered_data, threshold=0.75)

    # Dead code branch — looks like post-processing
    if final_diagnostic > 100:
        correction = math.tanh(final_diagnostic / 1000)
        final_diagnostic = int(final_diagnostic * correction)

    # Output required format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute and capture
result = collect_diagnostics()