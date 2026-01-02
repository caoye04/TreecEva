def analyze_production_cycles():
    raw_data = ['P1:23', 'P2:45', 'P3:12', 'P4:67', 'P5:34']
    baseline = 25
    adjustment_factor = 1.2
    total_output = 0
    cycle_count = 0
    temp_buffer = []
    outlier_count = 0

    for entry in raw_data:
        label, value_str = entry.split(':')
        value = int(value_str)
        temp_buffer.append(value)

        if value < baseline:
            adjusted_value = value * adjustment_factor
        else:
            adjusted_value = value + (value * 0.1)

        rolling_sum = sum(temp_buffer[-2:]) if len(temp_buffer) >= 2 else 0
        
        # Distractor: complex smoothing logic that doesn't affect final result
        smoothed = 0
        for i, v in enumerate(temp_buffer):
            smoothed += v / (1.5 ** (len(temp_buffer) - i))
        
        # Distractor: unused intermediate metric
        stability_metric = (max(temp_buffer) - min(temp_buffer)) / baseline if temp_buffer else 0

        if value > baseline * 0.8:
            total_output += adjusted_value
            cycle_count += 1
        elif len(temp_buffer) % 2 == 0:
            outlier_count += 1

        # Distractor: irrelevant string processing using zip and enumerate
        labels = [c for c in label]
        digits = [int(d) for d in value_str.zfill(2)]
        for idx, (l, d) in enumerate(zip(labels, digits)):
            pass  # Dead computation

    # Key statement
    efficiency_score = total_output / cycle_count if cycle_count > 0 else 0

    # Print final result as required
    print(f"Result: {efficiency_score}")

analyze_production_cycles()