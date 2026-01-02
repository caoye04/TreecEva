def analyze_production_cycle():
    raw_data = [124, 87, 156, 203, 98, 142, 111]
    thresholds = [100, 150, 200]
    temp_buffer = []
    total_output = 0
    cycle_count = 0
    debug_trace = []

    for index, value in enumerate(raw_data):
        adjusted_value = value * (0.98 + index * 0.01)
        temp_buffer.append(adjusted_value)

        if value > thresholds[0]:
            category_flag = 'high'
            secondary_mask = [i for i in range(3) if value > thresholds[i]]
            cycle_count += 1
            contribution = 0

            for i, threshold in enumerate(thresholds):
                if value > threshold:
                    contribution += threshold // (i + 1)

            total_output += contribution
            debug_trace.append((index, contribution))
        else:
            category_flag = 'low'
            backup_calc = value % 13

    # Misleading intermediate: this appears important but isn't used
    outlier_count = sum(1 for x in raw_data if x < 100 or x > 200)
    avg_base = sum(raw_data) / len(raw_data)
    normalized_total = 0
    for val in raw_data:
        normalized_total += val / avg_base

    # Real computation path resumes
    cycle_time = 0
    for i in range(len(raw_data)):
        if i % 2 == 0:
            cycle_time += 1.5
        else:
            cycle_time += 0.8

    efficiency_score = total_output / (cycle_time * 0.95)

    # Dead code branch - never executed but adds cognitive load
    if False:
        fallback_score = sum(temp_buffer) / 1000
        efficiency_score = max(efficiency_score, fallback_score)

    print(f"Result: {efficiency_score}")

analyze_production_cycle()