def process_data(sequence):
    data_sequence = [15, 22, 8, 31, 17, 24, 9, 12, 28, 5]
    threshold_check = lambda x: x > 15 and x % 2 == 0
    filtered_values = [x for x in data_sequence if threshold_check(x)]
    data_mapping = {x: x * 2 for x in filtered_values}
    temp_result = sum(data_mapping.values())
    final_count = temp_result // len(filtered_values)
    print(f"Result: {final_count}")
    return final_count

final_count = process_data([15, 22, 8, 31, 17, 24, 9, 12, 28, 5])