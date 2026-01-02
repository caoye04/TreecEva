def analyze_metrics(raw_values, threshold=5.0):
    stats = {}
    temp_buffer = []
    cumulative = 0

    for idx, val in enumerate(raw_values):
        if val > threshold:
            temp_buffer.append(val * 0.9)
        else:
            temp_buffer.append(val + 0.1)

    normalized = [round(x / max(temp_buffer), 3) for x in temp_buffer]

    count_high = sum(1 for x in normalized if x > 0.7)
    count_low = sum(1 for x in normalized if x < 0.3)

    # Distractor: irrelevant statistical moment calculation
    moment_sum = 0
    for i, x in enumerate(normalized):
        moment_sum += (x - 0.5)**3  # skewness proxy - unused later

    stats['valid_count'] = len([x for x in raw_values if x >= 0])
    stats['processed_max'] = max(normalized)
    return normalized, stats


def filter_anomalies(data_stream):
    clean_stream = []
    anomalies = []
    moving_avg = 0

    for i, item in enumerate(data_stream):
        if i == 0:
            moving_avg = item
        else:
            moving_avg = moving_avg * 0.7 + item * 0.3

        if abs(item - moving_avg) > 0.5:
            anomalies.append((i, item))
        else:
            clean_stream.append(item)

    # Dead code path - never accessed in normal execution
    if len(anomalies) > 100:
        fallback = [x for x in data_stream if x > 0.1]
        return fallback

    return clean_stream


def calculate_rating(input_batch):
    base_rating = 0
    adjustment = 0.0

    for val in input_batch:
        if val > 0.8:
            base_rating += 3
        elif val > 0.5:
            base_rating += 2
        else:
            base_rating += 1

    # Use of zip to align indices and values for secondary analysis
    index_shift = sum(i * 0.1 for i, v in enumerate(input_batch) if v < 0.4)

    # Conditional expression with distractor logic
    bonus = 5 if all(v > 0.2 for v in input_batch) else 0
    penalty = 2 if len(input_batch) % 2 == 1 else 0

    # Unused intermediate calculation - red herring
    entropy_approx = 0
    for p in input_batch:
        if p > 0:
            entropy_approx -= p * __import__('math').log(p, 2)

    adjustment = index_shift + bonus - penalty
    return int(base_rating + adjustment)

# Main execution flow
raw_input = [6.2, 4.1, 7.3, 2.8, 5.5, 3.0, 8.4]
processed_data, metadata = analyze_metrics(raw_input)
cleaned_data = filter_anomalies(processed_data)

# Key statement
final_score = calculate_rating(cleaned_data)

print(f"Result: {final_score}")