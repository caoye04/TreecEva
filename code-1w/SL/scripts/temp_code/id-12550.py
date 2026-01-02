def analyze_temperatures(temp_readings):
    high_threshold = 30
    low_threshold = 10
    hot_days = set()
    cold_days = set()
    moderate_sum = 0
    anomaly_count = 0

    for i, temp in enumerate(temp_readings):
        if temp > high_threshold:
            hot_days.add(i)
        elif temp < low_threshold:
            cold_days.add(i)
        else:
            moderate_sum += temp

        # Distractor: tracking anomalies but not used later
        if abs(temp - 20) > 15:
            anomaly_count += 1

    return hot_days, cold_days, moderate_sum


def transform_labels(labels):
    # Irrelevant transformation
    upper_labels = [label.upper() for label in labels]
    reversed_labels = [label[::-1] for label in upper_labels]
    return reversed_labels  # Not used


def calculate_final_score(data_chunk):
    base_score = 0
    penalty = 0
    bonus = 0

    # Summation with conditional logic
    for val in data_chunk:
        if val % 2 == 0:
            base_score += val // 2
        else:
            base_score -= val // 3

        # Bonus logic based on set membership
        if val in {7, 11, 13, 17}:
            bonus += 5

        # Dead code path (never executed due to condition)
        if val < 0 and val > 100:
            penalty += 10

    # Final adjustment
    final_value = base_score + bonus
    return final_value

# Main execution
if __name__ == "__main__":
    temperature_data = [12, 15, 35, 8, 22, 31, 5, 19, 27]
    label_metadata = ['jan', 'feb', 'mar', 'apr', 'may']

    # Extract relevant numerical features
    hot_set, cold_set, mod_sum = analyze_temperatures(temperature_data)

    # Create derived dataset for scoring
    processed_data = []
    for t in temperature_data:
        processed_data.append((t + 5) * 2 // 3)

    # Transform but ignore result
    ignored_transform = transform_labels(label_metadata)

    # Key computation
    final_score = calculate_final_score(processed_data)

    # Print required output
    print(f"Result: {final_score}")