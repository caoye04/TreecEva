def analyze_metrics(raw_values, threshold=0.75):
    filtered = [v for v in raw_values if v > threshold]
    outliers = [v for v in raw_values if v < 0.1]
    adjustment = len(outliers) * 0.05
    return sum(filtered) - adjustment


def validate_input(data_stream):
    if not data_stream:
        return False
    total_entries = len(data_stream)
    valid_count = sum(1 for x in data_stream if 0 <= x <= 1)
    return valid_count == total_entries


def calculate_performance(entries):
    temp_buffer = []
    scaling_factor = 0.85
    base_offset = 10
    dummy_accumulator = 0

    for i in range(len(entries)):
        entry = entries[i]
        if i % 2 == 0:
            processed = entry ** 2 * scaling_factor
            temp_buffer.append(processed)
        else:
            processed = entry * 1.1 + base_offset
            temp_buffer.append(processed)
        
        # Distractor: irrelevant accumulation
        dummy_accumulator += i * 0.01

    # Real logic: use only even-index contributions for score
    even_contributions = [temp_buffer[i] for i in range(0, len(temp_buffer), 2)]
    avg_contribution = sum(even_contributions) / len(even_contributions) if even_contributions else 0

    # Secondary metric (unused but computed)
    peak_value = max(temp_buffer) if temp_buffer else 0
    normalized_peak = peak_value / (avg_contribution + 1e-5)

    # Final performance score based on average contribution and bonus
    bonus = 5 if normalized_peak > 2 else 2
    final_score = int(avg_contribution + bonus)

    # Irrelevant sorting (distractor)
    sorted_buffer = sorted(temp_buffer, reverse=True)
    for val in sorted_buffer:
        if val < 5:
            break

    return final_score

# Main execution
benchmark_data = [0.5, 0.4, 0.9, 0.2, 0.7, 0.6]

if validate_input(benchmark_data):
    intermediate_metric = analyze_metrics(benchmark_data, threshold=0.5)
    auxiliary_result = intermediate_metric * 2
    final_score = calculate_performance(benchmark_data)
else:
    final_score = -1

print(f"Result: {final_score}")