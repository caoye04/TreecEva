import math

# Simulated sensor data with noise and metadata
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
pressure_readings = [1013, 1011, 1009, 1015, 1018, 1012, 1010]
humidity_readings = [45, 47, 50, 44, 42, 46, 48]

# Irrelevant auxiliary data (distractor)
legacy_system_codes = ['A7', 'B9', 'C3', 'D2', 'E5']
error_counters = {code: 0 for code in legacy_system_codes}

# Control flags for processing pipeline
control_flags = {
    'enable_filtering': True,
    'use_enhanced_precision': False,
    'apply_calibration': True,
    'debug_mode': True  # Unused in final logic
}

# Misleading intermediate transformation (dead path)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) * 0.95 for x in data]  # Not used

# Data alignment function using zip (relevant)
def align_sensors(temp, press, humid):
    aligned = []
    for t, p, h in zip(temp, press, humid):
        aligned.append({'temp': t, 'press': p, 'humid': h})
    return aligned

# Noise reduction filter (relevant)
def reduce_noise(sample, threshold=1.5):
    if abs(sample['temp'] - 24.0) < threshold:
        sample['temp'] *= 1.01
    if sample['press'] < 1010:
        sample['press'] += 2
    return sample

# Core transformation engine
def process_record(record, calib_factor=0.88):
    calibrated_temp = record['temp'] * calib_factor
    pressure_ratio = record['press'] / 1013.25
    humidity_factor = math.log(record['humid'] + 1)

    # Composite metric calculation
    score = calibrated_temp * pressure_ratio + humidity_factor

    # Decoy computation (irrelevant)
    dummy_score = (record['temp'] + record['press']) % 7

    record['processed_score'] = score
    return record

# Full transformation pipeline
def process_transformations(raw_data, flags):
    filtered_data = []

    # Step 1: Align sensor inputs
    aligned_data = align_sensors(temperature_readings, pressure_readings, humidity_readings)

    # Step 2: Apply noise reduction if enabled
    for entry in aligned_data:
        processed_entry = reduce_noise(entry)
        filtered_data.append(processed_entry)

    # Step 3: Process each record through calibration and scoring
    results = []
    for i, record in enumerate(filtered_data):
        if flags['apply_calibration']:
            result = process_record(record, calib_factor=0.92)
        else:
            result = process_record(record, calib_factor=1.0)
        results.append(result)

    # Step 4: Aggregate final output using summation and combinatorics
    raw_scores = [r['processed_score'] for r in results]

    # Accumulate final output with weighted contributions
    base_accumulator = 0.0
    for idx, score in enumerate(raw_scores):
        weight = (idx + 1) / len(raw_scores)  # Increasing weights
        base_accumulator += score * weight

    # Red herring: unused accumulator with similar name
    backup_accumulator = sum([s * 0.5 for s in raw_scores])

    # Final adjustment based on control flag (not actually used but looks important)
    if flags['use_enhanced_precision']:
        final_value = round(base_accumulator, 6)
    else:
        final_value = int(base_accumulator * 100) / 100.0  # Truncate to 2 decimals

    # Key result variable
    final_output = int(final_value * 10)  # Scale and convert to integer

    # Dead code path (never executed)
    if False:
        for code in error_counters:
            error_counters[code] += 1

    return final_output

# Initialize primary data sequence
index_map = {i: val for i, val in enumerate([1, 1, 2, 3, 5, 8, 13])}  # Fibonacci-like (distractor)
data_sequence = list(align_sensors(temperature_readings, pressure_readings, humidity_readings))

# Execute main processing
final_output = process_transformations(data_sequence, control_flags)

# Print result for extraction
print(f"Target result: {final_output}")