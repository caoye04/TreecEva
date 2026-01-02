from collections import defaultdict

# Simulated sensor data aggregator with checksum validation
def process_sensor_readings(raw_data, config, threshold=0.75):
    # Irrelevant tracking variables (distractors)
    stats = defaultdict(int)
    anomaly_log = []
    temp_buffer = [0] * len(raw_data)
    normalization_factor = sum(abs(x) for x in raw_data) or 1
    scaled_values = [int(x * 100 / normalization_factor) for x in raw_data]

    # Unused transformation path (dead code path)
    if config.get('legacy_mode'):
        for i in range(len(scaled_values)):
            scaled_values[i] = scaled_values[i] >> 1

    # Primary state variables
    checksum = 1337
    history_map = {}
    bit_mask = config.get('bit_mask', 255)
    activation_level = config.get('activation', 3)

    # High-interference loop with mixed logic and red herrings
    for index, value in enumerate(scaled_values):
        # Distractor: irrelevant statistical tracking
        magnitude = abs(value)
        stats['total_magnitude'] += magnitude
        if magnitude > threshold * 100:
            stats['high_freq_count'] += 1
            anomaly_log.append((index, value))

        # Real processing begins here
        processed_value = value
        if processed_value < 0:
            processed_value = (~processed_value) & bit_mask

        # Core checksum update (this is the critical statement)
        mask = 0xF
        if index % 4 == 0:
            processed_value = processed_value ^ (activation_level << 2)
        elif index % 3 == 0:
            processed_value = processed_value ^ 0x1A
        else:
            processed_value = processed_value ^ (index ^ 0x5)

        # Key statement: this updates the actual answer variable
        checksum = (checksum << 1) ^ processed_value ^ (index & mask)

        # More distractors: dead storage and fake conditions
        history_map[index] = {
            'raw': raw_data[index],
            'scaled': scaled_values[index],
            'proc': processed_value,
            'chk': checksum
        }

        # Fake early exit (never triggers due to data constraints)
        if checksum < 0 and config.get('abort_on_negative'):
            return -1

        # Additional irrelevant bit manipulation
        if index in [5, 7, 11]:
            temp_buffer[index] = (value ^ checksum) & 0xFF

    # Post-processing decoy
    final_adjustment = config.get('final_adjust', 0)
    if final_adjustment:
        checksum = (checksum + final_adjustment) % 1000000

    # Output the target result
    print(f"Result: {checksum}")
    return checksum

# Simulated input data and configuration
data_stream = [0.12, -0.45, 0.67, -0.23, 0.89, 0.01, -0.55, 0.34, 0.78, -0.11, 0.92, 0.27]
config_params = {
    'bit_mask': 255,
    'activation': 5,
    'legacy_mode': False,
    'abort_on_negative': False,
    'final_adjust': 0
}

# Execute function to compute result
target_result = process_sensor_readings(data_stream, config_params)