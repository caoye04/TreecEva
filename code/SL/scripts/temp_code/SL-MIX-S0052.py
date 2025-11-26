def data_validator(records):
    # Irrelevant metadata processing
    file_header = [0xDE, 0xAD, 0xBE, 0xEF]
    header_sum = sum(file_header)  # This is irrelevant distractor
    
    # Main data processing with misleading intermediate steps
    temp_buffer = []
    validation_flags = []
    
    for idx, record in enumerate(records):
        # Misleading conditional that doesn't affect final result
        if idx % 3 == 0:
            validation_flags.append(record * 2)  # Dead code path
        else:
            temp_buffer.append(record)
    
    # Distractor calculations that look important
    buffer_sum = sum(temp_buffer) * 17 % 256
    
    # Actual core logic with modular arithmetic
    processed_data = []
    for record in records:
        # Key transformation using modular arithmetic
        processed_val = (record * 7 + 13) % 100
        processed_data.append(processed_val)
    
    # More irrelevant operations
    debug_counter = len(validation_flags)  # Unused variable
    
    # Final checksum calculation (this is the actual answer)
    checksum = 0
    for val in processed_data:
        checksum = (checksum + val) % 1000
    
    # Final irrelevant transformation that gets discarded
    final_debug = (checksum + buffer_sum) % 500  # Misleading result
    
    return checksum

# Initialize test data
raw_measurements = [45, 23, 67, 89, 12, 34, 78, 56, 91, 14]

# Irrelevant preprocessing steps
calibration_offset = 17
calibrated_data = [x + calibration_offset for x in raw_measurements]

# More distraction - unused operations
quality_metrics = [x * 0.5 for x in calibrated_data]

# Actual processing
processed_records = [x % 50 + 10 for x in calibrated_data]

# Call the validator function
final_checksum = data_validator(processed_records)

# Print the result
print(f"Result: {final_checksum}")