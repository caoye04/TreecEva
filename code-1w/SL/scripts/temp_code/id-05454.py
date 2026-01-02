def analyze_sequence(values):
    mid_section = values[2:6]
    base_sum = sum(mid_section)
    adjustment = base_sum // 4
    return base_sum + adjustment


def process_metrics(data):
    offset = len(data) % 3
    trimmed = data[offset:offset+5]
    normalized = [x * 2 for x in trimmed]
    return normalized


def final_adjustment(input_list):
    processed = [x - 1 for x in input_list if x > 3]
    total_score = sum(processed)
    bonus = total_score % 7
    total_score += bonus
    return total_score

# Main execution sequence
data_stream = [4, 1, 3, 5, 2, 7, 8, 4, 9]
extracted_metrics = data_stream[1:8:2]
analyzed_result = analyze_sequence(extracted_metrics)
processed_data = process_metrics([analyzed_result, 4, 6, 3, 8, 2])
total_score = final_adjustment(processed_data)
print(f"Result: {total_score}")