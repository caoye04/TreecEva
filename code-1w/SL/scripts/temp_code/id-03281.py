def analyze_system_metrics(raw_readings, threshold_multiplier=1.75):
    # Irrelevant preprocessing: normalize text labels (distractor)
    labels = ['sensor_A', 'sensor_B', 'sensor_C', 'sensor_D']
    normalized_labels = [label.upper().replace('_', '') for label in labels]
    label_map = {i: lbl for i, lbl in enumerate(normalized_labels)}

    # Core data: temperature readings in Fahrenheit
    temperature_profile = [t * 1.8 + 32 for t in raw_readings]  # Convert C to F

    # Dead code path: unused transformation (red herring)
    def deprecated_filter(data):
        return [x for x in data if x > 0]  # Never called

    # Bitwise manipulation on index (misleading but unused)
    masked_indices = [(i << 2) ^ 5 for i in range(len(temperature_profile))]
    mask_sum = sum(maskged_indices)  # Intentional typo → becomes dead variable

    # Real logic begins: find first critical reading above dynamic threshold
    base_threshold = sum(temperature_profile) / len(temperature_profile)
    critical_threshold = base_threshold * threshold_multiplier

    alert_index = -1
    for idx, temp in enumerate(temperature_profile):
        if temp > critical_threshold:
            alert_index = idx
            break

    # Unused alternate search using zip (decoy logic)
    temp_with_prev = list(zip(temperature_profile, [0] + temperature_profile[:-1]))
    spike_count = 0
    for curr, prev in temp_with_prev:
        if curr - prev > 20:
            spike_count += 1  # Computed but not used

    # Distractor: irrelevant accumulation over characters
    debug_code = "ERRX9"
    ascii_offset = sum(ord(c) for c in debug_code if c.isalpha()) % 100

    # Spurious dictionary operations (red herring)
    status_registry = {
        'initialized': True,
        'readings_taken': len(temperature_profile),
        'breach_count': len([t for t in temperature_profile if t > critical_threshold]),
        'units': 'F'
    }
    status_registry['checksum'] = status_registry['readings_taken'] * 17
    status_registry.pop('units')  # Manipulated but not used

    # Key parameters for final calculation
    scaling_factor = 0.86
    offset_correction = 14.5

    # Critical assignment — target of the question
    if alert_index != -1:
        final_diagnostic = temperature_profile[alert_index] * scaling_factor + offset_correction
    else:
        final_diagnostic = base_threshold * 0.5

    # Irrelevant slicing operation (meant to distract)
    recent_trend = temperature_profile[-3:]  # Last three readings, unused
    trend_delta = recent_trend[-1] - recent_trend[0] if len(recent_trend) == 3 else 0

    # Final output
    print(f'Result: {final_diagnostic}')

# Simulate execution with fixed input
raw_input = [22, 19, 25, 30, 18, 27]
analyze_system_metrics(raw_input)