def calculate_final_score(raw_data, limits):
    total = 0
    penalty = 0
    bonus_tracker = []
    temp_sum = 0  # distractor: used in irrelevant computation

    for index, (value, threshold) in enumerate(zip(raw_data, limits)):
        if value < 0:
            continue  # skip negative values

        adjusted_value = value * (1.1 if index % 2 == 0 else 0.9)

        # Irrelevant temperature simulation (distractor block)
        ambient_temp = 20 + index
        heat_factor = ambient_temp / 5
        temp_sum += heat_factor * 0.01  # dead computation

        if adjusted_value > threshold:
            total += int(adjusted_value)
            bonus_tracker.append(index)
            if len(bonus_tracker) > 2:
                total += 5  # bonus for frequent exceedance
        else:
            penalty += 1

        # Early termination condition (rarely triggered, but relevant)
        if penalty >= 3:
            break

    # Another distractor: unused transformation
    scaled_values = [v * 1.05 for v in raw_data if v > 10]
    avg_scaled = sum(scaled_values) / len(scaled_values) if scaled_values else 0

    # Final score with conditional expression
    final_score = total - penalty * 2 if penalty > 0 else total + 10

    # This print is required to output the result
    print(f"Result: {final_score}")
    return final_score

# Input data
sensor_readings = [12, -5, 18, 7, 25, 30]
thresh_levels = [10, 8, 20, 15, 22, 28]

# Execute
final_score = calculate_final_score(sensor_readings, thresh_levels)