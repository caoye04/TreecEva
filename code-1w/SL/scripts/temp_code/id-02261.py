def process_data(data_stream, key):
    checksum = 0
    temp_records = []
    metadata_map = {}
    
    for index, (value, flag) in enumerate(zip(data_stream, key)):
        if flag % 3 == 0:
            adjusted_value = value * 2 + index
        elif flag % 3 == 1:
            adjusted_value = value + 5
        else:
            adjusted_value = value // 2
            
        temp_records.append(adjusted_value)
        checksum += adjusted_value

    # Irrelevant transformation on metadata (distractor)
    for i, record in enumerate(temp_records):
        metadata_map[i] = {'raw': record, 'squared': record ** 2, 'active': record > 30}

    outlier_filter = lambda x: x > 10
    filtered_values = list(filter(outlier_filter, temp_records))

    # Dead code path - never executed due to constant condition (distractor)
    if len(temp_records) < 0:
        backup_result = sum(temp_records) / len(temp_records)
    else:
        pass  # Simulated branch with no effect

    # Core logic: sum of filtered values modulo 1000
    aggregation = sum(filtered_values) % 1000
    
    # Additional irrelevant computation
    avg_metadata = 0
    if metadata_map:
        total_sq = sum(entry['squared'] for entry in metadata_map.values() if entry['active'])
        count_active = sum(1 for entry in metadata_map.values() if entry['active'])
        avg_metadata = total_sq / count_active if count_active > 0 else 0

    final_result = aggregation + 10  # Final adjustment
    return final_result

# Input data
stream_buffer = [12, 8, 15, 23, 7, 19, 4]
validation_key = [3, 1, 4, 6, 2, 9, 5]

intermediate_calc = [x ** 2 for x in stream_buffer if x < 10]  # Unused side computation
misc_lookup = {k: v for k, v in enumerate(['A','B','C','D'])}  # Unused structure

final_output = process_data(stream_buffer, validation_key)
print(f"Result: {final_output}")